import pandas as pd
import argparse
from Bio import SeqIO
import datatable as dt
import pathlib


parser = argparse.ArgumentParser()
parser.add_argument('--metadata', type=str)
parser.add_argument('--faa', type=str)
parser.add_argument('--fna', type=str)
parser.add_argument('--origins', type=str)
parser.add_argument('outdir', type=str, default='tables')
args = parser.parse_args()


print('Loading input data...', end=' ')
metadata = dt.fread(args.metadata, sep='\t').to_pandas()
metadata = metadata[['GMSC', 'AMPSphere_code', 'sample', 'microontology', 'environmental_features',
                     'host_tax_id', 'host_scientific_name', 'latitude', 'longitude']]
origins = dt.fread(args.origins, sep='\t').to_pandas()
origins.rename(columns={'AMPsphere code': 'AMPSphere_code', 'GMSC': 'GMSC',
                        'sample': 'sample', 'taxid': 'origin_tax_id',
                        'name': 'origin_scientific_name'},
               inplace=True)
origins = origins[['AMPSphere_code', 'GMSC', 'sample', 'origin_tax_id', 'origin_scientific_name']]
faa = SeqIO.parse(args.faa, 'fasta')
fna = SeqIO.parse(args.fna, 'fasta')
print('done')


output_dir = pathlib.Path(args.outdir)
if not output_dir.is_dir():
    output_dir.mkdir()


print('Generating tables...', end=' ')
AMP_cols = ['accession', 'sequence', 'family']
GMSC_cols = ['accession', 'gene_sequence', 'AMP']
tables = {
    'AMP': pd.DataFrame([[r.id, str(r.seq), r.description.split(' | ')[1]] for r in faa.records],
                        columns=AMP_cols),
    'GMSC': pd.DataFrame([[r.id, str(r.seq), r.description.split(' ')[1]] for r in fna.records],
                         columns=GMSC_cols),
    'Metadata': pd.merge(left=metadata, right=origins, on=['GMSC', 'AMPSphere_code', 'sample'], how='outer')
}
tables['Statistics'] = pd.DataFrame({**tables['Metadata'].nunique(dropna=True).to_frame().T.to_dict(),
                                     **tables['AMP'].nunique(dropna=True).to_frame().T.to_dict()})

# SPHEREs with num_amps < 8 should not be treated as families.
tables['Statistics']['family'] = sum(tables['AMP'].family.value_counts() >= 8)
cols = "GMSC sample microontology environmental_features host_scientific_name origin_scientific_name accession family "
tables['Statistics'] = tables['Statistics'][cols.split()]
# for col in cols.split():
#     if col in tables['Metadata'].columns and tables['Metadata'][col].hasnans:
#         tables['Statistics'][col] -= 1
print('done')


for name, table in tables.items():
    outfile = output_dir.joinpath(name + '.tsv')
    print('Writing to {}...'.format(outfile), end=' ')
    table.to_csv(outfile, sep='\t', index=False)
    print('done')
