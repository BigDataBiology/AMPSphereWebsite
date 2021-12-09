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
    length = Column(Integer, index=True)
    molecular_weight = Column(Float, index=True)
    isoelectric_point = Column(Float, index=True)
    charge = Column(Float, index=True)
    aromaticity = Column(Float)
    instability_index = Column(Float)
    gravy = Column(Float)


class Quality(Base):
    """

    """
    __tablename__ = "Quality"
    AMP = Column(String, primary_key=True, index=True)
    Antifam = Column(String)
    RNAcode = Column(String)
    metaproteomes = Column(String)
    coordinates = Column(String)
    score = Column(Float)
    badge = Column(String, index=True)


class GMSC(Base):
    """

    """
    __tablename__ = "GMSC"
    accession = Column(String, primary_key=True, index=True)
    gene_sequence = Column(String)
    AMP = Column(String, ForeignKey(AMP.accession), index=True)


class Metadata(Base):
    """
    gmsc	amp	sample	source	specI	is_metagenomic	geographic_location	latitude	longitude	general envo name	environment_material
    """
    __tablename__ = "Metadata"
    GMSC = Column(String, primary_key=True, index=True)
    AMPSphere_code = Column(String, ForeignKey(AMP.accession), index=True)
    sample = Column(String, index=True)
    microbial_source = Column(String, index=True)
    specI = Column(String, index=True)
    is_metagenomic = Column(Boolean, index=True)
    geographic_location = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    general_envo_name = Column(String, index=True)
    environment_material = Column(String)


class Statistics(Base):
    """

    """
    __tablename__ = "Statistics"
    gmsc = Column(Integer, primary_key=True)
    amp = Column(Integer)
    sample = Column(Integer)
    source = Column(Integer)
    specI = Column(Integer)
    is_metagenomic = Column(Integer)
    geographic_location = Column(Integer)
    latitude = Column(Integer)
    longitude = Column(Integer)
    general_envo_name = Column(Integer)
    environment_material = Column(Integer)
    family = Column(Integer)
