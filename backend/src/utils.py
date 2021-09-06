import configparser
import pathlib
import subprocess

from Bio.SeqUtils.ProtParam import ProtParamData
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from datetime import datetime
from pprint import pprint
import uuid
import pandas as pd
from Bio import SearchIO
import livingTree as lt


def parse_config():
    parser = configparser.ConfigParser()
    parser.read('config/config.ini')
    return parser['DEFAULT']


cfg = parse_config()

# Protparam scales:
# kd → Kyte & Doolittle Index of Hydrophobicity
# Flex → Normalized average flexibility parameters (B-values)
# hw → Hopp & Wood Index of Hydrophilicity
# em → Emini Surface fractional probability (Surface Accessibility)

aalist = ['A', 'C', 'D', 'E',
          'F', 'G', 'H', 'I',
          'K', 'L', 'M', 'N',
          'P', 'Q', 'R', 'S',
          'T', 'V', 'Y', 'W']

# Colour scheme in Lesk (Introduction to Bioinformatics)
# Uses 5 groups (note Histidine): 
# Small nonpolar	    G, A, S, T                  Orange
# Hydrophobic	        C, V, I, L, P, F, Y, M, W   Green
# Polar                 N, Q, H		                Magenta
# Negatively charged    D, E		                Red
# Positively charged    K, R                        Blue
colorpallete = {'G': 'orange', 'A': 'orange', 'S': 'orange', 'T': 'orange',
                'C': 'g', 'V': 'g', 'I': 'g', 'L': 'g',
                'P': 'g', 'F': 'g', 'Y': 'g', 'M': 'g',
                'W': 'g', 'N': 'm', 'Q': 'm', 'H': 'm',
                'D': 'r', 'E': 'r', 'K': 'b', 'R': 'b'}

# these hydrophobicity scales are minmax organized
# the higher the value, more hydrophobic the aa is
scales = {'Parker': {'W': 1.0, 'F': 0.96, 'L': 0.96,
                     'M': 0.71, 'V': 0.685, 'Y': 0.595,
                     'C': 0.43, 'P': 0.395, 'A': 0.395,
                     'H': 0.395, 'R': 0.29, 'T': 0.24,
                     'G': 0.215, 'K': 0.215, 'Q': 0.2,
                     'S': 0.175, 'N': 0.15, 'E': 0.11,
                     'D': 0.0, 'I': 0.9},
          'ez': {'L': -4.92, 'I': -4.92, 'V': -4.04,
                 'F': -2.98, 'M': -2.35, 'W': -2.33,
                 'A': -1.81, 'C': -1.28, 'G': -0.94,
                 'Y': 0.14, 'T': 2.57, 'S': 3.4,
                 'H': 4.66, 'Q': 5.54, 'K': 5.55,
                 'N': 6.64, 'E': 6.81, 'D': 8.72,
                 'R': 14.92, 'P': 0.0}}


def get_amp_features(seq, include_graph_points=True):
    """
    :param seq:
    :return:
        Dict{
            MW: ...,
            Length: ...,
            Molar_extinction: [..., ...],
            Aromaticity: ...,
            GRAVY: ...,
            Instability_index: ...,
            Isoeletric_point: ...,
            Charget_at_pH_7: ...,
            Secondary_structure: [..., ..., ...],
        }
    """
    analyzed_seq = ProteinAnalysis(str(seq))

    out = {'Secondary_structure': dict(zip(['helix', 'turn', 'sheet'], analyzed_seq.secondary_structure_fraction())),
           'Length': analyzed_seq.length,
           'Molar_extinction': dict(zip(['cysteines_reduced', 'cystines_residues'],
                                        analyzed_seq.molar_extinction_coefficient())),
           'Aromaticity': round_3(analyzed_seq.aromaticity()),
           'GRAVY': round_3(analyzed_seq.gravy()),
           'MW': round_3(analyzed_seq.molecular_weight()),
           'Charge_at_pH_7': round_3(analyzed_seq.charge_at_pH(7.0)),
           'Instability_index': round_3(analyzed_seq.instability_index()),
           'Isoelectric_point': round_3(analyzed_seq.isoelectric_point()),
           'graph_points': get_graph_points(seq) if include_graph_points else None}
    return out


def get_graph_points(seq):
    graphs = ['transfer_energy', 'hydrophobicity_parker', 'surface_accessibility', 'flexibility']
    param_dict_list = [scales['ez'], scales['Parker'], ProtParamData.em, ProtParamData.Flex]
    wd = 5
    analyzed_seq = ProteinAnalysis(str(seq))
    graph_points = {}
    for graph, param_dict in zip(graphs, param_dict_list):
        val = analyzed_seq.protein_scale(window=wd, param_dict=param_dict)
        xval, xcolors = [], []
        for i in range(0, len(val)):
            xcolors.append(colorpallete[seq[i]])
            xval.append(f'{seq[i]}{i}')
        graph_points[graph] = {'type': 'line plot', 'x': xval, 'y': val, 'c': xcolors}
    return graph_points


def get_transfer_energy(seq):
    """
    :param seq:
    :return: a dict representing the coordinate of data points on the free energy of transfer from lipid phase to water graph.
        Dict{
            x: [..., ..., ..., ...]
            y: [..., ..., ..., ...]
            c: [..., ..., ..., ...] # color of axis X characters
        }
    """
    wd = 5
    analyzed_seq = ProteinAnalysis(str(seq))
    val = analyzed_seq.protein_scale(window=wd, param_dict=scales['ez'])
    xval, xcolors = [], []

    for i in range(0, len(val)):
        s = seq[i]
        c = colorpallete[s]
        xcolors.append(c)
        s = f'{s}{i}'
        xval.append(s)

    out = {'x': xval, 'y': val, 'c': xcolors}

    return out


def get_hydrophobicity_parker(seq):
    """
    :param seq:
    :return: a dict representing the coordinate of data points on the hydrophobicity_parker graph.
        Dict{
            x: [..., ..., ..., ...]
            y: [..., ..., ..., ...]
            c: [..., ..., ..., ...] # color of axis X characters
        }
    """
    wd = 5
    analyzed_seq = ProteinAnalysis(str(seq))
    val = analyzed_seq.protein_scale(window=wd, param_dict=scales['Parker'])
    xval, xcolors = [], []

    for i in range(0, len(val)):
        s = seq[i]
        c = colorpallete[s]
        xcolors.append(c)
        s = f'{s}{i}'
        xval.append(s)

    out = {'x': xval, 'y': val, 'c': xcolors}

    return out


def get_surface_accessibility(seq):
    """
    :param seq:
    :return: a dict representing the coordinate of data points on the surface_accessibility graph.
        Dict{
            x: [..., ..., ..., ...]
            y: [..., ..., ..., ...]
            c: [..., ..., ..., ...] # color of axis X characters
        }
    """
    wd = 5
    analyzed_seq = ProteinAnalysis(str(seq))
    val = analyzed_seq.protein_scale(window=wd, param_dict=ProtParamData.em)
    xval, xcolors = [], []

    for i in range(0, len(val)):
        s = seq[i]
        c = colorpallete[s]
        xcolors.append(c)
        s = f'{s}{i}'
        xval.append(s)

    out = {'x': xval, 'y': val, 'c': xcolors}

    return out


def get_flexibility(seq):
    """
    :param seq:
    :return: a dict representing the coordinate of data points on the flexibility graph.
        Dict{
            x: [..., ..., ..., ...]
            y: [..., ..., ..., ...]
            c: [..., ..., ..., ...] # color of axis X characters
        }
    """
    wd = 5
    analyzed_seq = ProteinAnalysis(str(seq))
    val = analyzed_seq.protein_scale(window=wd, param_dict=ProtParamData.Flex)
    xval, xcolors = [], []

    for i in range(0, len(val)):
        s = seq[i]
        c = colorpallete[s]
        xcolors.append(c)
        s = f'{s}{i}'
        xval.append(s)

    out = {'x': xval, 'y': val, 'c': xcolors}

    return out


def get_fam_downloads(accession):
    # TODO change prefix here for easier maintenance.
    prefix = pathlib.Path('http://119.3.63.164:443/v1/families/' + accession + '/downloads/')
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


def fam_download_file(accession: str, file: str):
    file = pathlib.Path(cfg['family_data_dir']).joinpath(accession).joinpath(file)
    return file


def get_downloads():
    pass


def download(file: str):
    # print(file)
    # print(pathlib.Path(file).exists())
    return file


def mmseqs_search(seq: str):
    query_id = str(uuid.uuid4())
    query_time_now = datetime.now()
    tmp_dir = pathlib.Path(cfg['tmp_dir'])
    input_seq_file = tmp_dir.joinpath(query_id + '.input')
    output_file = tmp_dir.joinpath(query_id + '.output')

    if not tmp_dir.exists():
        tmp_dir.mkdir(parents=True)
    with open(input_seq_file, 'w') as f:
        f.write(f'>submitted_sequence\n{seq}')

    command_base = 'mmseqs createdb {query_seq} {query_seq}.mmseqsdb && ' \
                   'mmseqs search {query_seq}.mmseqsdb  {database} {out}.mmseqsdb {tmp_dir} && ' \
                   'mmseqs convertalis {query_seq}.mmseqsdb {database} {out}.mmseqsdb {out}'
    command = command_base.format_map({
        'query_seq': input_seq_file,
        'database': cfg['mmseqs_database_file'],
        'out': output_file,
        'tmp_dir': str(tmp_dir)
    })
    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL) ## FIXME
    except subprocess.CalledProcessError as e:
        print('error when executing the command (code {})'.format(e))
        print(e.output)
        return None
    else:
        columns = ['query_identifier', 'target_identifier', 'sequence_identity', 'alignment_length',
                   'number_mismatches', 'number_gap_openings', 'domain_start_position_query',
                   'domain_end_position_query', 'domain_start_position_target',
                   'domain_end_position_target', 'E_value', 'bit_score']
        try:
            df = pd.read_table(output_file, sep='\t', header=None)
        except pd.errors.EmptyDataError:
            df = pd.DataFrame(columns=columns)
        df.columns = columns
        records = df.to_dict(orient='records')
        # pprint(records)
        return records


def hmmscan_search(seq: str):
    query_id = str(uuid.uuid4())
    query_time_now = datetime.now()
    tmp_dir = pathlib.Path(cfg['tmp_dir'])
    input_seq_file = tmp_dir.joinpath(query_id + '.input')
    output_file = tmp_dir.joinpath(query_id + '.output')

    if not tmp_dir.exists():
        tmp_dir.mkdir(parents=True)
    with open(input_seq_file, 'w') as f:
        f.write(f'>submitted_sequence\n{seq}')

    command_base = 'hmmscan --domtblout {out} {hmm_profiles} {query_seq}'
    command = command_base.format_map({
        'out': output_file,
        'hmm_profiles': cfg['hmm_profile_file'],
        'query_seq': input_seq_file,
        # 'out_tmp': tmp_dir.joinpath(query_id + '.tmp')
    })
    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL) ## FIXME
    except subprocess.CalledProcessError as e:
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


def obj_to_dict(obj):
    return {key: value for key, value in obj.__dict__.items() if key != '_sa_instance'}


def round_3(num: float):
    return round(num, 3)


def df_to_formatted_json(df, sep="."):
    """
    The opposite of json_normalize
    """
    result = []
    for idx, row in df.iterrows():
        parsed_row = {}
        for col_label, v in row.items():
            keys = col_label.split(".")

            current = parsed_row
            for i, k in enumerate(keys):
                if i == len(keys) - 1:
                    current[k] = v
                else:
                    if k not in current.keys():
                        current[k] = {}
                    current = current[k]
        # save
        result.append(parsed_row)
    print(result)
    return result


def get_sunburst_data(paths_values, sep: str = None) -> dict:
    """
    :param paths_values:
    :param sep: each path is a list if sep = None.
    :return:
    """
    paths_values.columns = ['path', 'value']
    paths = paths_values['path']

    if sep:
        paths = paths.str.strip(sep).str.split(sep)
    else:
        sep = ';'

    # paths to set up the prefix tree
    # pprint('before prefix')
    # pprint(paths.tolist())
    paths = paths.apply(lambda x: ['Unknown' if i == '' else i for i in x])
    paths = paths.apply(lambda x: [sep.join(x[0:i]) for i in range(1, len(x) + 1)])
    # pprint('after prefix')
    # pprint(paths.tolist())
    identifiers = paths.apply(lambda x: x[-1])
    tree = lt.SuperTree()
    tree.create_node(identifier='')
    tree.from_paths(paths)
    tree.init_nodes_data(0)
    values = dict(zip(identifiers, paths_values['value'].tolist()))
    # print(values)
    tree.fill_with(values)
    tree.update_values()
    # print(vars(tree.get_node('a')))
    def rm_prefix(identifier): return identifier.split(sep)[-1]
    id_parent_value = list(zip(*[(rm_prefix(nid), rm_prefix(tree.parent(nid).identifier), tree.get_node(nid).data)
                                 for nid in tree.expand_tree(mode=tree.WIDTH) if nid != '']))
    return dict(zip(['labels', 'parents', 'values'], id_parent_value))


def compute_distribution_from_query_data(query_data):
    if len(query_data) > 0:
        metadata = pd.DataFrame([obj.__dict__ for obj in query_data]).drop(columns='_sa_instance_state')
        # print(metadata)
        color_map = {}  # TODO supply here
        metadata['latitude'] = metadata['latitude'].replace('', None).astype(float).round(1)
        metadata['longitude'] = metadata['longitude'].replace('', None).astype(float).round(1)
        metadata['habitat_type'] = pd.Categorical(metadata['microontology'].apply(lambda x: x.split(':')[0]))
        # metadata['color'] = metadata['habitat_type'].map(color_map)
        data = dict(
            geo=metadata[['AMPSphere_code', 'latitude', 'longitude', 'habitat_type']].
                groupby(['latitude', 'longitude', 'habitat_type'], as_index=False, observed=True).size(),
            host=metadata[['AMPSphere_code', 'host_tax_id', 'host_scientific_name']].
                groupby('host_tax_id', as_index=False).size(),
            habitat=metadata[['AMPSphere_code', 'microontology', 'habitat_type']].
                groupby(['microontology', 'habitat_type'], as_index=False).size(),
            origin=metadata[['AMPSphere_code', 'origin_tax_id', 'origin_scientific_name']].
                groupby('origin_tax_id', as_index=False).size()
        )

        # FIXME fix color map for geo plot
        # print('Processing geo data...')
        names = {'latitude': 'lat', 'longitude': 'lon', 'AMPSphere_code': 'size'}
        data['geo'].rename(columns=names, inplace=True)
        data['geo'] = data['geo'].to_dict(orient='list')
        # print(data['geo'])
        # FIXME hierarchical structure generation.
        data['habitat'] = data['habitat'][data['habitat'].microontology != '']
        # pprint(data['habitat'])
        data['habitat'] = get_sunburst_data(data['habitat'][['microontology', 'size']], sep=':')
        # Fix id inconsistency.
        data['host'] = data['host'][data['host'].host_tax_id != '']
        data['host']['host_tax_id'] = data['host']['host_tax_id'].apply(lambda x: x if x != 2116673.0 else 85678.0)
        data['host']['host_lineage'] = lt.LineageTracker(ids=data['host']['host_tax_id'].astype(int)).paths_sp
        data['host'] = get_sunburst_data(data['host'][['host_lineage', 'size']], sep=None)
        data['origin'] = None
        return data
    else:
        empty_sunburst = dict(
            labels=[''],
            parents=[''],
            values=[0.0]
        )
        empty_bubblemap = dict(
            lat=[0.0],
            lon=[0.0],
            size=[0.0]
        )
        return dict(
            host=empty_sunburst,
            habitat=empty_sunburst,
            geo=empty_bubblemap
        )

# paths_values = pd.DataFrame({'path': ['a:b', 'a:c', 'a:d'], 'value': [1, 2, 3]})
# print(get_sunburst_data(paths_values, sep=':'))
