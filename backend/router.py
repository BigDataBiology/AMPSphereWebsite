from sqlalchemy.orm import Session
from database import SessionLocal
import schemas
from typing import List
from fastapi import Depends
import schemas
import utils
import crud
from fastapi import APIRouter


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get("/amp", response_model=schemas.AMP)
def amp(accession: str, db: Session = Depends(get_db)):
    amp = crud.get_amp(accession, db)
    return amp


@router.get("/amps", response_model=List[schemas.AMP])
def amps(page: int = 0, page_size: int = 20, db: Session = Depends(get_db)):
    """
    Get a list of amps.
    :param page:
    :param page_size:
    :param db:
    :return:
    """
    return crud.get_amp_list(db, page=page, page_size=page_size)


@router.get("/distribution/geo", response_model=schemas.BubbleMapData)
def geo_distribution(accession):
    data = crud.get_geo_data(accession)
    return utils.get_geo_distribution(data)


@router.get("/distribution/habitat", response_model=schemas.SunburstPlotData)
def distribution_across_habitats(accession):
    data = crud.get_habitat_data(accession)
    return utils.get_distribution_across_habitats(data)


@router.get("/distribution/host", response_model=schemas.SunburstPlotData)
def distribution_across_hosts(accession):
    data = crud.get_hosts_data(accession)
    return utils.get_distribution_across_hosts(data)


@router.get("/distribution/origin", response_model=schemas.SunburstPlotData)
def distribution_across_origins(accession):
    data = crud.get_origins_data(accession)
    return utils.get_distribution_across_origins(data)


@router.get("/features", response_model=schemas.Features)
def features(seq):
    return utils.get_features(seq)


@router.get("/feature/enzyme-energy", response_model=schemas.LinePlotData)
def enzyme_energy(seq):
    return utils.get_transfer_energy(seq)


@router.get("/feature/hydrophobicity_parker", response_model=schemas.LinePlotData)
def hydrophobicity_parker(seq):
    return utils.get_hydrophobicity_parker(seq)


@router.get("/feature/flexibility/", response_model=schemas.LinePlotData)
def flexibility(seq):
    return utils.get_flexibility(seq)


@router.get("/feature/surface-accessibility", response_model=schemas.LinePlotData)
def surface_accessibility(seq):
    return utils.get_surface_accessibility(seq)


@router.get("/family/", response_model=schemas.Family)
def families(accession, db: Session = Depends(get_db)):
    families = crud.get_family(accession, db)
    return families


@router.get("/families", response_model=List[schemas.Family])
def families(db: Session = Depends(get_db)):
    families = crud.get_families(db, skip=skip, page_size=page_size)
    return families


@router.get("/downloads", response_model=List[schemas.Download])
def read_downloads(db: Session = Depends(get_db)):
    downloads = crud.get_downloads(db, skip=skip, page_size=page_size)
    return downloads
