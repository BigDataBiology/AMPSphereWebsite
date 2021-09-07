# AMPSphereBackend

This repository contains source code for the backend of AMPSphere website.

## Components and description

```txt
├── config/*                # Define default configuration of the backend here.
├── conftest.py             # This file only exists for unittest. 
├── database/*              # AMPSphere database and sequence search databases. 
├── description.md          # Markdown content to be displayed on the Swagger API page.
├── __init__.py   
├── README.md  
├── requirements.txt
├── setup.cfg
├── src
│   ├── crud.py             # Define database-related functions here: including Create, Read, Update, and Delete
│   ├── database.py         # Generate a database session and a base class (used to define models of the database) here
│   ├── __init__.py         
│   ├── main.py             # Main FastAPI application.
│   ├── models.py           # Define models (classes) of the database
│   ├── __pycache__
│   ├── router.py           # Mount functions to URLs here
│   ├── schemas.py          # Define basic classes to return by the backend
│   └── utils.py            # Define database-unrelated functions here.
├── taxdump.tar.gz
└── tests
    ├── coverage_html       # Coverage report (HTML).
    ├── __init__.py         
    ├── inputs.tsv          # Define test cases and expected http response code here.
    ├── __pycache__
    └── testing.py          # Main testing script.
```

## Instructions

- To install the requirements

```shell
pip install -r requirements.txt
```

- To run the service in DEV mode
```shell
uvicorn main:app --reload
```

- To test the backend API
```shell
python -m pytest tests/testing.py
```

- To generate coverage report (html)
```shell
python -m pytest --cov-report html:tests/coverage_html --cov=src tests/testing.py
```

- To host the coverage report using http.server
```shell
python -m http.server --directory tests/coverage_html/ 8000
```

- To browse the coverage report hosted on the HuaWeiCloud server

See [http://119.3.63.164:8000/](http://119.3.63.164:8000/)

## Contact

- Hui Chong (huichong.me@gmail.com), Big Data Biology Lab.