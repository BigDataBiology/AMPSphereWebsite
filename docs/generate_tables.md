## Generate AMP table in the database

- Generate faa.tsv - `Python`

```python
from Bio import SeqIO
import pandas as pd
faa = SeqIO.parse('AMPSphere_v.2021-03.faa', 'fasta')
df = pd.DataFrame(
  [{'accession': r.id, 
    'sequence': str(r.seq), 
    'family': r.description.split(' | ')[1], 
    'helical_wheel_path':''} 
   for r in faa]
)
df.to_csv('AMPSphere_v.2021-03.faa.tsv', sep='\t'，index=False)
```

- Import the table data - `sql`

```sql
.mode csv
.sep \t
.import --skip 1 AMPSphere_v.2021-03.faa.tsv AMP
```

- Test - `sql`

```sql
select accession, sequence, family from AMP where accession == 'AMP10.000_000';
```
You should see 
```text
accession      sequence                     family            
-------------  ---------------------------  ------------------
AMP10.000_000  KKVKSIFKKALAMMGENEVKAWGIGIK  SPHERE-III.001_396
```

## Generate Metadata table

- Generate metadata.tsv - `Python`
```python
import pandas as pd
df = pd.read_csv('AMPSphere_metadata.tsv', sep='\t')
df[['GMGC', 'AMPSphere_code', 'sample', 'microontology', 'environmental_features', 'host_tax_id', 
    'host_scientific_name', 'latitude', 'longitude']].to_csv('AMPSphere_metadata.tsv', sep='\t', index=False)
```

- Import the data - `sql`
```sql
.mode csv
.sep \t
.import --skip 1 AMPSphere_metadata.tsv Metadata
```

-Test
```sql
select AMPSphere_code, latitude, longitude from Metadata where AMPSphere_code == 'AMP10.000_000';
```
