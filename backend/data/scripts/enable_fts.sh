#!/usr/bin/env bash


#    GMSC = Column(String, primary_key=True, index=True)
#    AMPSphere_code = Column(String, ForeignKey(AMP.accession), index=True)
#    sample = Column(String, index=True)
#    microbial_source = Column(String, index=True)
#    specI = Column(String, index=True)
#    is_metagenomic = Column(Boolean, index=True)
#    geographic_location = Column(String, index=True)
#    latitude = Column(Float)
#    longitude = Column(Float)
#    general_envo_name = Column(String, index=True)


sqlite-utils enable-fts ampsphere_main_db/AMPSphere_v.2021-03.sqlite Metadata \
GMSC sample microbial_source specI geographic_location general_envo_name

# Test command:
#   sqlite-utils search ampsphere_main_db/AMPSphere_v.2021-03.sqlite Metadata soil