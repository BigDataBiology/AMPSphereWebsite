def get_basic_info(accession):
    return {"Sequence": 'plllkplllkplllkplllkplllk',
    "Length": 25,
    "Family_ID": "SPHERE-III-000"}

def get_metagenomes(accession):
    return ['SRR11111', 'SRR233333']


def get_features(seq):
    return {"tinyAA": "AA",
    "smallAA": "AA",
    "aliphaticAA": "AA",
    "aromaticAA": "AA",
    "nonpolarAA": "AA",
    "polarAA": "AA",
    "chargedAA": "AA",
    "basicAA": "AA",
    "acidicAA": "AA",
    "charge": 1e-5,
    "pI": 1e-5,
    "aindex": 1e-5,
    "instaindex": 1e-5,
    "boman": 1e-5,
    "hydrophobicity": 1e-5,
    "hmoment": 1e-5,
    "SA_Group1_residue0": "K",
    "SA_Group2_residue0": "K",
    "SA_Group3_residue0": "K",
    "HB_Group1_residue0": "K",
    "HB_Group2_residue0": "K",
    "HB_Group3_residue0": "K",
    "AGG": "K",
    "AMYLO": "K",
    "TURN": "K",
    "HELIX": "K",
    "HELAGG": "K",
    "BETA": "K",
    "Level_I": "K",
    "Level_II": "K",
    "Level_III": "K"}

def get_prediction(seq):
    return {"AMP_Class": "__class__",
    "AMP_Probability": 0.66,
    "Hemolysis_Class": "__Hemolysis__",
    "Hemolysis_Probability": 0.80}


def get_country(accession):
    return {
    "Asia": 1,
    "Europe": 0,
    "Africa": 0,
    "South_America": 0,
    "North_America": 0,
    "Oceania": 0,
    "Pacific_Ocean": 0,
    "New_Zaeland": 0
    }


def get_envs(accession):
    return {
    "Freshwater": 1,
    "Gut": 0,
    "Marine": 0,
    "Milk": 0,
    "Oral_Cavity": 0,
    "Respiratory_Tract": 0,
    "Skin": 0,
    "Soil": 0,
    "Surface": 0,
    "Vagina": 0,
    "Wastewater": 0,
    }


def get_AMP_graphs(seq):
    return ['a', 'b', 'c']