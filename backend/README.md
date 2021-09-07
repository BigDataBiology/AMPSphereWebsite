## Components and description
```text
.
├── README.md               # This file
├── __init__.py             
├── crud.py                 # Define database-related functions here: including Create, Read, Update, and Delete
├── database.py             # Generate a database session and a base class (used to define models of the database) here
├── main.py                 # Mount functions to URLs here
├── models.py               # Define models (classes) of the database
└── schemas.py              # Define basic classes to return by the backend
```

## To install the requirements
```shell
pip install -r requirements.txt
```

## To run the service in DEV mode
```shell
uvicorn main:app --reload
```

## To test the backend API
```shell
python -m pytest tests/testing.py
```

## To generate coverage report (html)
```shell
python -m pytest --cov-report html:tests/coverage_html --cov=src tests/testing.py
```

## To host the coverage report using http.server
```shell
python -m http.server --directory tests/coverage_html/ 8000
```

## To browse the coverage report hosted on the HuaWeiCloud server

See [here]()