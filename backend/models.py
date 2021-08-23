from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from database import Base


class AMP(Base):
    """

    """
    __tablename__ = "AMP"
    accession = Column(String, primary_key=True, index=True)
    sequence = Column(String)
    family = Column(String)
    helical_wheel_path = Column(String)


class Metadata(Base):
    """

    """
    __tablename__ = "Metadata"
    GMSC = Column(String, primary_key=True, index=True)
    AMPSphere_code = Column(String, ForeignKey(AMP.accession))
    sample = Column(String)
    microontology = Column(String)
    environmental_features = Column(String)
    host_tax_id = Column(Integer)
    host_scientific_name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)


class Family(Base):
    """

    """
    __tablename__ = "Family"
    accession = Column(String, primary_key=True, index=True)

