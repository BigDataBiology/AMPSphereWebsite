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
python generate_tables.py --metadata AMPSphere_metadata.tsv --fna AMPSphere_v.2021-03.fna --faa AMPSphere_v.2021-03.faa --origins complete_table_origins.tsv tables
```

2. Import the tables into the sqlite3 database.

```shell
sqlite3 AMPSphere_v.2021-03.sqlite < import.sql
```

All the scripts have been tested on Linux platform.

## TODO

- [ ] Generate the tables using input files from the zenodo repository.

## Contact

- For anything related with using the scripts, please contact Hui Chong (huichong.me@gmail.com).
