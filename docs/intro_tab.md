# Global prokaryotic AMPs survey

_Version_ = AMPsphere v.2021-03 

_Curators_ = [ Santos-Junior CD, Hui C, Coelho LP ]

## Overview

Antimicrobial peptides (AMPs) are small proteins with lengths ranging from 10 to 100
residues of amino acids, which disturb microbial growth and can be produced by a wide
range of organisms belonging to all life domains. These peptides are ancient defense
molecules and some recently have shown activity against multi-resistant pathogens.
Besides their clinical applications, AMPs also can be widely used in food preservation
and agriculture.

Although small molecules, their diversity is huge and is hidden from most of the current
bioinformatics techniques. In other words, peptides are not detected with enough
confidence by the gene prediction methods and are often discharged to reduce the false
discovery rate. Therefore, uncovering the diversity of AMPs is not just a matter of
function prediction by homology, instead involves complex patterns and feature discovery
with machine learning. 

Recently, the Big Data Biology Research Group from the Institute of Science and Technology
for Brain-inspired Intelligence (ISTBI / Fudan University) developed a method called Macrel,
which differs from other methods was directed to metagenomic approaches and can handle a
variety of data formats (from reads to peptide sequences). By using Macrel, we started the
Global AMPs Survey, a project which intends to collect all AMP sequences available in the
public databases to date. Thus, motivated to develop a database-assisted platform that
provides comprehensive functional and physicochemical features of large-scale (meta)genomic-
derived AMPs, we created AMPsphere!

Just as the ecosphere is the worldwide sum of all ecosystems, the AMPsphere is the complexity
of prokaryotic AMPs assembled in one dataset. To this date, it was analyzed ProGenomes2, which
includes 86 thousand high-quality genomes, as well as a dataset of over 35,000 publicly
available metagenomes. After redundancy removal, we produced a collection of AMPs from the
global microbiome, containing 317,790 distinct sequences, clustered into 4,705 AMP families.
 
### Benefits and Features
                
**1. Integration**

AMPsphere displays each AMP as a flashcard and also as a list, clicking on it, you can access its
family, location, and even samples where it was found. In the cases when AMPs were spotted in other
databases, preferentially DRAMP, we also referred to their accession code, allowing users to cross
information. 
                
**2. Functional and physicochemical properties**

In the flashcard of each AMP there is information such as pI, charge, molecular weight, hydrophobicity,
the proportion of charged residues, and the probabilities associated with the predictions of its
antimicrobial and hemolytic activities. In some cases, the targets also were predicted using machine
learning. Functionalities are available to filter the more than 300 thousand AMPs present in AMPsphere by
physical-chemical properties or geographical/sample type origin.
                    
**3. AMPs from different species**

An user-friendly interface for browsing the collected AMPs in AMPsphere provides users the possibility to
map AMPs back to specI clusters, species name, NCBI taxID access codes, and also metagenome access codes.
Besides that, AMPsphere presents a classification of all collected AMPs into families by identity, with
phylogenetic trees, hidden Markov models (HMM), and alignments.
                    
**4. Tools**

AMPsphere presents a section of tools with search tools preloaded with our database, where users
can insert query sequences and search for homologs. Adjusting parameters, Blast can be used for
direct ortholog search of AMP sequences and HMMSearch for AMP families. The database also is
linked with the Macrel developing team and tool, allowing users to contribute actively with the
search for new AMPs.
                    
**5. AMP web interface**

Users can interact with the AMPsphere team and other users in a google community.
To enable local analyses, the complete database is available for download on two
different sites, the latest releases are both in Zenodo and on this
web page. Users are allowed to browse all the AMPs' functionalities.





