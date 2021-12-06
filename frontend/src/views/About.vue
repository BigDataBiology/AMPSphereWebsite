<template>
  <div id="About">
    <div class="row justify-center">
      <div class="col-xs-0 col-lg-2"></div>
      <div class="col-12 col-lg-8 justify-center q-pr-md q-ma-auto">
        <div class="row">
          <div class="col-12 col-md-6 q-pr-md">
            <h4>Overview</h4>
            <p>
              Antimicrobial peptides (AMPs) are small proteins with 10 to 100 residues of amino acids.
              The small proteins are able to disturb microbial growth and can be produced by a wide range
              of organisms being found in all life domains. These peptides are ancient defense molecules
              and some recently have shown activity against multi-resistant pathogens. Besides their potential
              to clinical applications, AMPs also are widely used in food preservation and agriculture.
            </p>
            <p>
              Although small molecules, they have an immense diversity and cannot be detected with enough
              confidence by the gene prediction methods. Because of that, AMPs are often discharged to reduce
              the false discovery rate. Therefore, uncovering the diversity of AMPs is not just a matter of
              homology-based function prediction, instead it involves complex patterns and feature discovery
              with machine learning.
            </p>
            <p>
              Recently, the <a href="big-data-biology.org/">Big Data Biology Research Group</a> from the
              <a href="istbi.fudan.edu.cn/">Institute of Science and Technology for Brain-inspired Intelligence (ISTBI / Fudan University)</a>
              developed a method called <a href="https://big-data-biology.org/software/macrel/">Macrel</a>,
              which differently from other methods, was developed to metagenomic approaches also handling a variety
              of data formats (from reads to peptide sequences). By using Macrel, we started the Global Survey for AMPs
              , a project which intends to collect all AMP sequences available in the publicly-available databases to
              date.
              Thus, motivated to develop a database-assisted platform that provides comprehensive functional and
              physicochemical features of large-scale (meta)genomic-derived AMPs, we created AMPsphere!
            </p>
            <p>
              Just as the ecosphere is the worldwide sum of all ecosystems, the AMPsphere comprises the complexity of
              prokaryotic AMPs assembled in one dataset. To this date, it was analyzed the 86k high-quality genomes in
              <a href="progenomes.embl.de/">ProGenomes2</a>, and over 63k metagenomes from
              <a href="https://www.ebi.ac.uk/ena/browser/">ENA</a>, <a href="ncbi.nlm.nih.gov/">NCBI</a> and
              <a href="https://genome.jgi.doe.gov/portal/">JGI</a>. After redundancy removal, we produced a collection of AMPs from
              the global microbiome, containing 863,498 distinct sequences, clustered into 10,715 AMP families with at
              least 7 sequences each. AMPSphere is permanently deposited in Zenodo in the
              <a href="https://doi.org/10.5281/zenodo.4574468">link</a>.
            </p>

          </div>
          <div class="col-12 col-md-6 q-pl-md ">
            <h4>Benefits and Features</h4>

            <div class="text-bold">Integration</div>
            <p>AMPSphere is available as a web resource that displays each AMP
            for browsing by family, location, and samples where it was
            found.</p>

            <div class="text-bold">Functional and physicochemical properties</div>
            <p>In the individual AMP cards, information such as pI, charge,
            molecular weight, hydrophobicity, the proportion of charged
            residues, and the probabilities associated with the predictions of
            its antimicrobial and hemolytic activities are available.</p>

            <div class="text-bold">AMPs from different species</div>
            <p>Collected AMPs can be mapped back to species, NCBI taxID accession
            codes, and also the accession of (meta)genomes. Besides that, AMP
            families also have pre-calculated phylogenetic trees, hidden Markov
            models (HMM), and alignments available.</p>

            <div class="text-bold">Tools</div> <p>AMPSphere has two tools for sequence searching by homology direct alignment and HMM profiles of
            families preloaded with our database.</p>

            <div class="text-bold">Getting more help</div>
            <p>Users can interact in a
            <a href="https://groups.google.com/g/ampsphere-users">mailing
            list</a> dedicated to the resource. To enable local analyses, the
            complete database is available for download</p>

            <div class="text-bold">Downloads &amp; API</div>
            <p>Advanced users can <a href="/downloads">download all our data</a>
            or query it using <a href="/api">an API</a>.</p>

          </div>
        </div>
      </div>
      <div class="col-xs-0 col-lg-2 bg-white"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "About",
}
</script>

<style scoped>

</style>
