from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from src.database import Base


class AMP(Base):
    """

    """
    __tablename__ = "AMP"
    accession = Column(String, primary_key=True, index=True)
    sequence = Column(String)
    family = Column(String, index=True)


class GMSC(Base):
    """

    """
    __tablename__ = "GMSC"
    accession = Column(String, primary_key=True, index=True)
    gene_sequence = Column(String)
    AMP = Column(String, ForeignKey(AMP.accession), index=True)



class Metadata(Base):
    """

    """
    __tablename__ = "Metadata"
    GMSC = Column(String, primary_key=True, index=True)
    AMPSphere_code = Column(String, ForeignKey(AMP.accession), index=True)
    sample = Column(String, index=True)
    microontology = Column(String, index=True)
    environmental_features = Column(String)
    host_tax_id = Column(Integer)
    host_scientific_name = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    origin_tax_id = Column(Integer)
    origin_scientific_name = Column(String, index=True)


class Statistics(Base):
    """

    """
    __tablename__ = "Statistics"
    GMSC = Column(Integer, primary_key=True)
    sample = Column(Integer)
    microontology = Column(Integer)
    environmental_features = Column(Integer)
    host_scientific_name = Column(Integer)
    origin_scientific_name = Column(Integer)
    accession = Column(Integer)
    family = Column(Integer)
