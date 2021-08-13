from typing import List, Text

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from . import models, crud, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url='/api/docs',
              redoc_url='/api/redoc',
              openapi_url='/api/openapi.json')

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
    return None


@app.get("/home")
def main():
    return None


@app.get("/amp/", response_model=schemas.AMP)
def read_amp_list(ampId: str, db: Session = Depends(get_db)):
    amp = crud.get_amp(ampId, db)
    return amp


@app.get("/amps/", response_model=List[schemas.AMP])
def read_amp_list(db: Session = Depends(get_db)):
    amp_list = crud.get_amp_list(db)
    return amp_list


@app.get("/hosts/", response_model=List[schemas.Host])
def read_hosts(skip: int = 0, page_size: int = 100, db: Session = Depends(get_db)):
    hosts = crud.get_hosts(db, skip=skip, page_size=page_size)
    return hosts


@app.get("/families/", response_model=List[schemas.Family])
def read_families(db: Session = Depends(get_db)):
    families = crud.get_families(db, skip=skip, page_size=page_size)
    return families


@app.get("/envs/", response_model=List[schemas.Env])
def read_envs(db: Session = Depends(get_db)):
    envs = crud.get_envs(db, skip=skip, page_size=page_size)
    return envs


@app.get("/downloads/", response_model=List[schemas.Download])
def read_downloads(db: Session = Depends(get_db)):
    downloads = crud.get_downloads(db, skip=skip, page_size=page_size)
    return downloads



