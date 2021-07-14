from typing import List, Optional

from pydantic import BaseModel


# Define JSON objects to be returned to frontend here.

# Object for AMP_card page ------------------------------------------------
class AMP_BasicInfo(BaseModel):
    Sequence: str
    Length: int
    Family_ID: str

class AMP_Feature(BaseModel):
    tinyAA: str
    smallAA: str
    aliphaticAA: str
    aromaticAA: str
    nonpolarAA: str
    polarAA: str
    chargedAA: str
    basicAA: str
    acidicAA: str
    charge: float
    pI: float
    aindex: float
    instaindex: float
    boman: float
    hydrophobicity: float
    hmoment: float
    SA_Group1_residue0: str
    SA_Group2_residue0: str
    SA_Group3_residue0: str
    HB_Group1_residue0: str
    HB_Group2_residue0: str
    HB_Group3_residue0: str
    AGG: str
    AMYLO: str
    TURN: str
    HELIX: str
    HELAGG: str
    BETA: str
    Level_I: str
    Level_II: str
    Level_III: str

class AMP_Prediction(BaseModel):
    AMP_Class: str
    AMP_Probability: float
    Hemolysis_Class: str
    Hemolysis_Probability: str

class AMP_Country(BaseModel):
    Asia: int
    Europe: int
    Africa: int
    South_America: int
    North_America: int
    Oceania: int
    Pacific_Ocean: int
    New_Zaeland: int

class AMP_Environment(BaseModel):
    Freshwater: int
    Gut: int
    Marine: int
    Milk: int
    Oral_Cavity: int
    Respiratory_Tract: int
    Skin: int
    Soil: int
    Surface: int
    Vagina: int
    Wastewater: int


class AMP(BaseModel):
    AMP_Accession: str
    AMP_Metagenome: List[str]
    AMP_Feature: AMP_Feature
    AMP_Prediction: AMP_Prediction
    AMP_Country: AMP_Country
    AMP_Environment: AMP_Environment
    class Config:
        orm_mode = True
# Object for Host page ------------------------------------------------
class Host(BaseModel):
    Host_Taxon_Id: int
    Host_Common_Name: str
    Host_Sci_Name: str
    Host_Counts = int

    class Config:
        orm_mode = True

# Object for Family page ------------------------------------------------
class Family(BaseModel):
    Family_AMP: List[str]
    Family_Environment: List[str]
    Family_Avg_Feature: List[float]
    Family_Std_Feature: List[float]

    class Config:
        orm_mode = True

# Object for Environment page ------------------------------------------------
class Env(BaseModel):
    pass

    class Config:
        orm_mode = True

# Object for Download page ------------------------------------------------
class Download(BaseModel):
    pass

    class Config:
        orm_mode = True

