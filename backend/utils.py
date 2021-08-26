from Bio.SeqUtils.ProtParam import ProtParamData
from Bio.SeqUtils.ProtParam import ProteinAnalysis

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


def get_features(seq):
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

    print(type(analyzed_seq.isoelectric_point()))
    print(type(analyzed_seq.charge_at_pH(7.0)))
    out = {'Secondary_structure': analyzed_seq.secondary_structure_fraction(),  # helix, turn, sheet
           'Length': analyzed_seq.length,
           'Molar_extinction': analyzed_seq.molar_extinction_coefficient(),
           'Aromaticity': analyzed_seq.aromaticity(),
           'GRAVY': analyzed_seq.gravy(),
           'MW': analyzed_seq.molecular_weight(),
           'Charge_at_pH_7': analyzed_seq.charge_at_pH(7.0),
           'Instability_index': analyzed_seq.instability_index(),
           'Isoelectric_point': analyzed_seq.isoelectric_point()}
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


def get_search_results(seq, search_using):
    """
    :param seq: sequence
    :param search_using: {mmSeqs, HMMsearch}
    :return:
    """
    pass
