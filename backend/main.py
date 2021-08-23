from typing import List

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud
import models
import schemas
import utils
from database import SessionLocal, engine

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


@app.get("/", response_model=str)
def main():
    return "Hello world"


@app.get("/home", response_model=str)
def main():
    return "Hello"


@app.get("/amp/", response_model=schemas.AMP)
def read_amp_list(accession: str, db: Session = Depends(get_db)):
    amp = crud.get_amp(accession, db)
    return amp


@app.get("/amps/", response_model=List[schemas.AMP])
def read_amp_list(db: Session = Depends(get_db)):
    amp_list = crud.get_amp_list(db)
    return amp_list


@app.get("/distribution/geo", response_model=schemas.BubbleMapData)
def compute_geo_distribution(accession):
    data = crud.get_geo_data(accession)
    return utils.get_geo_distribution(data)


@app.get("/distribution/habitat", response_model=schemas.SunburstPlotData)
def compute_distribution_across_habitats(accession):
    data = crud.get_habitat_data(accession)
    return utils.get_distribution_across_habitats(data)


@app.get("/distribution/host", response_model=schemas.SunburstPlotData)
def compute_distribution_across_hosts(accession):
    data = crud.get_hosts_data(accession)
    return utils.get_distribution_across_hosts(data)


@app.get("/distribution/origin", response_model=schemas.SunburstPlotData)
def compute_distribution_across_origins(accession):
    data = crud.get_origins_data(accession)
    return utils.get_distribution_across_origins(data)


@app.get("/features/", response_model=schemas.Features)
def compute_features(seq):
    return utils.get_features(seq)


@app.get("/feature/enzyme-energy/", response_model=schemas.LinePlotData)
def compute_enzyme_energy(seq):
    return utils.get_enzyme_energy(seq)


@app.get("/feature/hydrophobicity_parker/", response_model=schemas.LinePlotData)
def compute_hydrophobicity_parker(seq):
    return utils.get_enzyme_energy(seq)


@app.get("/feature/flexibility/", response_model=schemas.LinePlotData)
def compute_flexibility(seq):
    return utils.get_flexibility(seq)


@app.get("/feature/surface-accessibility/", response_model=schemas.LinePlotData)
def compute_surface_accessibility(seq):
    return utils.get_surface_accessibility(seq)


@app.get("/family/", response_model=schemas.Family)
def read_families(accession, db: Session = Depends(get_db)):
    families = crud.get_family(accession, db)
    return families


@app.get("/families/", response_model=List[schemas.Family])
def read_families(db: Session = Depends(get_db)):
    families = crud.get_families(db, skip=skip, page_size=page_size)
    return families


@app.get("/downloads/", response_model=List[schemas.Download])
def read_downloads(db: Session = Depends(get_db)):
    downloads = crud.get_downloads(db, skip=skip, page_size=page_size)
    return downloads
