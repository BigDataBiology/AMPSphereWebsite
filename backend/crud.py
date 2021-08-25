from sqlalchemy.orm import Session
import models
import schemas
import utils


#
def get_hosts(db: Session, skip: int, page_size: int):
    return db.query(models.Hosts).all()


def get_amp_list(db: Session, page: int, page_size: int):
    return db.query(models.AMP).offset(page * page_size).limit(page_size).all()


def get_amp(accession: str, db: Session):
    return db.query(models.AMP).filter(models.AMP.accession == accession).first()


def get_families(db: Session, skip: int = 0, page_size: int = 100):
    pass


def get_envs(db: Session, skip: int = 0, page_size: int = 100):
    pass


def get_downloads(db: Session, skip: int = 0, page_size: int = 100):
    pass

