import math
import pathlib
import types

import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import or_
from src import models
from src import utils
from sqlalchemy import distinct, func
from fastapi import HTTPException


def get_amps(db: Session, page: int = 0, page_size: int = 20, **kwargs):
    query = db.query(distinct(models.AMP.accession)).outerjoin(models.Metadata)

    # Mapping from filter keys to table columns
    metadata_cols = {
        'habitat': 'microontology',
        'host': 'host_scientific_name',
        'origin': 'origin_scientific_name',
        'sample': 'sample'}
    for key, value in kwargs.items():
        if key in {'habitat', 'host', 'origin', 'sample'}:
            if value:
                query = query.filter(getattr(models.Metadata, metadata_cols[key]) == value)
        elif key == 'family':
            if value:
                query = query.filter(getattr(models.AMP, key) == value)
        else:
            pass
    accessions = query.offset(page * page_size).limit(page_size).all()
    # if len(accessions) == 0:
    #     raise HTTPException(status_code=400, detail='invalid filter applied.')
    data = [get_amp(accession, db) for accession, in accessions]
    info = get_page_info(kind='amp', page=page, page_size=page_size, db=db)
    paged_amps = types.SimpleNamespace()
    paged_amps.info = info
    paged_amps.data = data
    return paged_amps


def get_amp(accession: str, db: Session):
    amp_obj = db.query(models.AMP).filter(models.AMP.accession == accession).first()
    if not amp_obj:
        raise HTTPException(status_code=400, detail='invalid accession received.')
    gene_seqs = db.query(models.GMSC.gene_sequence).filter(models.GMSC.AMP == accession).all()
    features = utils.get_amp_features(amp_obj.sequence)
    feature_graph_points = utils.get_graph_points(amp_obj.sequence)
    features["graph_points"] = feature_graph_points

    metadata = get_amp_metadata(accession, db, page=0, page_size=5)

    setattr(amp_obj, "gene_sequences", gene_seqs)
    setattr(amp_obj, "features", features)
    setattr(amp_obj, "metadata", metadata)
    return amp_obj


def get_amp_metadata(accession: str, db: Session, page: int, page_size: int):
    data = db.query(
        models.Metadata.AMPSphere_code,
        models.Metadata.GMSC,
        models.GMSC.gene_sequence,
        models.Metadata.sample,
        models.Metadata.microontology,
        models.Metadata.environmental_features,
        models.Metadata.host_tax_id,
        models.Metadata.host_scientific_name,
        models.Metadata.latitude,
        models.Metadata.longitude,
        models.Metadata.origin_tax_id,
        models.Metadata.origin_scientific_name,
    ).outerjoin(
        models.GMSC, models.Metadata.GMSC == models.GMSC.accession
    ).filter(
        models.Metadata.AMPSphere_code == accession
    ).offset(page * page_size).limit(page_size).all()
    if len(data) == 0:
        raise HTTPException(status_code=400, detail='invalid accession received.')
    metadata_info = get_page_info(kind='amp.metadata', accession=accession, page_size=page_size, page=page, db=db)
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
        'habitat': 'microontology',
        'host': 'host_scientific_name',
        'origin': 'origin_scientific_name',
        'sample': 'sample'}
    for key, value in kwargs.items():
        if value:
            query = query.filter(getattr(models.Metadata, metadata_cols[key]) == value)
    accessions = query.offset(page * page_size).limit(page_size).all()
    # if len(accessions) == 0:
    #     raise HTTPException(status_code=400, detail='invalid filter applied.')
    data = [get_family(accession, db) for accession, in accessions]
    info = get_page_info(kind='family', page=page, page_size=page_size, db=db)
    paged_families = types.SimpleNamespace()
    paged_families.info = info
    paged_families.data = data
    return paged_families


def get_family(accession: str, db: Session):
    family = dict(
        accession=accession,
        consensus_sequence='',  # FIXME calculate consensus sequence.
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
    if len(features) == 0:
        raise HTTPException(status_code=400, detail='invalid accession received.')
    else:
        statstics = pd.json_normalize(features).describe().round(3)
        stats = statstics.index.tolist()
        return dict(zip(stats, utils.df_to_formatted_json(statstics)))


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
    q = db.query(models.AMP.family).filter(models.AMP.family == accession).first()
    in_db = bool(q)
    if not in_db:
        raise HTTPException(status_code=400, detail='invalid accession received.')
    else:
        prefix = pathlib.Path('https://119.3.63.164:443/v1/families/' + accession + '/downloads/')
    path_bases = dict(
        alignment=str(prefix.joinpath('{}.aln')),
        sequences=str(prefix.joinpath('{}.faa')),
        hmm_logo=str(prefix.joinpath('{}.png')),
        hmm_profile=str(prefix.joinpath('{}.hmm')),
        sequence_logo=str(prefix.joinpath('{}.pdf')),
        tree_figure=str(prefix.joinpath('{}.ascii')),
        tree_nwk=str(prefix.joinpath('{}.nwk'))
    )
    return {key: item.format(accession) for key, item in path_bases.items()}


def search_by_text(db: Session, text: str, page: int, page_size: int):
    """
    FIXME.
    :param query:
    :param db:
    :return:
    """
    query = db.query(distinct(models.AMP.accession)).outerjoin(models.Metadata)

    query = query.filter(or_(
        models.AMP.accession.like(text),
        models.AMP.family.like(text),
        models.Metadata.GMSC.like(text),
        models.Metadata.sample.like(text),
        models.Metadata.microontology.like(text),
        models.Metadata.origin_scientific_name.like(text),
        models.Metadata.host_scientific_name.like(text),
    ))

    accessions = query.offset(page * page_size).limit(page_size).all()
    # print(accessions)
    return [get_amp(accession, db) for accession, in accessions]


def get_statistics(db: Session):
    # TODO SPHEREs with num_amps < 8 should not be treated as families.
    # TODO display two numbers for num_genomes / num_metagenomes
    #               (analyzed_genomes..., num_...containing amps)
    return dict(
        num_amps=db.query(func.count(models.AMP.accession)).scalar(),
        num_families=db.query(func.count(distinct(models.AMP.family))).scalar(),
        num_hosts=db.query(func.count(distinct(models.Metadata.host_scientific_name))).scalar() - 1,
        num_habitats=db.query(func.count(distinct(models.Metadata.microontology))).scalar() - 1,
        num_genomes=db.query(func.count(distinct(models.Metadata.sample))). \
                        filter(models.Metadata.microontology == '').scalar() - 1,
        num_metagenomes=db.query(func.count(distinct(models.Metadata.sample))). \
                        filter(models.Metadata.microontology != '').scalar(),
    )


def get_page_info(kind: str, page_size: int, page: int, db: Session, accession: str = None):
    if kind == 'amp':
        total_items = db.query(models.AMP.accession).count()
    elif kind == 'family':
        total_items = db.query(models.AMP.family).distinct().count()
    elif kind == 'amp.metadata':
        total_items = db.query(models.Metadata.GMSC). \
            filter(models.Metadata.AMPSphere_code == accession).count()
    elif kind == 'family.metadata':
        total_items = db.query(models.Metadata.GMSC).outerjoin(models.AMP). \
            filter(models.AMP.family == accession).count()
    else:
        total_items = 0
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
    family, = zip(*db.query(models.AMP.family).limit(100).distinct())
    habitat, = zip(*db.query(models.Metadata.microontology).limit(100).distinct())
    host, = zip(*db.query(models.Metadata.host_scientific_name).limit(100).distinct())
    sample, = zip(*db.query(models.Metadata.sample).limit(100).distinct())
    origin, = zip(*db.query(models.Metadata.origin_scientific_name).limit(100).distinct())
    return dict(
        family=family,
        habitat=habitat,
        host=host,
        sample=sample,
        origin=origin,
    )