from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

'''
class AMP(Base):
    __tablename__ = "AMP"

    accession = Column(String, primary_key=True, index=True)
    consensus_sequence = Column(String)
    species = Column(Integer)
    hosts = Column(Integer)
    environments = Column(String)
    alignment = Column(String)
    phylogeny_tree = Column(String)
'''

class Hosts(Base):
    __tablename__ = "Hosts"

    taxon_id = Column(Integer, primary_key=True, index=True)
    #related_amp = relationship("AMP", back_populates="hosts")
    common_name = Column(String)
    sci_name = Column(String, index=True)
    counts = Column(Integer)

'''
class Species(Base):
    __tablename__ = "Species"

    taxon_id = Column(Integer, primary_key=True, index=True)
    related_amp = relationship("AMP", back_populates="hosts")
    common_name = Column(String)
    sci_name = Column(String, index=True)
    counts = Column(Integer)
'''

# class Env(Base):

# class


