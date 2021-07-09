from typing import List, Text

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from . import models, crud, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# to be updated

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


'''
def read_hosts(skip: int = 0, taxon_id: int = None, page_size: int = 100, db: Session = Depends(get_db)):
    if taxon_id:
        hosts = crud.get_hosts(db, taxon_id=taxon_id)
    else:
        hosts = crud.get_hosts(db, skip=skip, page_size=page_size)
    return hosts
'''

@app.get("/hosts/", response_model=List[schemas.Host])
def read_hosts(skip: int = 0, page_size: int = 100, db: Session = Depends(get_db)):
    hosts = crud.get_hosts(db, skip=skip, page_size=page_size)
    return hosts


@app.get("/example-host/", response_model=Text)
def example_hosts(skip: int = 0, taxon_id: int = None, page_size: int = 100, db: Session = Depends(get_db)):
    return "this is an example host"