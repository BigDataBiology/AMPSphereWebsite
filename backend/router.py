from sqlalchemy.orm import Session
from database import SessionLocal
from typing import List
from fastapi import Depends
from fastapi.responses import RedirectResponse
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


# Change here.
default_route_summary = ' '
version = '/v1'

amp_router = APIRouter(
    prefix=version + "/amps",
    tags=['amp']
)


# TODO define consistent schema for AMP object.
@amp_router.get(path="",
                response_model=List[schemas.AMP],
                summary=default_route_summary)
def amps(db: Session = Depends(get_db),
         family: str = None,
         habitat: str = None,
         host: str = None,
         sample: str = None,
         origin: str = None,
         page_size: int = 20,
         page: int = 0):
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
        family=family, habitat=habitat, host=host, origin=origin, sample=sample
    )


@amp_router.get(path="/{accession}",
                response_model=schemas.AMP,
                summary=default_route_summary)
def amp(accession: str,
        db: Session = Depends(get_db)):
    """
    **tested**.

    - :param accession:
    - :param db:
    - :return:
    """
    return crud.get_amp(accession, db)


@amp_router.get("/{accession}/features",
                response_model=schemas.AMPFeatures,
                summary=default_route_summary)
def amp_features(accession: str,
                 db: Session = Depends(get_db)):
    """
    **tested**.

    - :param seq:
    - :return:
    """
    # TODO get sequence here.
    return crud.get_amp_features(accession, db)


@amp_router.get("/{accession}/distributions",
                response_model=schemas.Distributions,
                summary=default_route_summary)
def distributions(accession: str,
                  db: Session = Depends(get_db)):
    """
    TODO: implement me, medium PRIORITY

    - :param accession:
    - :return:
    """
    return crud.get_distributions(accession=accession, db=db)


@amp_router.get("/{accession}/metadata",
                response_model=List[schemas.AMPMetadata],
                summary=default_route_summary)
def metadata(accession: str,
             db: Session = Depends(get_db),
             page: int = 0,
             page_size: int = 20):
    """
    **tested**.

    - :param accession:
    - :return:
    """
    return crud.get_amp_metadata(accession=accession, db=db, page=page, page_size=page_size)


family_router = APIRouter(
    prefix=version + '/families',
    tags=['family']
)


@family_router.get(path="",
                   response_model=List[schemas.Family],
                   summary=default_route_summary)
def families(db: Session = Depends(get_db)):
    """
    TODO: implement me, medium PRIORITY

    - :param db:
    - :return:
    """
    families = crud.get_families(db, skip=skip, page_size=page_size)
    return families


@family_router.get(path="/{accession}",
                   response_model=schemas.Family,
                   summary=default_route_summary)
def families(accession, db: Session = Depends(get_db)):
    """
    TODO: implement me, medium PRIORITY

    - :param accession:
    - :param db:
    - :return:
    """
    families = crud.get_family(accession, db)
    return families


@family_router.get(path="/{accession}/features",
                   response_model=schemas.FamilyFeatures,
                   summary=default_route_summary)
def fam_features(accession):
    """
    TODO: implement me, medium PRIORITY

    - :param seq:
    - :return:
    """
    # TODO get sequence here.
    return utils.get_features(accession)


@family_router.get(path="/{accession}/distributions",
                   response_model=schemas.Distributions,
                   summary=default_route_summary)
def fam_distributions(accession: str, db: Session = Depends(get_db)):
    """
    TODO: implement me, low PRIORITY

    - :param accession:
    - :return:
    """
    return crud.get_distributions(accession=accession, db=db)


@family_router.get("/{accession}/downloads",
                   response_model=schemas.FamilyDownloads,
                   summary=default_route_summary)
def fam_downloads(accession: str, db: Session = Depends(get_db)):
    """
    **TODO test me**.
    TODO: implement me, medium PRIORITY
    - :param accession:
    - :return:
    """
    return crud.get_fam_downloads(accession=accession, db=db)


default_router = APIRouter(
    prefix=version + '',
    tags=['default']
)


@default_router.get("/downloads",
                    response_model=List[schemas.Download],
                    summary=default_route_summary)
def read_downloads(db: Session = Depends(get_db)):
    """
    TODO **test this**.
    TODO: implement me, low PRIORITY
    - :param db:
    - :return:
    """
    downloads = crud.get_downloads(db)
    return downloads


@default_router.get("/search/text",
                    response_model=schemas.SearchResults,
                    summary=default_route_summary)
def text_search(query: str):
    """
    TODO: implement me, high PRIORITY
    - :param query:
    - :return:
    """
    return crud.search_by_text(query)


@default_router.get("/search/sequence",
                    response_model=List[schemas.SearchResults],
                    summary=default_route_summary)
def sequence_search(query: str, method: str):
    """
    TODO: implement me, high PRIORITY
    - :param query:
    - :param method:
    - :return:
    """
    return utils.search_by_sequence(query, method=method)


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
