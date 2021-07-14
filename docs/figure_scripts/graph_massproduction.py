import os, gzip

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['agg.path.chunksize'] = 10000

cols = ['charge', 'pI',
        'aindex', 'instaindex',
        'boman', 'hydrophobicity',
        'hmoment']

os.mkdir('./graphs_comparison/')

pos = pd.read_table('data/zamps_train.tsv.gz',
                    sep='\t',
                    header='infer')

neg = pd.read_table('data/znamps_train.tsv.gz',
                    sep='\t',
                    header='infer')

ampsf = pd.read_table('data/zfeatures.tsv.gz',
                      sep='\t',
                      header='infer')

for A in ampsf['AMP']:
    for C in cols:
        xo = f'{C}_z'
        xamp = ampsf[ampsf['AMP'] == A]['length']
        yamp = ampsf[ampsf['AMP'] == A]['boman_z']
        plt.scatter(neg.length,
                    neg[xo],
                    color='gray',
                    label='Non-AMPs',
                    s=[5 for x in neg[xo]])
        plt.scatter(pos.length,
                    pos[xo],
                    color='black',
                    label='AMPs',
                    s=[5 for x in pos[xo]])
        plt.plot(xamp,
                 yamp,
                 '*',
                 color='red',
                 label=A,
                 markersize=5)
        plt.legend()
        plt.xlabel('Length in residues')
        plt.ylabel(f'{C} / Z-Score')
        plt.savefig(f'graphs_comparison/{A}_{C}_z.png',
                    dpi=300)
        plt.close()


