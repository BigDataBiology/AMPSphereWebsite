from sqlalchemy.orm import Session
from backend import models, schemas
from backend import utils


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
    prediction = schemas.AMP_Prediction(**utils.get_prediction(basic_info.Sequence))
    countries = schemas.AMP_Country(**utils.get_country(accession))
    envs = schemas.AMP_Environment(**utils.get_envs(accession))
    graphs = utils.get_AMP_graphs(accession)
    return schemas.AMP(
        AMP_Accession=accession,
        AMP_Metagenome=metagenomes,
        AMP_Feature=features,
        AMP_Prediction=prediction,
        AMP_Country=countries,
        AMP_Environment=envs,
        AMP_Graphs=graphs
    )


def get_amps_by_fam(fam_accession):
    pass


def get_families(db: Session, skip: int = 0, page_size: int = 100):
    pass


def get_envs(db: Session, skip: int = 0, page_size: int = 100):
    pass


def get_downloads(db: Session, skip: int = 0, page_size: int = 100):
    pass

