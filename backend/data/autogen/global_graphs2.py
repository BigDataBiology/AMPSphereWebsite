import sys
import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from Bio import SeqIO
from six import StringIO

from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio.SeqUtils.ProtParam import ProtParamData
from modlamp.plot import helical_wheel

# Protparam scales:
# kd → Kyte & Doolittle Index of Hydrophobicity
# Flex → Normalized average flexibility parameters (B-values)
# hw → Hopp & Wood Index of Hydrophilicity
# em → Emini Surface fractional probability (Surface Accessibility)


aalist = ['A','C', 'D','E',
          'F','G', 'H','I',
          'K','L', 'M','N',
          'P','Q', 'R','S',
          'T','V', 'Y','W']

# Colour scheme in Lesk (Introduction to Bioinformatics)
# Uses 5 groups (note Histidine): 
# Small nonpolar	G, A, S, T                      Orange
# Hydrophobic	        C, V, I, L, P, F, Y, M, W       Green
# Polar                 N, Q, H		                Magenta
# Negatively charged    D, E		                Red
# Positively charged    K, R                            Blue

colorpallete = {'G': 'orange', 'A': 'orange', 'S': 'orange', 'T': 'orange',
                'C': 'g', 'V': 'g', 'I': 'g', 'L': 'g',
                'P': 'g', 'F': 'g', 'Y': 'g', 'M': 'g',
                'W': 'g', 'N': 'm', 'Q': 'm', 'H': 'm',
            	'D': 'r', 'E': 'r', 'K': 'b', 'R': 'b'}

# these hydrophobicity scales are minmax organized
# the higher the value, more hydrophobic the aa is
scales = {'Cowan': {'W': 0.879, 'F': 0.965, 'L': 0.992,
                    'I': 1.0, 'M': 0.817, 'V': 0.872,
                    'Y': 0.46, 'C': 0.731, 'P': 0.751,
                    'A': 0.628, 'H': 0.377, 'R': 0.163,
                    'T': 0.472, 'G': 0.54, 'K': 0.153,
                    'Q': 0.307, 'S': 0.382, 'N': 0.291,
                    'E': 0.05, 'D': 0.0},
          'Kovacs_a': {'W': 1.0, 'F': 0.916, 'L': 0.76,
                       'I': 0.707, 'M': 0.551, 'V': 0.486,
                       'Y': 0.514, 'C': 0.318, 'P': 0.355,
                       'A': 0.174, 'H': 0.19, 'R': 0.174,
                       'T': 0.174, 'G': 0.056, 'K': 0.0,
                       'Q': 0.103, 'S': 0.09, 'N': 0.084,
                       'E': 0.044, 'D': 0.034},
          'Kovacs_b': {'W': 1.0, 'F': 0.931, 'L': 0.792,
                       'I': 0.74, 'M': 0.59, 'V': 0.538,
                       'Y': 0.549, 'C': 0.382, 'P': 0.422,
                       'A': 0.266, 'H': 0.266, 'R': 0.338,
                       'T': 0.243, 'G': 0.182, 'K': 0.266,
                       'Q': 0.182, 'S': 0.171, 'N': 0.165,
                       'E': 0.012, 'D': 0.0},
          'Parker': {'W': 1.0, 'F': 0.96, 'L': 0.96,
                     'M': 0.71, 'V': 0.685, 'Y': 0.595,
                     'C': 0.43, 'P': 0.395, 'A': 0.395,
                     'H': 0.395, 'R': 0.29, 'T': 0.24,
                     'G': 0.215, 'K': 0.215, 'Q': 0.2,
                     'S': 0.175, 'N': 0.15, 'E': 0.11,
                     'D': 0.0, 'I': 0.9},
          'Monerac': {'W': 0.983, 'F': 1.0, 'L': 0.983,
                      'I': 0.99, 'M': 0.833, 'V': 0.843,
                      'Y': 0.76, 'C': 0.67, 'P': 0.173,
                      'A': 0.62, 'H': 0.403, 'R': 0.263,
                      'T': 0.437, 'G': 0.357, 'K': 0.207,
                      'Q': 0.29, 'S': 0.323, 'N': 0.173,
                      'E': 0.157, 'D': 0.0},
          'AVE3': {'W': 1.0, 'F': 0.969, 'L': 0.916, 'I': 0.882,
                   'M': 0.715, 'V': 0.693, 'Y': 0.639, 'C': 0.497,
                   'P': 0.333, 'A': 0.43, 'H': 0.357, 'R': 0.298,
                   'T': 0.309, 'G': 0.248, 'K': 0.225, 'Q': 0.231,
                   'S': 0.224, 'N': 0.163, 'E': 0.093, 'D': 0.0},
          'ez': {'L': -4.92, 'I': -4.92, 'V': -4.04,
                 'F': -2.98, 'M': -2.35, 'W': -2.33,
                 'A': -1.81, 'C': -1.28, 'G': -0.94,
                 'Y': 0.14, 'T': 2.57, 'S': 3.4,
                 'H': 4.66, 'Q': 5.54, 'K': 5.55,
                 'N': 6.64, 'E': 6.81, 'D': 8.72,
                 'R': 14.92, 'P': 0.0}}


data_aa = {'AMP_mean': {'A': 7.520502564098912, 'C': 6.36633345571278,
                        'D': 2.668597822622926, 'E': 2.7141042077216704,
                        'F': 4.391951106649475, 'G': 10.675459550168885,
                        'H': 2.1711336118510483, 'I': 6.347409500480028,
                        'K': 9.861591967792371, 'L': 9.658690725226656,
                        'M': 1.2484935261695338, 'N': 3.7691909197648736,
                        'P': 4.580420590187392, 'Q': 2.4477634910400194,
                        'R': 5.545623161260059, 'S': 6.026451554176794,
                        'T': 4.151896217120581, 'V': 5.789255898915741,
                        'Y': 2.3433663843826027, 'W': 1.7217637446576457},
           'AMP_std': {'A': 6.606149264041305, 'C': 7.243769785740786,
                       'D': 3.653517299310336, 'E': 3.627738452023139,
                       'F': 4.741961828857768, 'G': 7.367561399376693,
                       'H': 3.899314485554839, 'I': 5.552037685411282,
                       'K': 7.372780284577385, 'L': 8.756227525252548,
                       'M': 2.3385964346632746, 'N': 3.752206751253756,
                       'P': 6.03595086307002, 'Q': 3.29147871240816,
                       'R': 6.997662087778225, 'S': 4.907602757156398,
                       'T': 4.314364835800506, 'V': 4.980394942927765,
                       'Y': 3.2792515791237014, 'W': 3.1977236581945347},
           'NAMP_mean': {'A': 8.5622274065478, 'C': 1.4789156615654058,
                         'D': 5.155744906305648, 'E': 6.795230159499449,
                         'F': 3.728852171144205, 'G': 7.14820582792835,
                         'H': 2.1557129065808085, 'I': 6.187847874241366,
                         'K': 7.068499469732919, 'L': 9.3359440472875,
                         'M': 1.9695515485179416, 'N': 3.837576140353241,
                         'P': 4.307095987596791, 'Q': 3.739296528690092,
                         'R': 6.329842863422612, 'S': 5.97177857365507,
                         'T': 5.164575553563543, 'V': 7.339571862896026,
                         'Y': 2.764380580261445, 'W': 0.9591499302097856},
           'NAMP_std': {'A': 4.152347300212898, 'C': 2.41911267211069,
                        'D': 2.516020373325246, 'E': 3.314402093538308,
                        'F': 2.330314168513022, 'G': 3.297362816891616,
                        'H': 1.6512452826231296, 'I': 3.0490889819362645,
                        'K': 4.154914723867973, 'L': 3.6288667599165914,
                        'M': 1.5326492787082528, 'N': 2.279318863869867,
                        'P': 2.668229546280934, 'Q': 2.3496768850990324,
                        'R': 3.941947102442459, 'S': 2.835126542032928,
                        'T': 2.3327615292710866, 'V': 2.951465012361856,
                        'Y': 1.8416000916385065, 'W': 1.2009973185629197}}


data_aa = pd.DataFrame(data_aa)


def profile(header, sequence, out, size=7, wd=5, scale='ez'):
    analyzed_seq = ProteinAnalysis(str(sequence))
    val = analyzed_seq.protein_scale(window=wd, param_dict=scales[scale])
    xval, xcolors = [], []
    for i in range(0, len(val)):
        s = sequence[i]
        c = colorpallete[s]
        xcolors.append(c)
        s = f'{s}{i}'
        xval.append(s)
    plt.plot(xval, val)
    plt.xticks(fontsize=size, rotation=90)
    for i, c in enumerate(xcolors):
        plt.gca().get_xticklabels()[i].set_color(c)
    plt.xlabel('Window start position')
    if scale == 'ez':
        plt.axhline(y=0, color='gray', linestyle='--')
        plt.ylabel('Transfer energy from water\nto lipid bilayer')
        plt.savefig(f'{out}/EZenergy_{header}.png',
                    dpi=300)
    else:
        plt.axhline(y=0.5, color='gray', linestyle='--')
        plt.ylabel(f'Scaled hydrophobicity - Scale {scale}')
        plt.savefig(f'{out}/hydrophobicity_{scale}_{header}.png',
                    dpi=300)
    plt.close()


def sstruc(seq, wd=5):
    analyzed_seq = ProteinAnalysis(str(seq))
    ss = analyzed_seq.secondary_structure_fraction() # helix, turn, sheet
    profexp = analyzed_seq.protein_scale(window=wd, param_dict=ProtParamData.em)
    proflex = analyzed_seq.protein_scale(window=wd, param_dict=ProtParamData.Flex)
    L = analyzed_seq.length
    extinc = analyzed_seq.molar_extinction_coefficient()
    aroma = analyzed_seq.aromaticity()
    gravy = analyzed_seq.gravy()
    MW = analyzed_seq.molecular_weight()              
    charge_at_pH7 = analyzed_seq.charge_at_pH(7.0)
    II = analyzed_seq.instability_index()
    pI = analyzed_seq.isoelectric_point()
    return [ss, profexp, proflex,
            L, extinc, aroma,
            gravy, MW,
            charge_at_pH7,
            II, pI]


def decompose(header, sequence, out):
    l = len(sequence)
    k = 100/l
    seqfreq = []
    for aa in aalist:
        seqfreq.append(sequence.count(aa)*k)
    df = pd.DataFrame()
    df['AMPmu'] = data_aa['AMP_mean']
    df['NAMPmu'] = data_aa['NAMP_mean']
    df['AMPstd'] = data_aa['AMP_std']
    df['NAMPstd'] = data_aa['NAMP_std']
    df[header] = seqfreq
    df['zAMP'] = df[header] - df['AMPmu']
    df['zAMP'] = df['zAMP'] / df['AMPstd']
    df['zNAMP'] = df[header] - df['NAMPmu']
    df['zNAMP'] = df['zNAMP'] / df['NAMPstd']
    df = df.drop(['AMPmu', 'NAMPmu',
                  header, 'AMPstd',
                  'NAMPstd'], axis=1)
    df.plot.bar()
    plt.xlabel('Amino acid')
    plt.ylabel('Z-Score')
    plt.savefig(f'{out}/aa_composition_deviation_{header}.png',
                dpi=300)
    plt.close()


os.mkdir('figures')
os.mkdir('figures/hydrophobicity')
os.mkdir('figures/ez')
os.mkdir('figures/flexibility')
os.mkdir('figures/aa_comp')
os.mkdir('figures/wheel')
os.mkdir('figures/SA')
os.mkdir('figures/reports')

for index, record in enumerate(SeqIO.parse(sys.argv[1],"fasta")):
        out = open(f'figures/reports/{str(record.id)}.txt', 'w')
        print(f'{record.id}')
        complete = sstruc(str(record.seq))
        if 70 < len(record.seq) < 150:
            size = 4
        elif 50 < len(record.seq) <= 70:
            size = 5
        elif 30 < len(record.seq) <= 50:
            size = 6
        elif 0 < len(record.seq) <= 30:
            size = 7
        L = complete[3]
        extinc = complete[4]
        aroma = complete[5]
        gravy = complete[6]
        MW = complete[7]
        charge_at_pH7 = complete[8]
        II = complete[9]
        pI = complete[10]
        ss = complete[0]
        out.write(f'''
        ---------------------------------------------------------
        [PROC] -- {record.id}
        ---------------------------------------------------------
        sequence = {record.seq}
        MW = {(MW/1000):.2f} kDa
        Length = {L}
        Molar extinction = {extinc}
        Aromaticity = {aroma}
        GRAVY = {gravy}
        Instability index = {II}
        Isoeletric point = {pI}
        Charget at pH 7.0 = {charge_at_pH7}
        ---------------------------------------------------------
        Secondary Structure Assessment
        helix: {ss[0]*100}, turn: {ss[1]*100}, sheet: {ss[2]*100}
        ---------------------------------------------------------
        ''')
        out.close()
        profexp = complete[1]
        xval, xcolors = [], []
        for i in range(0, len(profexp)):
            s = str(record.seq)[i]
            c = colorpallete[s]
            xcolors.append(c)
            s = f'{s}{i}'
            xval.append(s)
        plt.plot(xval, profexp)
        plt.xticks(fontsize=size, rotation=90)
        for i, c in enumerate(xcolors):
            plt.gca().get_xticklabels()[i].set_color(c)
        plt.axhline(y=1.0, color='gray', linestyle='--')
        plt.xlabel('Window start position')
        plt.ylabel('Surface accessibility')
        plt.savefig(f'figures/SA/SA_{record.id}.png',
                    dpi=300)
        plt.close()
        proflex = complete[2]
        xval, xcolors = [], []
        for i in range(0, len(proflex)):
            s = str(record.seq)[i]
            c = colorpallete[s]
            xcolors.append(c)
            s = f'{s}{i}'
            xval.append(s)
        plt.plot(xval, proflex)
        plt.xticks(fontsize=size, rotation=90)
        for i, c in enumerate(xcolors):
            plt.gca().get_xticklabels()[i].set_color(c)
        plt.axhline(y=1.0, color='gray', linestyle='--')
        plt.xlabel('Window start position')
        plt.ylabel(f'Flexibility as B-values')
        plt.savefig(f'figures/flexibility/flexibility_{record.id}.png',
                    dpi=300)
        plt.close()
        profile(record.id, record.seq, 'figures/hydrophobicity', size, 5, 'Parker')
        profile(record.id, record.seq, 'figures/ez', size, 5, 'ez')
        decompose(record.id, record.seq, 'figures/aa_comp')
        file_name = f'figures/wheel/helicalwheel_{str(record.id)}.png'
        helical_wheel(str(record.seq),
                      moment=True,
                      colorcoding='amphipathic',
                      lineweights=True,
                      filename=file_name,
                      seq=False)
        plt.close()

