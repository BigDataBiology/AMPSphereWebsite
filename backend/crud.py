from sqlalchemy.orm import Session

from backend import models, schemas


# to be updated
def get_hosts(db: Session, skip: int = 0, page_size: int = 100):
    return db.query(models.Hosts).all()