from sqlalchemy.orm import Session
from . import models, schemas
from . import utils


#
def get_hosts(db: Session, skip: int = 0, page_size: int = 100):
    return db.query(models.Hosts).all()


def get_amp_list(db: Session):
    pass


def get_amp(accession: str, db: Session):
    basic_info = schemas.AMP_BasicInfo(**utils.get_basic_info(accession))
    # db.query(models.AMP).filter(models.AMP.AMP_Accession == accession).first()
    metagenomes = utils.get_metagenomes(accession)
    features = schemas.AMP_Feature(**utils.get_features(basic_info.Sequence))
    #features = utils.get_features(basic_info.Sequence)
    prediction = schemas.AMP_Prediction(**utils.get_prediction(basic_info.Sequence))
    countries = schemas.AMP_Country(**utils.get_country(accession))
    envs = schemas.AMP_Environment(**utils.get_envs(accession))
    graphs = utils.get_AMP_graphs(basic_info.Sequence)
    return schemas.AMP(
        AMP_Accession=accession,
        AMP_Family=[basic_info],
        AMP_Metagenome=metagenomes,
        AMP_Feature=[features],
        AMP_Prediction=[prediction],
        AMP_Country=[countries],
        AMP_Environment=[envs],
        AMP_Graphs=graphs
    )


def get_families(db: Session, skip: int = 0, page_size: int = 100):
    pass


def get_envs(db: Session, skip: int = 0, page_size: int = 100):
    pass


def get_downloads(db: Session, skip: int = 0, page_size: int = 100):
    pass

