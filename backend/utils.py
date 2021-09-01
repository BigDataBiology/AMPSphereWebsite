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


def parse_config():
    parser = configparser.ConfigParser()
    parser.read('config.ini')
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
        subprocess.run(command, shell=True, check=True)
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
        pprint(records)
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
        subprocess.run(command, shell=True, check=True)
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
        print(df)
        records = df.to_dict(orient='records')
        pprint(records)
        return records


# --- deprecated
# with pyhmmer.plan7.HMMFile('./database/hmmsearch_model/AMPSphere_v2021-03.hmm') as hmms:
#     alphabet = pyhmmer.easel.Alphabet.amino()
#     background = pyhmmer.plan7.Background(alphabet)
#     pipeline = pyhmmer.plan7.Pipeline(alphabet, background=background)
#     with pyhmmer.easel.SequenceFile("/root/AMPSphere/tmp/343598dd-f03a-4555-b0e5-9fe68eed7ae5.input") as seq_file:
#         seq_file.set_digital(alphabet)
#         hits = pipeline.search_hmm(query=hmms, sequences=seq_file)
#
# with pyhmmer.plan7.HMMFile('./database/hmmsearch_model/AMPSphere_v2021-03.hmm') as hmms:
#     alphabet = pyhmmer.easel.Alphabet.amino()
#     with pyhmmer.easel.SequenceFile("/root/AMPSphere/tmp/343598dd-f03a-4555-b0e5-9fe68eed7ae5.input") as seq_file:
#         seq_file.set_digital(alphabet)
#         all_hits = list(pyhmmer.hmmsearch(hmms, list(seq_file), cpus=1))


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
        for col_label,v in row.items():
            keys = col_label.split(".")

            current = parsed_row
            for i, k in enumerate(keys):
                if i==len(keys)-1:
                    current[k] = v
                else:
                    if k not in current.keys():
                        current[k] = {}
                    current = current[k]
        # save
        result.append(parsed_row)
    return result