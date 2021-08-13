from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class Hosts(Base):
    __tablename__ = "Hosts"

    taxon_id = Column(Integer, primary_key=True, index=True)
    #related_amp = relationship("AMP", back_populates="hosts")
    common_name = Column(String)
    sci_name = Column(String, index=True)
    counts = Column(Integer)

class AMP(Base):
    __tablename__ = "AMP"
    accession = Column(String, primary_key=True, index=True)
    sequence = Column(String)
    family = Column(String)
    pass



