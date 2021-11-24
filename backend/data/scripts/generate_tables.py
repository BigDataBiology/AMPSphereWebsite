import shutil

import pandas as pd
import argparse
from Bio import SeqIO
import datatable as dt
import pathlib


parser = argparse.ArgumentParser()
parser.add_argument('--metadata', type=str)
parser.add_argument('--faa', type=str)
parser.add_argument('--fna', type=str)
parser.add_argument('--features', type=str)
parser.add_argument('outdir', type=str, default='tables')
args = parser.parse_args()


print('Loading input data...', end=' ')
metadata_file = pathlib.Path(args.metadata)
metadata = dt.fread(args.metadata, sep='\t').to_pandas()
features = dt.fread(args.features, sep='\t').to_pandas()
faa = SeqIO.parse(args.faa, 'fasta')
fna = SeqIO.parse(args.fna, 'fasta')
print('done')


output_dir = pathlib.Path(args.outdir)
if not output_dir.is_dir():
    output_dir.mkdir()


print('Generating tables...', end=' ')
"""
    accession = Column(String, primary_key=True, index=True)
    sequence = Column(String)
    family = Column(String, index=True)
    length = Column(Integer, index=True)
    molecular_weight = Column(Float, index=True)
    isoelectric_point = Column(Float, index=True)
    charge = Column(Float, index=True)
    aromaticity = Column(Float)
    instability_index = Column(Float)
    gravy = Column(Float)
"""
AMP_cols = ['accession', 'sequence', 'family', 'length', 'molecular_weight', 'isoelectric_point', 'charge', 'aromaticity', 'instability_index', 'gravy']
GMSC_cols = ['accession', 'gene_sequence', 'AMP']
AMP_table = pd.DataFrame([[r.id, str(r.seq), r.description.split(' | ')[1]] for r in faa.records], columns=AMP_cols[0:3])
tables = {
    'AMP': pd.merge(AMP_table.drop(columns='family'), features, left_on=['accession'], right_on=['id'])[AMP_cols],
    'GMSC': pd.DataFrame([[r.id, str(r.seq), r.description.split(' ')[1]] for r in fna.records], columns=GMSC_cols),
    'Statistics': pd.DataFrame({**metadata.nunique(dropna=True).to_frame().T.to_dict(),
                                **AMP_table.drop(columns=['sequence', 'accession']).nunique(dropna=True).to_frame().T.to_dict()})
}

# SPHEREs with num_amps < 8 should not be treated as families.
tables['Statistics']['family'] = sum(tables['AMP'].family.value_counts() >= 8)
# cols = "GMSC sample microontology environmental_features host_scientific_name origin_scientific_name accession family "
# tables['Statistics'] = tables['Statistics'][cols.split()]
# for col in cols.split():
#     if col in tables['Metadata'].columns and tables['Metadata'][col].hasnans:
#         tables['Statistics'][col] -= 1
print('done')

shutil.copy(metadata_file, pathlib.Path(output_dir.joinpath('Metadata.tsv')))
for name, table in tables.items():
    outfile = output_dir.joinpath(name + '.tsv')
    print('Writing to {}...'.format(outfile), end=' ')
    table.to_csv(outfile, sep='\t', index=False, header=False)
    print('done')
