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
class AMPFeatures(BaseModel):
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


class AMPMetadata(BaseModel):
    """
  'AMPSphere_code': 'AMP10.000_000',
  'GMSC': 'GMSC10.SMORF.000_036_899_109',
  '_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7f852d890e50>,
  'environmental_features': 'human-associated habitat [ENVO:00009003]',
  'host_scientific_name': 'Homo sapiens',
  'host_tax_id': 9606,
  'latitude': 23.1271,
  'longitude': 113.2828,
  'microontology': 'host-associated:animal host:digestive tract:intestine',
  'origin_scientific_name': 'Phocaeicola vulgatus',
  'origin_tax_id': 238,
  'sample': 'SAMEA104142074
    """
    # AMPSphere_code: str
    # GMSC: str
    # environmental_features: Optional[str]
    # host_scientific_name: Optional[str]
    # host_tax_id: Optional[int]
    # latitude: Optional[float]
    # longitude: Optional[float]
    # microontology: Optional[str]
    # origin_scientific_name: Optional[str]
    # origin_tax_id: Optional[int]
    # sample: Optional[str]
    AMPSphere_code: str
    GMSC: str
    sample: str
    microontology: str
    environmental_features: str
    host_tax_id: Optional[int]
    host_scientific_name: Optional[str]
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

    @validator('host_scientific_name', pre=True)
    def host_sci_name_blank_string(value, field):
        return None if value == "" else value

    @validator('latitude', pre=True)
    def latitude_blank_string(value, field):
        return None if value == "" else value

    @validator('longitude', pre=True)
    def longitude_blank_string(value, field):
        return None if value == "" else value


class AMP(BaseModel):
    accession: str
    sequence: str
    family: str
    helical_wheel_path: str
    features: AMPFeatures
    metadata: List[AMPMetadata]

    class Config:
        orm_mode = True


# Object for Family page ------------------------------------------------
class FamilyFeatures(BaseModel):
    pass


class FamilyDownloads(BaseModel):
    pass


class Family(BaseModel):
    accession: str
    consensus_sequence: str
    num_amps: int
    features: FamilyFeatures
    downloads: FamilyDownloads

    class Config:
        orm_mode = True


# Object for Download page ------------------------------------------------
class Download(BaseModel):
    pass

    class Config:
        orm_mode = True


class SearchResults(BaseModel):
    target_sequence_id: str
    sequence_identity: float
    alignment_length: int
    number_of_mismatches: int
    number_of_gap_openings: int
    domain_start_index_query: int
    domain_end_index_query: int
    domain_start_index_target: int
    domain_end_index_target: int
    e_value: float
    bit_score: int

    class Config:
        orm_mode = True
