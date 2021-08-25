from typing import List, Optional, Dict
from pydantic import BaseModel


# Define JSON objects to be returned to frontend here.

# Object for AMP_card page ------------------------------------------------
class AMP(BaseModel):
    accession: str
    sequence: str
    family: str
    helical_wheel_path: str

    class Config:
        orm_mode = True


class LinePlotData(BaseModel):
    x: List[str]
    y: List[float]
    c: List[str] = ['not provided']


class SunburstPlotData(BaseModel):
    labels: List[str]
    parents: List[str]
    values: List[float]
    colorway: List[str]


class BubbleMapData(BaseModel):
    latitudes: List[float]
    longitudes: List[float]
    sizes: List[float]
    colors: List[str]


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
