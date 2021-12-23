## Database maintenance 

This folder lists all the necessary scripts for construct/update the database.
```text
.
├── AMPSphere_v.2021-03.sqlite
├── README.md
├── generate_tables.py           # Python script to generate necessary tables
└── import.sql                   # SQL script to import the tables 
```

## To update

1. generate tables. You also have to include these input files in current directory. 

```shell
python scripts/generate_tables.py --metadata original_data/gmsc_amp_genes_envohr_source.tsv --faa original_data/AMPSphere_v.2021-03.faa --fna original_data/AMPSphere_v.2021-03.fna --features original_data/features_plot_ampsphere.tsv tables
```

2. Import the tables into the sqlite3 database.

```shell
sqlite3 ampsphere_main_db/AMPSphere_v.2021-03.sqlite < scripts/import.sql
```

All the scripts have been tested on Linux platform.

## TODO

- [ ] Generate the tables using input files from the zenodo repository.

## Contact

- For anything related with using the scripts, please contact Hui Chong (huichong.me@gmail.com).
