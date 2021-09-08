<template>
    <div id="Help">
      <el-row>
        <el-col :span="22" :offset="1">
          <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
            <el-breadcrumb-item :to="{ path: '/help' }">Help</el-breadcrumb-item>
          </el-breadcrumb>
          <br/>
          <el-tabs type="card" @tab-click="handleTabClick">
            <el-tab-pane label="AMPSphere" lazy=true>
              <!--        <h1 style="text-align: center">Global prokaryotic AMPs survey</h1>-->
              <el-col :offset="1" :span="10">
<!--                TODO go to `about page`-->
                <h2>Overview</h2>
                Antimicrobial peptides (AMPs) are small proteins with lengths ranging from 10 to 100
                residues of amino acids, which disturb microbial growth and can be produced by a wide
                range of organisms belonging to all life domains. These peptides are ancient defense
                molecules and some recently have shown activity against multi-resistant pathogens.
                Besides their clinical applications, AMPs also can be widely used in food preservation
                and agriculture. <br/><br/>
                Although small molecules, their diversity is huge and is hidden from most of the current
                bioinformatics techniques. In other words, peptides are not detected with enough
                confidence by the gene prediction methods and are often discharged to reduce the false
                discovery rate. Therefore, uncovering the diversity of AMPs is not just a matter of
                function prediction by homology, instead involves complex patterns and feature discovery
                with machine learning.<br/><br/>
                Recently, the <el-link type='primary' href="https://big-data-biology.org">Big Data
                Biology Research Group</el-link> from the Institute of Science and Technology
                for Brain-inspired Intelligence (ISTBI / Fudan University) developed a method called Macrel,
                which differs from other methods was directed to metagenomic approaches and can handle a
                variety of data formats (from reads to peptide sequences). By using Macrel, we started the
                Global AMPs Survey, a project which intends to collect all AMP sequences available in the
                public databases to date. Thus, motivated to develop a database-assisted platform that
                provides comprehensive functional and physicochemical features of large-scale (meta)genomic-
                derived AMPs, we created AMPsphere!<br/><br/>
                Just as the ecosphere is the worldwide sum of all ecosystems, the AMPsphere is the complexity
                of prokaryotic AMPs assembled in one dataset. To this date, it was analyzed ProGenomes2, which
                includes 86 thousand high-quality genomes, as well as a dataset of over 35,000 publicly
                available metagenomes. After redundancy removal, we produced a collection of AMPs from the
                global microbiome, containing 317,790 distinct sequences, clustered into 4,705 AMP families.<br/><br/>
              </el-col>
              <el-col :span="10" :offset="1">
                <h2>Benefits and Features</h2>

                <div style="font-weight: bold">1. Integration</div>
                AMPsphere displays each AMP as a flashcard and also as a list, clicking on it, you can access its
                family, location, and even samples where it was found. In the cases when AMPs were spotted in other
                databases, preferentially DRAMP, we also referred to their accession code, allowing users to cross
                information.<br/><br/>

                <div style="font-weight: bold">2. Functional and physicochemical properties</div>
                In the flashcard of each AMP there is information such as pI, charge, molecular weight, hydrophobicity,
                the proportion of charged residues, and the probabilities associated with the predictions of its
                antimicrobial and hemolytic activities. In some cases, the targets also were predicted using machine
                learning. Functionalities are available to filter the more than 300 thousand AMPs present in AMPsphere by
                physical-chemical properties or geographical/sample type origin.<br/><br/>

                <div style="font-weight: bold">3. AMPs from different species</div>
                An user-friendly interface for browsing the collected AMPs in AMPsphere provides users the possibility to
                map AMPs back to specI clusters, species name, NCBI taxID access codes, and also metagenome access codes.
                Besides that, AMPsphere presents a classification of all collected AMPs into families by identity, with
                phylogenetic trees, hidden Markov models (HMM), and alignments.<br/><br/>

                <div style="font-weight: bold">4. Tools</div>
                AMPsphere presents a section of tools with search tools preloaded with our database, where users
                can insert query sequences and search for homologs. Adjusting parameters, Blast can be used for
                direct ortholog search of AMP sequences and HMMSearch for AMP families. The database also is
                linked with the Macrel developing team and tool, allowing users to contribute actively with the
                search for new AMPs.<br/><br/>

                <div style="font-weight: bold">5. AMP web interface</div>
                Users can interact with the AMPsphere team and other users in a google community.
                To enable local analyses, the complete database is available for download on two
                different sites, the latest releases are both in Zenodo and on this
                web page. Users are allowed to browse all the AMPs' functionalities.<br/><br/>
              </el-col>
            </el-tab-pane>
            <el-tab-pane label="AMP pages" lazy=true>
<!--              <h1 id="help-for-amp-pages">Help for AMP pages</h1>-->
              <p>AMPSphere has different pages with information of AMPs about their biochemistry and sequence organization to obtain the best insights from each sequence. This information is divided into numerical values and graphical. Below, we detailed point by point their meaning, origin, and how to use them.</p>
              <hr />
              <h2 id="the-amp-info-cards">The AMP info cards</h2>
              <p>AMPSphere brings analyses for each AMP sequence organized as cards, for example:</p>
              <pre><code>        ---------------------------------------------------------
        [PROC] -- AMP10.000_000
        ---------------------------------------------------------
        sequence = KKVKSIFKKALAMMGENEVKAWGIGIK
        MW = 3.01 kDa
        Length = 27
        Molar extinction = (5500, 5500)
        Aromaticity = 0.07407407407407407
        GRAVY = -0.11111111111111117
        Instability index = -18.348148148148148
        Isoeletric point = 10.12554931640625
        Charget at pH 7.0 = 4.758729531142717

        ---------------------------------------------------------
        Secondary Structure Assessment

        helix: 29.629629629629626
        turn: 18.51851851851852
        sheet: 29.629629629629626
        ---------------------------------------------------------</code></pre>
              <p>These results obtained using ProtParam include the molecular weight, theoretical pI, instability index, aliphatic index, and grand average of hydropathicity (GRAVY).</p>
              <p>The molar extinction comes from the Lambert-Beer law and indicates how much light a protein absorbs at a given wavelength. It helps in the determination of protein concentration in water or diluted solutions from its absorbance. The molar extinction coefficient assesses the protein contents of tyrosine, tryptophan, and cystine (because cysteine does not absorb light considerably at wavelengths &gt;260 nm). Protein molar extinction coefficients used the Edelhoch method (<a href="https://pubmed.ncbi.nlm.nih.gov/6049437/">Edelhoch (1967)</a>), with the extinction coefficients for Trp and Tyr determined by <a href="https://pubmed.ncbi.nlm.nih.gov/8563639/">Pace et al. (1995)</a>. The calculus can be simplified by:</p>
              <pre><code>    Extinction coefficient = (#Tyr)*Ext(Tyr) + (#Trp)*Ext(Trp) + (#Cystine)*Ext(Cystine)

    where (at 280 nm):

        Ext(Tyr) = 1490
        Ext(Trp) = 5500
        Ext(Cystine) = 125</code></pre>
              <p>The absorbance (optical density) is calculated using the following formula:</p>
              <pre><code>    Absorb(Prot) = extinction coefficient / molecular weight
</code></pre>
              <p>ProtParam produces two values: one assuming all cysteine residues appear as half cystines, and the second, that no cysteine appears as half cystine.</p>
              <p>The aromaticity is calculated as described by <a href="https://pubmed.ncbi.nlm.nih.gov/8065933/">Lobry, 1994</a> and is the relative frequency of Phe + Trp + Tyr in the entire sequence. Higher values of this parameter can lead to less soluble proteins.</p>
              <p>The Grand Average of Hydropathy (GRAVY) value for a peptide or protein described in <a href="https://pubmed.ncbi.nlm.nih.gov/7108955/">Kyte and Doolittle (1982)</a> consists of summing the hydropathy values of each residue in the peptide and dividing by its length.</p>
              <p>The instability index (II) measures the peptide stability in a test tube considering the statistical analysis of 12 unstable and 32 stable proteins (<a href="https://pubmed.ncbi.nlm.nih.gov/2075190/">Guruprasad et al., 1990</a>). The analysis revealed certain dipeptides significantly happening in the unstable proteins when compared with stable ones. Thus, the 400 different dipeptides (DIWV) assigned to values measuring their instability take place in the II calculus as follows:</p>
              <pre><code>              i=L-1
II = (10/L) * Sum  DIWV(x[i]x[i+1])
              i=1

where:

    L is the length of the sequence

    DIWV(x[i]x[i+1]) is the instability weight
                         value for the dipeptide
                         starting in position i.</code></pre>
              <p>II less than 40 predicts a protein as stable.</p>
              <p>Protein isoelectric point (pI) calculated using pK values of amino acids described in Bjellqvist et al.(<a href="https://pubmed.ncbi.nlm.nih.gov/8125050/">1993</a> and <a href="https://pubmed.ncbi.nlm.nih.gov/8055880/">1994</a>) in pH 7.0 at 25°C. This method is from <a href="https://biopython.org/docs/1.75/api/Bio.SeqUtils.ProtParam.html">Bio.SeqUtils.ProtParam</a>. The charge of a protein at given pH is calculated as a derivation of Henderson- Hasselbalch equation:</p>
              <pre><code>    pH = pKa + log([A-]/[HA])

    Rearranging:

        [HA]/[A-] = 10 ** (pKa - pH)

    partial_charge =

        [A-]/[A]total = [A-]/([A-] + [HA]) = 1 / { ([A-] + [HA])/[A-] } =
        1 / (1 + [HA]/[A-]) = 1 / (1 + 10 ** (pKa - pH)) for acidic residues;
                                      1 / (1 + 10 ** (pH - pKa)) for basic residues


        charge = positive_charge - negative_charge
</code></pre>
              <p>Molecular weight (MW) values are in thousands of Daltons (kDa) and was obtained by adding the average isotopic masses of amino acids in the protein and one water molecule.</p>
              <p>The secondary structure of the peptide, in AMPSphere, is a percent composition of a protein taking amino acids which tend to be in Helix, Turn, or Sheet. It follows the groups of amino acids belonging to helix (V, I, Y, F, W, L), turns (N, P, G, S), and sheets (E, M, A, L).</p>
              <p><strong>Be aware that:</strong></p>
              <ul>
                <li>The current predictions may not be adequate for very alkaline proteins.</li>
                <li>pI predictions for small proteins can be problematic.</li>
                <li>It is not taken into account the effects of post-translational modifications.</li>
                <li>The molar extinction calculus assumes that no other chromophores that absorb at 280 nm are present in the protein.</li>
                <li>Molar extinction can have more than 10% error for proteins without Trp residues.</li>
              </ul>
              <hr />
              <h2 id="graphs-in-amp-cards">Graphs in AMP cards</h2>
              <p>The amino acids compositional deviation was calculated using the Z-score calculated from two different groups (AMPs and non-AMPs) previously used in the training set of Macrel models (<strong>Fig. 1</strong>).</p>
              <figure class="figure">
<!--                <img style="align-content: center;" src="../assets/figures/aa_composition_deviation_AMP10.000_000.png" width="450" height="300">-->
                <figcaption class="figure-caption">
                  Fig. 1. Compositional deviation of peptide AMP10.000_000 from Macrel’s training set of AMPs and non-AMPs.<br>
                </figcaption>
              </figure>
              <p><br/>This method consists of calculating the average percent composition of AMPs and non-AMPs separately per amino acid. Then using the Z-score:</p>
              <pre><code>
    Z-score(amino acid x) = (X% - Xmu) / Xstd

    where:

        X% - amino acid X percent composition in the protein

        Xstd - standard deviation of amino acid X percent composition
                       of the set of AMPs or NAMPs in the training set used in
                       Macrel models

        Xmu - average amino acid X percent composition of the set of
                      AMPs or NAMPs in the training set used in Macrel models
</code></pre>
              <p>A negative Z score means that a specific amino acid decreased compared with the average training set for AMPs or non-AMPs. On the other side, a positive Z-score means the opposite, the increment of some amino acid compared to the average training set. Whether the Z-score is around zero, then the peptide composition is close to the average training set.</p>
              <p>We produced Z-score graphs to compare AMPs with the training set used by Macrel of AMPs and non-AMPs, placing a given peptide in this background (<strong>Fig. 2</strong>). The average and standard deviation for each of the features calculated from Macrel’s training set were used to derive the Z-scores for AMPs and non-AMPs. These Z-scores were plotted for each variable and grouped by color (black for AMPs and gray for non-AMPs, respectively). Among the several different tested features, some of them were already above mentioned in detail.</p>
              <figure class="figure">
<!--                <img style="align-content: center;" src="../assets/figures/zscore_comparison.png" width="700" height="1000">-->
                <figcaption class="figure-caption">
                  Fig. 2. Z-score comparison of (a) aliphatic index, (b) Boman index, (c) hydrophobic moment, (d) instability index - instaindex, (e) isoelectric point, and (f) charge using the average of complete training set separated by non-antimicrobial peptides (gray), antimicrobial peptides (black) and dots representing the peptide as a red star - in this example, AMP10.000_000.
                </figcaption>
              </figure>
              <p><br/>The aliphatic index (AI) consists of the relative volume occupied by aliphatic side chains from Ala, Val, Leu/Ile. It correlates positively with the increasing thermostability of globular proteins. Then, it is possible to compare this parameter with the population of AMPs and non-AMPs sorted by length and again using the same rationale for Z-scores (<strong>Fig. 2a</strong>) AI can be calculated using the method from <a href="https://pubmed.ncbi.nlm.nih.gov/7462208/">Ikai (1980)</a>, as follows:</p>
              <pre><code>  AI = X(Ala) + a * X(Val) + b * ( X(Ile) + X(Leu) )

  where

        X(Ala), X(Val), X(Ile), and X(Leu) are mole percent of those amino acids (100 X mole fraction)
        a (= 2.9) represents the relative volume of the side chain of valine to alanine
        b (= 3.9) represents the relative volume of the side chain of leucine/isoleucine to alanine </code></pre>
              <p>In <strong>Fig. 2b</strong> it is possible to observe the placement of the tested sequence among AMPs and non-AMPs using the Boman index. This index, proposed by <a href="https://pubmed.ncbi.nlm.nih.gov/12930229/">Boman (2003)</a>, is the propensity of a peptide interacting with protein receptors or membranes. Boman index is the sum of the solubility values for all residues in a sequence divided by the number of residues. For reference, indices above 2.48 mean that the protein has high binding potential.</p>
              <p>The hydrophobic moment (H-moment) distribution in <strong>Fig. 2c</strong> detects the periodicity of hydrophobic residues of a protein. It measures the amphiphilicity perpendicular to the axis of any periodic peptide structure (a-helix or b-sheet). H-moment is especially useful to characterize AMPs, as their hydrophobic residues usually are arranged in a side of these structures.</p>
              <p>The standardized hydrophobicity scale developed by <a href="https://pubmed.ncbi.nlm.nih.gov/6582470/">Eisenberg (1984)</a> is used to calculate the H-moment. The hydrophobicity of each residue in a protein window multiplied by their unit vector sums up the final H-moment. The unit vectors are the angular momentum to the nucleus of the alpha- carbon toward the geometric center of the side chain. Simplifying, it is obtained as follows:</p>
              <pre><code>    H-moment = sum(Hn*Sn)

    H-moment = sum(Hn*sin(delta))**2 + sum(Hn*cos(delta))**2

    where:
            Hn is the hydrophobicity of the residue n

            sin(delta) is the sine of the angle delta in radians
                       having the periodic structure divided into
                       windows (100°)

            cos(delta) is the cosine of the angle delta in radians
                       having the periodic structure divided into
                       windows (100°)</code></pre>
              <p>The charge, instability index, and isoelectric point were calculated as mentioned in the previous section and compared against AMP and non-AMP sets using Z-score as shown in <strong>Fig. 2d-f</strong>.</p>
              <p>Usually, in globular proteins, helices have one face oriented toward the hydrophobic core and the other is solvent-exposed. The helical wheel (<strong>Fig. 3</strong>) illustrates this property of alpha-helices, through the concentration of hydrophobic amino acids on one side of the helix, with polar or hydrophilic amino acids on the other.</p>
              <figure class="figure">
<!--                <img style="align-content: center;" src="../assets/figures/helicalwheel_AMP10.000_000.png" width="300" height="300">-->
                <figcaption class="figure-caption">
                  Fig. 3. Amino acids helical wheel with the H-moment indicated.
                </figcaption>
              </figure>
              <p><br/>Helical wheels draw the protein residues in a rotation of 100° between consecutive amino acids. The H-moment and direction showed inside the wheel point to its maximum momentum. <strong>Fig. 3</strong> plotted using <a href="https://doi.org/10.1093/bioinformatics/btx285">modlAMP</a> has a color code for amphiphilicity of residues available in the module as it follows:</p>
              <pre><code>The amphipatic color code from modlAMP uses 8 colors:

G, A                        Beige
N, Q                        Purple
S, T                        Pink
K, R                        Blue
H                           Light blue
D, E                        Bordeaux
P                           Green
F, L, W, M, V, I, C, Y      Yellow</code></pre>
              <p><strong>Figures 4-7</strong> compute a profile by residues using scanning with fixed window size and different scale parameters. An amino acid scale is a numerical value assigned to each type of amino acid according to some specific feature in which they are classified or measured. To make a profile we also can use sequence positions or even the amino acids sequence colored by amino acids properties. In the above-mentioned figures we used Lesk’s color scale to code sequences in the X-axis as follows:</p>
              <pre><code>The colour scheme from Lesk

It uses 5 groups (note Histidine):

    Small nonpolar        G, A, S, T                    Orange
    Hydrophobic           C, V, I, L, P, F, Y, M, W     Green
    Polar                 N, Q, H                       Magenta
    Negatively charged    D, E                          Red
    Positively charged    K, R                          Blue
    </code></pre>
              <p>Our calculations used the algorithm implemented in <a href="http://www.expasy.org/cgi-bin/protscale.pl">ProtScale</a>, in which for a window size n, we use the i-(n-1)/2 neighboring residues on each side to compute the score for i.</p>
              <p>The hydrophobicity scale adopted in the AMPSphere (<a href="https://pubmed.ncbi.nlm.nih.gov/2430611/">Parker et al., 1986</a>) and used in <strong>Fig. 4</strong>. is derived by measuring HPLC retention times of peptide libraries. It presents two adjacent copies of a variable residue in a random coil peptide, one more exposed located toward the N-terminus of the peptide and one packed between the other copy of the tested residue and a Leucine residue (Ac–GXXLLLKK–amide).</p>
              <figure class="figure">
<!--                <img style="align-content: center;" src="../assets/figures/hydrophobicity_Parker_AMP10.000_000.png" width="500" height="300">-->
                <figcaption class="figure-caption">
                  Fig. 4. Profile of hydrophobicity of residues of AMP10.000_000 using the relative scale of Parker.
                </figcaption>
              </figure>
              <p><br/>This scale is interesting to understand whether hydrophobic or hydrophilic stretches are present in the peptide. If the hydrophobicity is above 0.5, it is considered hydrophobic (<a href="https://doi.org/10.1016/j.jtbi.2017.02.012">Pane et al., 2017</a>).</p>
              <p>The profile of residues free energy of transfer from water to membrane lipid (Ez) in <strong>Fig. 5</strong> was conceived initially by <a href="https://pubmed.ncbi.nlm.nih.gov/17174324/">Senes et al. (2007)</a>. Ez estimated by a reverse-Boltzman relationship of potential can be calculated from the propensities for the occurrence of each residue as a function of their depth in the lipid bilayer <a href="https://pubmed.ncbi.nlm.nih.gov/17174324/">Senes et al. (2007)</a>.AMPs need to have low free energy for transfer to easily insert themselves in the lipid membranes, triggering their effects. The scale adopted in <strong>Fig. 5</strong> is the same as in <a href="https://doi.org/10.1093/bioinformatics/btx285">modlAMP</a>.</p>
              <figure class="figure">
<!--                <img style="align-content: center;" src="../assets/figures/EZenergy_AMP10.000_000.png" width="500" height="300">-->
                <figcaption class="figure-caption">
                  Fig. 5. Profile of AMP10.000_000 residues free energy of transfer from water to membrane lipid.
                </figcaption>
              </figure>
              <p><br/>In a complementary way to hydrophobicity, solvent accessibility (SA) can show which residues are exposed or buried, as shown in <strong>Fig. 6</strong>. It uses the Emini Surface fractional probability (EM) scale in the <a href="https://biopython.org/wiki/ProtParam">Bio.SeqUtils.ProtParam</a> module. The scale used is that in <a href="https://pubmed.ncbi.nlm.nih.gov/2991600/">Emini et al. (1987)</a> based on the formula:</p>
              <pre><code>  Sn = (n+4+i)*(0.37)-6

  where
        Sn is the surface probability of residue n
        dn is the fractional surface probability value of the amino acid n
        i vary from 1 to 6 depending on its position in the window</code></pre>
              <p>SA values greater than 1.0 indicate an increased probability of being found on the surface. AMPs present an interesting periodicity of exposed and buried motifs, which arguments in the sense that they can form secondary structures and possibly interact with membranes and the extra/intra-cellular milleu.</p>
              <figure class="figure">
<!--                <img style="align-content: center;" src="../assets/figures/SA_AMP10.000_000.png" width="500" height="300">-->
                <figcaption class="figure-caption:bold">
                  Fig. 6. Profile of solvent accessibility of residues of AMP10.000_000.
                </figcaption>
              </figure>
              <p><br/>The calculated flexibility profile (<strong>Fig. 7</strong>) shows regions submitted to higher tensions in the molecule and those able to move the rigid structure into a more favorable conformation. Therefore, accurate analysis of the peptide flexibility can lead to valuable ideas of how the peptide can fold and conformationally adjust. The normalized flexibility parameters (B-values) from <a href="https://onlinelibrary.wiley.com/doi/10.1002/prot.340190207">Vihinen (1994)</a> was the scale adopted in the profile calculation.</p>
              <figure class="figure">
<!--                <img style="align-content: center;" src="../assets/figures/flexibility_AMP10.000_000.png" width="500" height="300">-->
                <figcaption class="figure-caption">
                  Fig. 7. Profile of flexibility of residues of AMP10.000_000.
                </figcaption>
              </figure>
              <hr />
              <h2 id="references">References</h2>
              <p>Authors of AMPSphere claim no authorship over the methods here cited and attributes merit who deserves it. The methods here referenced can be found further explained in the links below:</p>
              <ul>
                <li><a href="https://web.expasy.org/">Expasy</a></li>
                <li><a href="https://web.expasy.org/protparam/">ProtParam tool</a></li>
                <li><a href="https://biopython.org/docs/1.75/api/Bio.SeqUtils.ProtParam.html">Bio.SeqUtils.ProParam</a></li>
                <li><a href="https://cran.r-project.org/web/packages/Peptides/Peptides.pdf">Peptides R Package</a></li>
                <li><a href="https://modlamp.org/">modlAMP documentation</a></li>
                <li><a href="macrel.readthedocs.io/">Macrel</a></li>
              </ul>
            </el-tab-pane>
            <el-tab-pane label="Family pages">
              under developing...
            </el-tab-pane>
          </el-tabs>
        </el-col>
      </el-row>
    </div>
</template>

<script>
    export default {
        name: 'Help',

        data() {
            return {}
        },
      methods: {
        handleTabClick(tab, event) {
          console.log(tab, event);
        },
      }
    }
</script>
