import pandas as pd
from sqlalchemy.orm import Session
import models
import schemas
import utils
from pprint import pprint
import livingTree as lt


def get_amp_list(db: Session, page: int = 0, page_size: int = 20, **kwargs):
    query = db.query(
        models.AMP.accession, models.AMP.family, models.AMP.sequence,
        models.Metadata.GMSC, models.Metadata.sample,
        models.Metadata.microontology, models.Metadata.environmental_features,
        models.Metadata.host_tax_id, models.Metadata.host_scientific_name,
        models.Metadata.latitude, models.Metadata.longitude,
        models.Metadata.origin_tax_id, models.Metadata.origin_scientific_name
    ).outerjoin(
        models.Metadata
    ).outerjoin(
        models.GMSC
    )

    # Mapping from filter keys to table columns
    metadata_cols = {
        'habitat': 'microontology',
        'host': 'host_scientific_name',
        'origin': 'origin_scientific_name',
        'gene': 'GMSC',
        'sample': 'sample'}
    for key, value in kwargs.items():
        if key in {'habitat', 'host', 'origin', 'gene', 'sample'}:
            if value:
                query = query.filter(getattr(models.Metadata, metadata_cols[key]) == value)
        elif key == 'family':
            if value:
                query = query.filter(getattr(models.AMP, key) == value)
        else:
            pass
    return query.offset(page * page_size).limit(page_size).all()


def get_amp(accession: str, db: Session, include_feature_graph: bool):
    amp_obj = db.query(models.AMP).filter(models.AMP.accession == accession).first()
    features = utils.get_features(amp_obj.sequence)
    if include_feature_graph:
        feature_graph_points = utils.get_graph_points(amp_obj.sequence)
        features["graph_points"] = feature_graph_points
    setattr(amp_obj, "features", features)
    return amp_obj


def get_families(db: Session, skip: int = 0, page_size: int = 100):
    pass


def get_downloads(db: Session, skip: int = 0, page_size: int = 100):
    pass


def get_distributions(accession: str, db: Session):
    raw_data = None
    if accession.startswith('AMP'):
        raw_data = db.query(models.Metadata).filter(models.Metadata.AMPSphere_code == accession).all()
    elif accession.startswith('SPHERE'):
        raw_data = db.query(models.Metadata).outerjoin(models.AMP).filter(models.AMP.family == accession).all()
    else:
        print('error')  # better handle this.
    metadata = pd.DataFrame([obj.__dict__ for obj in raw_data]).drop(columns='_sa_instance_state')
    print(metadata)
    color_map = {} ##### supply here
    metadata['latitude'] = metadata['latitude'].replace('', None).astype(float).round(1)
    metadata['longitude'] = metadata['longitude'].replace('', None).astype(float).round(1)
    metadata['habitat_type'] = pd.Categorical(metadata['microontology'].apply(lambda x: x.split(':')[0]))
    # metadata['color'] = metadata['habitat_type'].map(color_map)
    data = dict(
        geo=metadata[['AMPSphere_code', 'latitude', 'longitude', 'habitat_type']].
            groupby(['latitude', 'longitude', 'habitat_type'], as_index=False, observed=True).size(),
        hosts=metadata[['AMPSphere_code', 'host_tax_id', 'host_scientific_name']].
            groupby('host_tax_id', as_index=False).size(),
        habitats=metadata[['AMPSphere_code', 'microontology', 'habitat_type']].
            groupby(['microontology', 'habitat_type'], as_index=False).size(),
        origins=metadata[['AMPSphere_code', 'origin_tax_id', 'origin_scientific_name']].
            groupby('origin_tax_id', as_index=False).size()
    )

    # FIXME fix color map for geo plot
    print('Processing geo data...')
    names = {'latitude': 'lat', 'longitude': 'lon', 'AMPSphere_code': 'size'}
    data['geo'].rename(columns=names, inplace=True)
    print(data['geo'])
    # FIXME hierarchical structure generation.
    data['habitats']['microontology'].str.split(':', expand=True).fillna('Unknown')
    print(data['habitats'])

    print('Assigning lineages to taxa...')
    # Fix id inconsistency.
    data['hosts']['host_tax_id'] = data['hosts']['host_tax_id'].apply(lambda x: x if x != 2116673.0 else 85678.0)
    pd.DataFrame(lt.LineageTracker(ids=data['hosts']['host_tax_id'].astype(int)).paths_sp,
                     columns=['sk', 'k', 'p', 'c', 'o', 'f', 'g', 's'])
    data['hosts'].fillna('Unknown', inplace=True)
    print(data)
    return
