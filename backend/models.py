from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from database import Base


class AMP(Base):
    """

    """
    __tablename__ = "AMP"
    accession = Column(String, primary_key=True, index=True)
    sequence = Column(String)
    family = Column(String, index=True)
    helical_wheel_path = Column(String)


class GMSC(Base):
    """

    """
    __tablename__ = "GMSC"
    accession = Column(String, primary_key=True, index=True)
    AMP = Column(String, ForeignKey(AMP.accession), index=True)
    sequence = Column(String)


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



