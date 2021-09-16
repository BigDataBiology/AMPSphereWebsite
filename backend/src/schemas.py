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
    colorway: List[str] = ['']

    class Config:
        orm_mode = True


class BubbleMapData(BaseModel):
    type: str = 'bubble map'
    lat: List[float]
    lon: List[float]
    size: List[float]
    colors: List[str] = ['']

    class Config:
        orm_mode = True


class Distributions(BaseModel):
    geo: BubbleMapData
    habitat: SunburstPlotData
    host: SunburstPlotData
    origin: Optional[SunburstPlotData]


# Object for AMP_card page ------------------------------------------------
class AMPFeatures(BaseModel):
    MW: float
    Length: float
    Molar_extinction: Dict[str, float]
    Aromaticity: float
    GRAVY: float
    Instability_index: float
    Isoelectric_point: float
    Charge_at_pH_7: float
    Secondary_structure: Dict[str, float]
    graph_points: Optional[FeatureGraphPoints]

    class Config:
        orm_mode = True


class Metadata(BaseModel):
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
    gene_sequence: str
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
    # helical_wheel_path: str
    features: AMPFeatures
    metadata: List[Metadata]

    class Config:
        orm_mode = True


# Object for Family page ------------------------------------------------
class FamilyDownloads(BaseModel):
    alignment: str
    sequences: str
    hmm_logo: str
    hmm_profile: str
    sequence_logo: str
    tree_figure: str
    tree_nwk: str

    class Config:
        orm_mode = True


# not used for now.
class FamilyFeatures(BaseModel):
    MW: Dict[str, float]
    Length: Dict[str, float]
    Molar_extinction: Dict[str, Dict[str, float]]
    Aromaticity: Dict[str, float]
    GRAVY: Dict[str, float]
    Instability_index: Dict[str, float]
    Isoelectric_point: Dict[str, float]
    Charge_at_pH_7: Dict[str, float]
    Secondary_structure: Dict[str, Dict[str, float]]

    class Config:
        orm_mode = True


class Family(BaseModel):
    accession: str
    consensus_sequence: str
    num_amps: int
    downloads: FamilyDownloads
    associated_amps: List[str]
    feature_statistics: Dict[str, AMPFeatures]
    distributions: Distributions

    class Config:
        orm_mode = True


# Object for Download page ------------------------------------------------
class Download(BaseModel):
    pass

    class Config:
        orm_mode = True


class mmSeqsSearchResult(BaseModel):
    query_identifier: str
    target_identifier: str
    sequence_identity: float
    alignment_length: int
    number_mismatches: int
    number_gap_openings: int
    domain_start_position_query: int
    domain_end_position_query: int
    domain_start_position_target: int
    domain_end_position_target: int
    E_value: float
    bit_score: int

    class Config:
        orm_mode = True


class HMMERSearchResult(BaseModel):
    query_accession: str
    query_length: int
    query_name: str
    target_accession: str
    target_length: int
    target_name: str
    E_value: float
    acc: float
    bias: float
    c_Evalue: float
    i_Evalue: float
    num_domain: int
    domain_index: int
    score: float
    from_ali: int
    from_env: int
    from_hmm: int
    to_ali: int
    to_env: int
    to_hmm: int
    description_of_target: str

    class Config:
        orm_mode = True


class Statistics(BaseModel):
    num_amps: int
    num_families: int
    num_hosts: int
    num_habitats: int
    num_genomes: int
    num_metagenomes: int
