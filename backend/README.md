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
