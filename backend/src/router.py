from sqlalchemy.orm import Session
from src.database import SessionLocal
from typing import List, Dict
from fastapi import Depends
from fastapi.responses import FileResponse
from src import schemas
from src import utils
from src import crud
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
                response_model=schemas.PagedAMPs,
                summary=default_route_summary)
def amps(db: Session = Depends(get_db),
         family: str = None,
         habitat: str = None,
         sample: str = None,
         microbial_source: str = None,
         pep_length_interval: str = None,
         mw_interval: str = None,
         pI_interval: str = None,
         charge_interval: str = None,
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
    return crud.get_amps(db, page=page, page_size=page_size,
                         family=family, habitat=habitat, microbial_source=microbial_source, sample=sample,
                         pep_length_interval=pep_length_interval, mw_interval=mw_interval,
                         pI_interval=pI_interval, charge_interval=charge_interval)


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


@amp_router.get(path="/{accession}/helicalwheel",
                # response_class=FileResponse,
                summary=default_route_summary)
def amp_helicalwheel(accession: str):
    """

    :param accession:
    :return:
    """
    path = crud.get_amp_helicalwheel(accession)
    print(path)
    return FileResponse(path)


@amp_router.get(path="/{accession}/features",
                response_model=schemas.AMPFeatures,
                summary=default_route_summary)
def amp_features(accession: str = 'AMP10.000_000',
                 db: Session = Depends(get_db)):
    """
    **tested**.

    - :param seq:
    - :return:
    """
    # TODO get sequence here.
    return crud.get_amp_features(accession, db)


@amp_router.get(path="/{accession}/distributions",
                response_model=schemas.Distributions,
                summary=default_route_summary)
def distributions(accession: str = 'AMP10.000_000',
                  db: Session = Depends(get_db)):
    """
    TODO: implement me, medium PRIORITY

    - :param accession:
    - :return:
    """
    return crud.get_distributions(accession=accession, db=db)


@amp_router.get(path="/{accession}/metadata",
                response_model=schemas.PagedMetadata,
                summary=default_route_summary)
def metadata(accession: str = 'AMP10.000_000',
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
                   response_model=schemas.PagedFamilies,
                   summary=default_route_summary)
def families(db: Session = Depends(get_db),
             habitat: str = None,
             sample: str = None,
             microbail_source: str = None,
             page_size: int = 5,
             page: int = 0):
    """
    **tested**

    - :param db:
    - :return:
    """
    families = crud.get_families(
        db, page=page, page_size=page_size,
        habitat=habitat, microbail_source=microbail_source, sample=sample
    )
    return families


@family_router.get(path="/{accession}",
                   response_model=schemas.Family,
                   summary=default_route_summary)
def family(accession: str = 'SPHERE-III.001_396', db: Session = Depends(get_db)):
    """
    **tested**

    FIXME how to get and return features and distribution.
    - :param accession:
    - :param db:
    - :return:
    """
    families = crud.get_family(accession, db)
    return families


@family_router.get(path="/{accession}/features",
                   response_model=Dict[str, schemas.AMPFeatures],
                   summary=default_route_summary)
def fam_features(accession: str = 'SPHERE-III.001_396', db: Session = Depends(get_db)):
    """
    **tested**

    FIXME how to present and effectively get features of an AMP family
    - :param seq:
    - :return:
    """
    # TODO get sequence here.
    return crud.get_fam_features(accession, db=db)


@family_router.get(path="/{accession}/distributions",
                   response_model=schemas.Distributions,
                   summary=default_route_summary)
def fam_distributions(accession: str = 'SPHERE-III.001_396', db: Session = Depends(get_db)):
    """
    **tested**

    - :param accession:
    - :return:
    """
    return crud.get_distributions(accession=accession, db=db)


@family_router.get("/{accession}/downloads",
                   response_model=schemas.FamilyDownloads,
                   summary=default_route_summary)
def fam_downloads(accession: str = 'SPHERE-III.001_396',
                  db: Session = Depends(get_db)):
    """
    **tested**

    - :param accession:
    - :return:
    """
    return crud.get_fam_downloads(accession=accession, db=db)


@family_router.get("/{accession}/downloads/{file}",
                   # response_model=schemas.FamilyDownloads,
                   summary=default_route_summary)
def fam_download_file(accession: str, file: str):
    """
    **tested**

    - :param accession: use SPHERE-III.000_000 for testing
    - :return:
    """
    return FileResponse(utils.fam_download_file(accession=accession, file=file))


default_router = APIRouter(
    prefix=version + '',
    tags=['default']
)


@default_router.get(path="/statistics",
                    response_model=schemas.Statistics,
                    summary=default_route_summary)
def get_statistics(db: Session = Depends(get_db)):
    """

    :param db:
    :return:
    """
    return crud.get_statistics(db)


@default_router.get(path='/available_filters',
                    #response_model=schemas.Filters,
                    summary=default_route_summary
                    )
def get_filters(db: Session = Depends(get_db)):
    """

    :param db:
    :return:
    """
    return crud.get_filters(db)


@default_router.get(path="/downloads",
                    response_model=List[str],
                    summary=default_route_summary)
def get_downloads():
    """
    TODO **test this**.
    TODO: implement me, low PRIORITY
    - :param db:
    - :return:
    """
    downloads = utils.get_downloads()
    return downloads


@default_router.get(path="/downloads/{file}",
                    # response_class=FileResponse,
                    summary=default_route_summary)
async def download_file(file: str):
    """
    TODO **test this**.
    TODO: implement me, low PRIORITY
    """
    return FileResponse(utils.download(file))


@default_router.get(path="/search/text",
                    response_model=schemas.PagedAMPs,
                    summary=default_route_summary)
def text_search(db: Session = Depends(get_db),
                query: str = 'AMP10.000_000',
                page: int = 0,
                page_size: int = 20):
    """
    **tested**

    - :param query:
    - :return:
    """
    return crud.search_by_text(db, text=query, page=page, page_size=page_size)


@default_router.get(path="/search/mmseqs",
                    response_model=List[schemas.mmSeqsSearchResult],
                    summary=default_route_summary)
def mmseqs_search(query: str = 'KKVKSIFKKALAMMGENEVKAWGIGIK'):
    """
    **tested**

    TODO: accelerate me by creating and indexing the db in advance.
    - :param query: sequence
    - :return:
    """
    return utils.mmseqs_search(query)


@default_router.get(path="/search/hmmer",
                    response_model=List[schemas.HMMERSearchResult],
                    summary=default_route_summary)
def hmmscan_search(query: str = 'KKVKSIFKKALAMMGENEVKAWGIGIK'):
    """
    **tested**

    - :param query:
    - :param method:
    - :return:
    """
    return utils.hmmscan_search(query)

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
