<template>
  <div id="About">
    <div class="row justify-center">
      <div class="col-xs-0 col-lg-2"></div>
      <div class="col-12 col-lg-8 justify-center q-pr-md q-ma-auto">
        <div class="row">
          <div class="col-12 col-md-6 q-pr-md">
            <h4>Overview</h4>
            <p>
              Antimicrobial peptides (AMPs) are small peptides (operationally
              defined here as proteins with 10-100 amino acid residues). These
              small proteins are able to disturb microbial growth and can be
              produced by a wide range of organisms from all domains of life.
              These peptides are ancient defense molecules and some recently
              have shown activity against multi-resistant pathogens. Besides
              their potential to clinical applications, AMPs also are widely
              used in food preservation and agriculture.
            </p>
            <p>
              Because of their small size, AMPs cannot be detected with high
              confidence by standard gene prediction methods. Therefore, AMPs
              are often discarded (<a
              href="https://peerj.com/articles/10555/">Santos-Júnior <i>et
              al</i>; PeerJ 2020</a>).
            </p>
            <p>
              Recently, <a href="https://big-data-biology.org/">we</a>
              developed <a
              href="https://big-data-biology.org/software/macrel/">Macrel</a>,
              which unlike other methods, was developed for metagenomes. Using
              Macrel, we started the Global Survey for AMPs, a project which
              intends to collect all AMP sequences available in the
              publicly-available databases to date.
              Thus, motivated to develop a database-assisted platform that
              provides comprehensive functional and physicochemical features of
              large-scale (meta)genomic-derived AMPs, we created AMPsphere!

            </p>
            <p>
              Just as the ecosphere is the worldwide sum of all ecosystems, the
              AMPsphere comprises the complexity of prokaryotic AMPs assembled
              in one dataset. To date, we analyzed the 86k high-quality genomes
              in <a href="https://progenomes.embl.de/">proGenomes2</a>, and
              over 63k metagenomes from <a
              href="https://www.ebi.ac.uk/ena/browser/">ENA</a>, <a
              href="https://ncbi.nlm.nih.gov/">NCBI</a> and
              <a href="https://genome.jgi.doe.gov/portal/">JGI</a>. After
              redundancy removal, we produced a collection of AMPs from the
              global microbiome, containing 863,498 distinct sequences,
              clustered into 10,715 AMP families with at
              least 7 sequences each.

           </p>
           <p>
              AMPSphere is permanently deposited in Zenodo under <a
              href="https://doi.org/10.5281/zenodo.4574468">DOI:
              10.5281/zenodo.4574468</a>.
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

            <div class="text-bold">Tools</div> <p>AMPSphere has two tools for
            sequence searching by homology direct alignment and HMM profiles of
            families preloaded with our database.

            </p>

            <div class="text-bold">Getting more help</div>
            <p>Questions can be sent to the <a
            href="https://groups.google.com/g/ampsphere-users">mailing list</a>
            dedicated to the project. To enable local analyses, the complete
            database is available for download</p>

            <div class="text-bold">Downloads &amp; API</div>
            <p>Advanced users can <a href="/downloads">download all our data</a>
            or query it using <a href="/api">the API</a>.</p>

            <div class="text-bold">Acknowledgements</div>
            <p>This project is conducted in collaboration with the <a
            href="https://www.embl.org/groups/bork/">Bork Group at EMBL</a> and
            the <a href="http://compgenomics.org/">Huerta-Cepas group at
            CPGB</a>.</p>

            <p>We would like to acknowledge in particular: T.S.B. Schmidt; A.N.
            Fullam; P. Bork; X. Zhao and J. Huerta-Cepas.</p>

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
