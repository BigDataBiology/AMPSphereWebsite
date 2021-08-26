from sqlalchemy.orm import Session
from database import SessionLocal
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


browse_router = APIRouter(
    prefix="/browse",
)


@browse_router.get("/amp/{accession}", response_model=schemas.AMP)
def amp(accession: str, db: Session = Depends(get_db), include_feature_graph: bool = True):
    """
    **tested**.

    - :param accession:
    - :param db:
    - :return:
    """
    return crud.get_amp(accession, db, include_feature_graph=include_feature_graph)


@browse_router.get("/amps", response_model=List[schemas.AMPMetadata])
def amps(db: Session = Depends(get_db),
         family: str = None, habitat: str = None, host: str = None,
         gene: str = None, sample: str = None, origin: str = None,
         page_size: int = 20, page: int = 0):
    """
    **tested**.

    Get a list of amps.
    - :param page:
    - :param page_size:
    - :param db:
    - :return:
    """
    return crud.get_amp_list(
        db, page=page, page_size=page_size,
        family=family, habitat=habitat, host=host, origin=origin, gene=gene, sample=sample
    )


@browse_router.get("/family/{accession}", response_model=schemas.Family)
def families(accession, db: Session = Depends(get_db)):
    """
    TODO **test this**.

    - :param accession:
    - :param db:
    - :return:
    """
    families = crud.get_family(accession, db)
    return families


@browse_router.get("/families", response_model=List[schemas.Family])
def families(db: Session = Depends(get_db)):
    """
    TODO **test this**.

    - :param db:
    - :return:
    """
    families = crud.get_families(db, skip=skip, page_size=page_size)
    return families


@browse_router.get("/downloads", response_model=List[schemas.Download])
def read_downloads(db: Session = Depends(get_db)):
    """
    TODO **test this**.

    - :param db:
    - :return:
    """
    downloads = crud.get_downloads(db)
    return downloads


compute_router = APIRouter(
    prefix="/compute",
)


@compute_router.get("/features/{seq}", response_model=schemas.Features)
def features(seq):
    """
    **tested**.

    - :param seq:
    - :return:
    """
    return utils.get_features(seq)


@compute_router.get("/distributions/{accession}", response_model=schemas.Distributions)
def distributions(accession, db: Session = Depends(get_db)):
    """
    **tested**.

    - :param accession:
    - :return:
    """
    return crud.get_distributions(accession=accession, db=db)

## --------------------------Deprecated----------------------------------


# @compute_router.get("/feature/enzyme-energy", response_model=schemas.LinePlotData)
# def enzyme_energy(seq):
#     """
#     **tested**.
#
#     - :param seq:
#     - :return:
#     """
#     return utils.get_transfer_energy(seq)
#
#
# @compute_router.get("/feature/hydrophobicity_parker", response_model=schemas.LinePlotData)
# def hydrophobicity_parker(seq):
#     """
#     **tested**.
#
#     - :param seq:
#     - :return:
#     """
#     return utils.get_hydrophobicity_parker(seq)
#
#
# @compute_router.get("/feature/flexibility/", response_model=schemas.LinePlotData)
# def flexibility(seq):
#     """
#     **tested**.
#
#     - :param seq:
#     - :return:
#     """
#     return utils.get_flexibility(seq)
#
#
# @compute_router.get("/feature/surface-accessibility", response_model=schemas.LinePlotData)
# def surface_accessibility(seq):
#     """
#     **tested**.
#
#     - :param seq:
#     - :return:
#     """
#     return utils.get_surface_accessibility(seq)


# @compute_router.get("/distribution/geo", response_model=schemas.BubbleMapData)
# def geo_distribution(accession):
#     """
#     TODO **test this**.
#
#     - :param accession:
#     - :return:
#     """
#     data = crud.get_geo_data(accession)
#     return utils.get_geo_distribution(data)
#
#
# @compute_router.get("/distribution/habitat", response_model=schemas.SunburstPlotData)
# def distribution_across_habitats(accession):
#     """
#     TODO **test this**.
#
#     - :param accession:
#     - :return:
#     """
#     data = crud.get_habitat_data(accession)
#     return utils.get_distribution_across_habitats(data)
#
#
# @compute_router.get("/distribution/host", response_model=schemas.SunburstPlotData)
# def distribution_across_hosts(accession):
#     """
#     TODO **test this**.
#
#     - :param accession:
#     - :return:
#     """
#     data = crud.get_hosts_data(accession)
#     return utils.get_distribution_across_hosts(data)
#
#
# @compute_router.get("/distribution/origin", response_model=schemas.SunburstPlotData)
# def distribution_across_origins(accession):
#     """
#     TODO **test this**.
#
#     - :param accession:
#     - :return:
#     """
#     data = crud.get_origins_data(accession)
#     return utils.get_distribution_across_origins(data)
