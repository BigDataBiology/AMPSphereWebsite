import math
import pathlib
import types
from pprint import pprint

import pandas as pd
from sqlalchemy.orm import Session, Query
from sqlalchemy import or_, and_
from src import models
from src import utils
from sqlalchemy import distinct, func, true, false
from sqlalchemy.sql.expression import func as sql_func
from fastapi import HTTPException


def get_amps(db: Session, page: int = 0, page_size: int = 20, **kwargs):
    query = db.query(distinct(models.AMP.accession)).outerjoin(models.Metadata)

    # Mapping from filter keys to table columns
    metadata_cols = {'habitat': 'general_envo_name', 'microbial_source': 'microbial_source', 'sample_genome': 'sample'}
    AMP_cols = {
        'pep_length_interval': 'length', 'mw_interval': 'molecular_weight',
        'pI_interval': 'isoelectric_point', 'charge_interval': 'charge'}
    for key, value in kwargs.items():
        if key in {'habitat', 'microbial_source', 'sample_genome'}:
            if value:
                query = query.filter(getattr(models.Metadata, metadata_cols[key]) == value)
        elif key == 'family':
            if value:
                query = query.filter(getattr(models.AMP, key) == value)
        elif key in ['pep_length_interval', 'mw_interval', 'pI_interval', 'charge_interval']:
            if value:
                min_max: [str] = value.split(',')
                col_values = getattr(models.AMP, AMP_cols[key])
                query = query.filter(and_(float(min_max[0]) <= col_values, col_values <= float(min_max[1])))
        else:
            pass
    accessions = query.offset(page * page_size).limit(page_size).all()
    # if len(accessions) == 0:
    #     raise HTTPException(status_code=400, detail='invalid filter applied.')
    data = [get_amp(accession, db) for accession, in accessions]
    info = get_query_page_info(q=query, page=page, page_size=page_size)
    paged_amps = types.SimpleNamespace()
    paged_amps.info = info
    paged_amps.data = data
    return paged_amps


def get_amp(accession: str, db: Session):
    amp_obj = db.query(models.AMP).filter(models.AMP.accession == accession).first()
    if not amp_obj:
        raise HTTPException(status_code=400, detail='invalid accession received.')
    # gene_seqs = db.query(models.GMSC.gene_sequence).filter(models.GMSC.AMP == accession).all()
    # features = utils.get_amp_features(amp_obj.sequence)
    feature_graph_points = utils.get_graph_points(amp_obj.sequence)
    metadata = get_amp_metadata(accession, db, page=0, page_size=5)
    setattr(amp_obj, "feature_graph_points", feature_graph_points)
    # setattr(amp_obj, "gene_sequences", gene_seqs)
    setattr(amp_obj, "secondary_structure", utils.get_secondary_structure(amp_obj.sequence))
    setattr(amp_obj, "metadata", metadata)
    return amp_obj


def get_amp_helicalwheel(accession):
    return "data/pre_computed/amps/helical_wheels/helicalwheel_{}.svg".format(accession)


def get_amp_metadata(accession: str, db: Session, page: int, page_size: int):
    query = db.query(
        models.Metadata.AMPSphere_code,
        models.Metadata.GMSC,
        models.GMSC.gene_sequence,
        models.Metadata.sample,
        models.Metadata.general_envo_name,
        models.Metadata.environment_material,
        models.Metadata.latitude,
        models.Metadata.longitude,
        models.Metadata.microbial_source,
        models.Metadata.specI,
    ).outerjoin(
        models.GMSC, models.Metadata.GMSC == models.GMSC.accession
    ).filter(
        models.Metadata.AMPSphere_code == accession
    )
    data = query.offset(page * page_size).limit(page_size).all()
    if len(data) == 0:
        raise HTTPException(status_code=400, detail='invalid accession received.')
    metadata_info = get_query_page_info(q=query, page_size=page_size, page=page)
    metadata = types.SimpleNamespace()
    metadata.info = metadata_info
    metadata.data = data
    return metadata


def get_amp_features(accession: str, db: Session):
    q = db.query(models.AMP.sequence).filter(models.AMP.accession == accession).first()
    if not q:
        raise HTTPException(status_code=400, detail='invalid accession received.')
    else:
        seq, = q
    return utils.get_amp_features(seq)


def get_families(db: Session, page: int, page_size: int, **kwargs):
    query = db.query(distinct(models.AMP.family)).outerjoin(models.Metadata)

    # Mapping from filter keys to table columns
    metadata_cols = {
        'habitat': 'general_envo_name',
        'microbial_source': 'microbial_source',
        'sample': 'sample'}
    for key, value in kwargs.items():
        if value:
            query = query.filter(getattr(models.Metadata, metadata_cols[key]) == value)
    accessions = query.offset(page * page_size).limit(page_size).all()
    # if len(accessions) == 0:
    #     raise HTTPException(status_code=400, detail='invalid filter applied.')
    data = [get_family(accession, db) for accession, in accessions]
    info = get_query_page_info(q=query, page=page, page_size=page_size)
    paged_families = types.SimpleNamespace()
    paged_families.info = info
    paged_families.data = data
    return paged_families


def get_family(accession: str, db: Session):
    family = dict(
        accession=accession,
        consensus_sequence=utils.cal_consensus_seq(accession),
        num_amps=db.query(func.count(models.AMP.accession).filter(models.AMP.family == accession)).scalar(),
        feature_statistics=get_fam_features(accession, db),
        distributions=get_distributions(accession, db),
        associated_amps=get_associated_amps(accession, db),
        downloads=get_fam_downloads(accession, db)
    )
    return family


def get_fam_metadata(accession: str, db: Session, page: int, page_size: int):
    amp_accessions = db.query(models.AMP.accession).filter(models.AMP.family == accession).all()
    amp_accessions = [accession for accession, in amp_accessions]
    # TODO FIX HERE
    m = db.query(models.Metadata).filter(models.Metadata.AMPSphere_code.in_(amp_accessions)). \
        offset(page * page_size).limit(page_size).all()
    return [row.__dict__ for row in m]


def get_fam_features(accession: str, db: Session):
    amps = db.query(models.AMP).filter(models.AMP.family == accession).all()
    features = [utils.get_amp_features(amp.sequence, include_graph_points=False) for amp in amps]
    accessions = [amp.accession for amp in amps]
    if len(features) == 0:
        raise HTTPException(status_code=400, detail='invalid accession received.')
    else:
        statistics = pd.json_normalize(features).round(3)
        # statistics.index = accessions
        # print(statistics)
        return dict(zip(accessions, utils.df_to_formatted_json(statistics)))


def get_associated_amps(accession, db):
    amp_accessions = db.query(models.AMP.accession).filter(models.AMP.family == accession).all()
    return [accession for accession, in amp_accessions]


def get_distributions(accession: str, db: Session):
    if accession.startswith('AMP'):
        raw_data = db.query(models.Metadata).filter(models.Metadata.AMPSphere_code == accession).all()
    elif accession.startswith('SPHERE'):
        raw_data = db.query(models.Metadata).outerjoin(models.AMP).filter(models.AMP.family == accession).all()
    else:
        raw_data = []
    if len(raw_data) == 0:
        raise HTTPException(status_code=400, detail='invalid accession received.')
    return utils.compute_distribution_from_query_data(raw_data)


def get_fam_downloads(accession, db: Session):
    # TODO change prefix here for easier maintenance.
    local_ip = utils.cfg['local_ip']
    q = db.query(models.AMP.family).filter(models.AMP.family == accession).first()
    in_db = bool(q)
    if not in_db:
        raise HTTPException(status_code=400, detail='invalid accession received.')
    else:
        prefix = pathlib.Path(local_ip + ':443/v1/families/' + accession + '/downloads/')
    path_bases = dict(
        alignment=str(prefix.joinpath('{}.aln')),
        sequences=str(prefix.joinpath('{}.faa')),
        hmm_logo=str(prefix.joinpath('{}.png')),
        hmm_profile=str(prefix.joinpath('{}.hmm')),
        sequence_logo=str(prefix.joinpath('{}.pdf')),
        tree_figure=str(prefix.joinpath('{}.ascii')),
        tree_nwk=str(prefix.joinpath('{}.nwk'))
    )
    return {key: 'http://' + item.format(accession) for key, item in path_bases.items()}


def search_by_text(db: Session, text: str, page: int, page_size: int):
    """
    FIXME.
    :param query:
    :param db:
    :return:
    """
    query = db.query(distinct(models.AMP.accession)).outerjoin(models.Metadata)
    # Consider blank space as + for query text.
    query = query.filter(or_(
        models.AMP.accession.like(text),
        models.AMP.family.like(text),
        models.Metadata.GMSC.like(text),
        models.Metadata.sample.like(text),
        models.Metadata.general_envo_name.like(text),
        models.Metadata.microbial_source.like(text),
    ))

    accessions = query.offset(page * page_size).limit(page_size).all()
    amps_data = [get_amp(accession, db) for accession, in accessions]
    page_info = get_query_page_info(q=query, page=page, page_size=page_size)
    paged_searchresult = types.SimpleNamespace()
    paged_searchresult.info = page_info
    paged_searchresult.data = amps_data
    return paged_searchresult


def get_statistics(db: Session):
    # TODO SPHEREs with num_amps < 8 should not be treated as families.
    # TODO display two numbers for num_genomes / num_metagenomes
    #               (analyzed_genomes..., num_...containing amps)
    # TODO FIX here.
    stats = db.query(models.Statistics).first()
    return dict(
        num_genes=stats.gmsc,
        num_amps=stats.amp,
        num_families=stats.family,
        num_habitats=stats.general_envo_name,
        num_genomes=db.query(func.count(distinct(models.Metadata.sample))).filter(
            models.Metadata.is_metagenomic == "False").scalar(),
        num_metagenomes=db.query(func.count(distinct(models.Metadata.sample))).filter(
            models.Metadata.is_metagenomic == "True").scalar(),
    )


def get_query_page_info(q: Query, page_size: int, page: int):
    total_items = q.count()
    total_page = math.ceil(total_items / page_size)
    current_page = page
    # info = types.SimpleNamespace()
    # info.currentPage = current_page
    # info.pageSize = page_size
    # info.totalPage = total_page
    # info.totalItem = total_items
    info = dict(
        currentPage=current_page,
        pageSize=page_size,
        totalPage=total_page,
        totalItem=total_items
    )
    return info


def get_filters(db: Session):
    # FIXME not using the first 100 rows.
    # TODO use query API to get filter suggestion, not all available filters (impossible).
    family, = zip(*db.query(models.AMP.family).distinct())
    habitat, = zip(*db.query(models.Metadata.general_envo_name).distinct())
    sample, = zip(*db.query(models.Metadata.sample).distinct())
    microbial_source, = zip(*db.query(models.Metadata.microbial_source).distinct())
    peplen_min, peplen_max, mw_min, mw_max, \
    pI_min, pI_max, charge_min, charge_max = db.query(
        func.min(models.AMP.length),
        func.max(models.AMP.length),
        func.min(models.AMP.molecular_weight),
        func.max(models.AMP.molecular_weight),
        func.min(models.AMP.isoelectric_point),
        func.max(models.AMP.isoelectric_point),
        func.min(models.AMP.charge),
        func.max(models.AMP.charge),
    ).first()
    # print(query)
    # print(query.__dict__())
    return dict(
        family=family,
        habitat=habitat,
        sample=sample,
        microbial_source=microbial_source,
        pep_length=dict(min=peplen_min, max=peplen_max),
        molecular_weight=dict(min=mw_min, max=mw_max),
        isoelectric_point=dict(min=pI_min, max=pI_max),
        charge_at_pH_7=dict(min=charge_min, max=charge_max)
    )


def mmseqs_search(seq: str, db):
    query_id = str(utils.uuid.uuid4())
    query_time_now = utils.datetime.now()
    tmp_dir = pathlib.Path(utils.cfg['tmp_dir'])
    input_seq_file = tmp_dir.joinpath(query_id + '.input')
    output_file = tmp_dir.joinpath(query_id + '.output')
    stdout_file = tmp_dir.joinpath(query_id + '.stdout')
    output_format = 'query,target,fident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,evalue,bits,qseq,tseq'
    # TODO calculate alignment string based on qaln,taln,gapopen,qstart,qend,tstart,alnlen
    # TODO add hint when the length of input sequence is not between 8 and 98
    # HINT: The search result may not reflect the reality as your sequence is too long/short.
    if not tmp_dir.exists():
        tmp_dir.mkdir(parents=True)
    with open(input_seq_file, 'w') as f:
        f.write(seq)
    # sensitivity = 1
    command_base = 'mmseqs createdb {query_seq} {query_seq}.mmseqsdb && ' \
                   'mmseqs search {query_seq}.mmseqsdb  {database} {out}.mmseqsdb {tmp_dir} -a && ' \
                   'mmseqs convertalis {query_seq}.mmseqsdb {database} {out}.mmseqsdb {out} --format-output {output_format}'
    command = command_base.format_map({
        'query_seq': input_seq_file,
        'database': utils.cfg['mmseqs_db'],
        'out': output_file,
        'tmp_dir': str(tmp_dir),
        'output_format': output_format,
        # 's': sensitivity
    })
    try:
        # TODO redirect the stdout to a temporary file and return its content when there is no match.
        with open(stdout_file, 'w') as f:
            utils.subprocess.run(command, shell=True, check=True, stdout=f)  ## FIXME
    except utils.subprocess.CalledProcessError as e:
        print('error when executing the command (code {})'.format(e))
        print(e.output)
        return None  # TODO better handle this
    else:
        columns = ['query_identifier', 'target_identifier', 'sequence_identity', 'alignment_length',
                   'number_mismatches', 'number_gap_openings', 'domain_start_position_query',
                   'domain_end_position_query', 'domain_start_position_target',
                   'domain_end_position_target', 'E_value', 'bit_score', 'seq_query', 'seq_target']
        try:
            df = pd.read_table(output_file, sep='\t', header=None)
        except pd.errors.EmptyDataError:
            df = pd.DataFrame(columns=columns)
        df.columns = columns
        format_alignment0 = lambda x: utils.format_alignment(
            x['seq_query'], x['seq_target'], x['bit_score'], x['domain_start_position_target'] - 1, x['domain_end_position_target']
        ).split('\n')[0:3]
        if df.shape[0] > 0:
            df['alignment_strings'] = df[['seq_query', 'seq_target', 'bit_score','domain_start_position_target', 'domain_end_position_target']].apply(format_alignment0, axis=1)
            df['family'] = df['target_identifier'].apply(lambda x: get_family_by_amp(x, db))
        records = df.to_dict(orient='records')
        # pprint(records)
        return records


def get_family_by_amp(amp_accession, db):
    family, = db.query(models.AMP.family).filter(models.AMP.accession == amp_accession).first()
    # print(type(family))
    # print(family)
    return family


def hmmscan_search(seq: str):
    query_id = str(utils.uuid.uuid4())
    query_time_now = utils.datetime.now()
    tmp_dir = pathlib.Path(utils.cfg['tmp_dir'])
    input_seq_file = tmp_dir.joinpath(query_id + '.input')
    output_file = tmp_dir.joinpath(query_id + '.output')
    stdout_file = tmp_dir.joinpath(query_id + '.stdout')
    # TODO add hint when the length of input sequence is not between 8 and 98
    # HINT: The search result may not reflect the reality as your sequence is too long/short.

    if not tmp_dir.exists():
        tmp_dir.mkdir(parents=True)
    # with open(input_seq_file, 'w') as f:
    #     f.write(f'>submitted_sequence\n{seq}')
    with open(input_seq_file, 'w') as f:
        f.write(seq)  # already in fasta format

    command_base = 'hmmscan --domtblout {out} {hmm_profiles} {query_seq}'
    command = command_base.format_map({
        'out': output_file,
        'hmm_profiles': utils.cfg['hmmprofile_db'],
        'query_seq': input_seq_file,
        'out_tmp': tmp_dir.joinpath(query_id + '.tmp')
    })
    try:
        # TODO redirect the stdout to a temporary file and return its content when there is no match.
        with open(stdout_file, 'w') as f:
            utils.subprocess.run(command, shell=True, check=True, stdout=f)  ## FIXME
    except utils.subprocess.CalledProcessError as e:
        print('error when executing the command (code {})'.format(e))
        print(e.output)
        return None
    else:
        columns = [
            'target_name', 'target_accession', 'target_length', 'query_name',
            'query_accession', 'query_length', 'E_value', 'score', 'bias',
            'domain_index', 'num_domain', 'c_Evalue', 'i_Evalue', 'score',
            'bias', 'from_hmm', 'to_hmm', 'from_ali', 'to_ali', 'from_env',
            'to_env', 'acc', 'description_of_target']
        try:
            df = pd.read_table(output_file, header=2, skipfooter=10, sep='\s+', engine='python')
        except pd.errors.EmptyDataError:
            df = pd.DataFrame(columns=columns)
        df.columns = columns
        # print(df)
        records = df.to_dict(orient='records')
        # pprint(records)
        return records
