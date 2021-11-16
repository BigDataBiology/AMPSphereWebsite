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
    microbial_source: Optional[SunburstPlotData]


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
    AMPSphere_code: str
    GMSC: str
    gene_sequence: str
    sample: str
    general_envo_name: str
    environment_material: str
    latitude: Optional[float]
    longitude: Optional[float]
    specI: Optional[str]
    microbial_source: Optional[str]

    class Config:
        orm_mode = True

    @validator('specI', pre=True)
    def origin_tax_id_blank_string(value, field):
        return None if value == "" else value

    @validator('microbial_source', pre=True)
    def origin_name_blank_string(value, field):
        return None if value == "" else value

    @validator('latitude', pre=True)
    def latitude_blank_string(value, field):
        return None if value == "" else value

    @validator('longitude', pre=True)
    def longitude_blank_string(value, field):
        return None if value == "" else value


class PageInfo(BaseModel):
    currentPage: int
    pageSize: int
    totalPage: int
    totalItem: int

    class Config:
        orm_mode = True


class PagedMetadata(BaseModel):
    info: PageInfo
    data: List[Metadata]

    class Config:
        orm_mode = True


class AMP(BaseModel):
    accession: str
    sequence: str
    family: str
    length: int
    molecular_weight: float
    isoelectric_point: float
    charge: float
    aromaticity: float
    instability_index: float
    gravy: float
    secondary_structure: Dict[str, float]
    feature_graph_points: Optional[FeatureGraphPoints]
    metadata: PagedMetadata

    class Config:
        orm_mode = True


class PagedAMPs(BaseModel):
    info: PageInfo
    data: List[AMP]

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


class PagedFamilies(BaseModel):
    info: PageInfo
    data: List[Family]

    class Config:
        orm_mode = True


# Object for Download page ------------------------------------------------
# class Download(BaseModel):
#     List of strings
#
#     class Config:
#         orm_mode = True


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
    seq_query: str
    seq_target: str
    alignment_strings: List[str]

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

    class Config:
        orm_mode = True


class Filters(BaseModel):
    family: List[str]
    habitat: List[str]
    host: List[str]
    sample: List[str]
    origin: List[str]

    class Config:
        orm_mode = True
