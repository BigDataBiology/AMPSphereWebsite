from typing import List, Optional, Dict
from pydantic import BaseModel, validator


# Define JSON objects to be returned to frontend here.

# Plot objects ------------------------------------------------------
class LinePlotData(BaseModel):
    type: str
    x: List[str]
    y: List[float]
    c: List[str]

    class Config:
        orm_mode = True


class FeatureGraphPoints(BaseModel):
    transfer_energy: LinePlotData
    hydrophobicity_parker: LinePlotData
    surface_accessibility: LinePlotData
    flexibility: LinePlotData


class SunburstPlotData(BaseModel):
    type: str = 'sunburst plot'
    labels: List[str]
    parents: List[str]
    values: List[float]
    colorway: List[str]

    class Config:
        orm_mode = True


class BubbleMapData(BaseModel):
    type: str = 'bubble map'
    lat: List[float]
    lon: List[float]
    sizes: List[float]
    colors: List[str]

    class Config:
        orm_mode = True


class Distributions(BaseModel):
    geo: BubbleMapData
    habitat: SunburstPlotData
    host: SunburstPlotData
    origin: SunburstPlotData


# Object for AMP_card page ------------------------------------------------
class Features(BaseModel):
    MW: float
    Length: float
    Molar_extinction: List[float]
    Aromaticity: float
    GRAVY: float
    Instability_index: float
    Isoelectric_point: float
    Charge_at_pH_7: float
    Secondary_structure: List[float]
    graph_points: Optional[FeatureGraphPoints]

    class Config:
        orm_mode = True


class AMP(BaseModel):
    accession: str
    sequence: str
    family: str
    helical_wheel_path: str
    features: Optional[Features]

    class Config:
        orm_mode = True


class AMPMetadata(BaseModel):
    accession: str
    sequence: str
    family: str
    GMSC: str
    sample: str
    microontology: str
    environmental_features: str
    host_tax_id: Optional[int]
    host_scientific_name: str
    latitude: Optional[float]
    longitude: Optional[float]
    origin_tax_id: Optional[int]
    origin_scientific_name: Optional[str]

    @validator('origin_tax_id', pre=True)
    def origin_tax_id_blank_string(value, field):
        return None if value == "" else value

    @validator('origin_scientific_name', pre=True)
    def origin_name_blank_string(value, field):
        return None if value == "" else value

    @validator('host_tax_id', pre=True)
    def host_tax_id_blank_string(value, field):
        return None if value == "" else value

    @validator('latitude', pre=True)
    def latitude_blank_string(value, field):
        return None if value == "" else value

    @validator('longitude', pre=True)
    def longitude_blank_string(value, field):
        return None if value == "" else value


# Object for Family page ------------------------------------------------
class Family(BaseModel):
    Family_AMP: List[str]
    Family_Environment: List[str]
    Family_Avg_Feature: List[float]
    Family_Std_Feature: List[float]

    class Config:
        orm_mode = True


# Object for Download page ------------------------------------------------
class Download(BaseModel):
    pass

    class Config:
        orm_mode = True


class SearchResults(BaseModel):
    pass

    class Config:
        orm_mode = True
