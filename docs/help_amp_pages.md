# Help for AMP pages

AMPSphere has different pages with information, the simplest level is the
AMP which contains information about its biochemistry and sequence organization
in different scenarios to allow the user obtain the best insights for each
sequence.

This information can be divided into numerical values and graphical. Bellow 
it is detailed point by point how they were obtained and why to use them.

## The AMP info cards

AMPSphere brings several analysis in the antimicrobial peptides cards, such as:

```
        ---------------------------------------------------------
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
        ---------------------------------------------------------
```

These results are obtained using ProtParam including the molecular weight, theoretical pI, instability index, aliphatic index and
grand average of hydropathicity (GRAVY).

The molar extinction comes from the Lambert-Beer law and indicates how much light a protein absorbs at a given wavelength.
This can be used to the determination of the protein concentration in a given solution from its absorbance.
The molar extinction coefficient takes in consideration the contents of specific amino acids in the native protein in water,
specially tyrosine, tryptophan and cystine (because cysteine does not absorb light considerably at wavelengths >260 nm).
Protein extinction coefficients used the Edelhoch method ([Edelhoch (1967)](https://pubmed.ncbi.nlm.nih.gov/6049437/)),
with the extinction coefficients for Trp and Tyr determined by [Pace et al. (1995)](https://pubmed.ncbi.nlm.nih.gov/8563639/).
The calculus can be simplified by:

```
	Extinction coefficient = (#Tyr)*Ext(Tyr) + (#Trp)*Ext(Trp) + (#Cystine)*Ext(Cystine)

	where (at 280 nm):

		Ext(Tyr) = 1490
		Ext(Trp) = 5500
		Ext(Cystine) = 125
```


The absorbance (optical density) can be calculated using the following formula:


```
	Absorb(Prot) = extinction coefficient / molecular weight

```

Two values are produced by ProtParam, one assuming all cysteine residues appear as half cystines, and the second assuming that
no cysteine appears as half cystine.

The aromaticity is calculated as described by [Lobry, 1994]() and is the relative frequency of Phe + Trp + Tyr.

The Grand Average of Hydropathy (GRAVY) value for a peptide or protein is calculated as in
[Kyte and Doolittle (1982)](https://pubmed.ncbi.nlm.nih.gov/7108955/). It consists in the sum of hydropathy values of each
residues in the peptide and divided by the total length of the sequence.

The instability index (II) is an estimate of the peptide stability in a test tube at 4°C. This technique considers the
statistical analysis of 12 unstable and 32 stable proteins ([Guruprasad, et al. 1990](https://pubmed.ncbi.nlm.nih.gov/2075190/)).
The analysis revealed certain dipeptides significantly happening in the unstable proteins when compared with stable ones. Then,
it was assigned a weight value of instability to each of the 400 different dipeptides (DIWV). Therefore, the II is defined as:


```
              i=L-1
II = (10/L) * Sum  DIWV(x[i]x[i+1])
              i=1

where:

	L is the length of sequence

	DIWV(x[i]x[i+1]) is the instability weight
                         value for the dipeptide
                         starting in position i.

```

II of a protein when smaller than 40 predicts it as stable.

Protein isoelectric point (pI) is calculated using pK values of amino acids described in Bjellqvist
et al.([1993](https://pubmed.ncbi.nlm.nih.gov/8125050/) and [1994](https://pubmed.ncbi.nlm.nih.gov/8055880/))
under pH 7.0 at 25°C. Molecular weight (MW) values are given in x10^3 Daltons (kDa). This MW is obtained by
adding the average isotopic masses of amino acids in the protein and the mass of one water molecule.

The charge of a protein at given pH is calculated as a derivation of Henderson Hasselbalch equation:

```
	pH = pKa + log([A-]/[HA])

	Rearranging:

		[HA]/[A-] = 10 ** (pKa - pH)

	partial_charge =

		[A-]/[A]total = [A-]/([A-] + [HA]) = 1 / { ([A-] + [HA])/[A-] } =
		1 / (1 + [HA]/[A-]) = 1 / (1 + 10 ** (pKa - pH)) for acidic residues;
                                      1 / (1 + 10 ** (pH - pKa)) for basic residues


        charge = positive_charge - negative_charge

```

This method is derived from [Bio.SeqUtils.ProtParam](https://biopython.org/docs/1.75/api/Bio.SeqUtils.ProtParam.html)

The secondary structure of the peptide was given as a simple fraction of amino acids which tend to be in Helix, Turn or Sheet. 
It follows the groups of amino acids belonging to helix (V, I, Y, F, W, L), turns (N, P, G, S) and sheets (E, M, A, L). 
This value is given as percent of the total length of the protein.

**Be aware that:**

 + Prediction of protein pI for highly basic proteins is yet to be studied and possibly the current predictions may not be adequate.
 + pI predictions for small proteins can be problematic.
 + It is not taken in account the effects of post-translational modifications.
 + The molar extinction calculus assumes that no [other] chromophores that absorb at 280 nm are present in the protein.
 + Molar extinction can have more than 10% error for proteins without Trp residues.

## Graphs in AMP cards

The amino acids compositional deviation was calculated using the Z-score calculated from two different groups (AMPs and non-AMPs) previously
used in the trainingset of Macrel models (**Fig. 1**).

<figure class="figure">
    <img style="float: center;" src="figures/aa_composition_deviation_AMP10.000_000.png" width="450" height="300">
    <figcaption class="figure-caption">Fig. 1. Amino acids compositional deviation of AMP10.000_000.<br></figcaption>
</figure>

<br/>This method consists in calculating the average percent composition of AMPs and non-AMPs separatedly per amino acid. Then using the Z-score:


```

	Z-score(amino acid x) = (X% - Xmu) / Xstd

	where:

		X% - amino acid X percent composition in the protein

		Xstd - standard deviation of amino acid X percent composition
                       of the set of AMPs or NAMPs in the trainingset used in
                       Macrel models

		Xmu - average amino acid X percent composition of the set of
                      AMPs or NAMPs in the trainingset used in Macrel models 

``` 

A negative Z score means a negative variation in relation to the average, therefore, a reduction in comparison to the average behavior.
By the other side, a positive Z-score means the gropwth of that variable in relation to the tested group's average.
Then, when Z-score is close to zero, then we can tell that the peptide is actually close to the tested group's average.

Similarly, in **Fig. 2**, we produced Z-score graphs to keep comparing the AMPs and non-AMPs behavior and also to place a given peptide having
this given background in mind. To that we calculated the average of the entire trainingset used in Macrel and then the Z-scores for AMPs
and non-AMPs, plotting them for each feature and also as different groups by color (black and gray, respectively). We can observe several 
different features, some of them calculated as above mentioned.

<figure class="figure">
    <img style="float: center;" src="figures/zscore_comparison.png" width="700" height="1000">
    <figcaption class="figure-caption">Fig. 2. Z-score comparison of (a) aliphatic index, (b) boman index,
            (c) hydrophobic moment, (d) instability index - instaindex,
            (e) isoelectric point, and (f) charge using the average of
            complete training set separated by non-antimicrobial peptides
            (gray), antimicrobial peptides (black) and dots representing
            the peptide as a red start - in this example, AMP10.000_000.</figcaption>
</figure>

<br/>The aliphatic index (AI) consists in the relative volume occupied by aliphatic side chains from Ala, Val, Leu/Ile.
It is positively correlated with increasing thermostability of globular proteins. Then, it is possible to compare
this parameter with the population of AMPs and non-AMPs sorted by length and again using the same rationale for Z-scores (**Fig. 2a**)
AI can be calculated using the method from [Ikai (1980)](https://pubmed.ncbi.nlm.nih.gov/7462208/):

```
  AI = X(Ala) + a * X(Val) + b * ( X(Ile) + X(Leu) )  

  where
  
        X(Ala), X(Val), X(Ile), and X(Leu) are mole percent of those amino acids (100 X mole fraction) 
        a (= 2.9) represents the relative volume of side chain of valine in relation to alanine
        b (= 3.9) represents the relative volume of side chain of leucine/isoleucine in relation to alanine 

```

In **Fig. 2b** it is possible to observe the placement of the tested sequence among AMPs and non-AMPs using the Boman index.
This index measures the potential protein interaction and was initially proposed by [Boman (2003)](https://pubmed.ncbi.nlm.nih.gov/12930229/).
Its calculus consists in the sum of the solubility values for all residues in a sequence divided by the number of residues.
In this way, Boman index can give us the idea of how probable is the interaction of that protein with membranes or other proteins as receptors.
For reference, indices above than 2.48 mean that the protein has high binding potential. 

The hydrophobic moment (H-moment) distribution is shown in the **Fig. 2c** and detects periodicity in protein hydrophobicity.
In a more technical way, it measures of the amphiphilicity perpendicular to the axis of any periodic peptide structure,
such as the a-helix or b-sheet. That is interesting because it is expected for AMPs that the hydrophobic residues arrange in a
side of these structures. For its calculus the standardized [Eisenberg (1984)](https://pubmed.ncbi.nlm.nih.gov/6582470/)
hydrophobicity scale is used and the hydrophobicity of residues is multiplied by their unit vector derived from the angular arrangement
in relation to the nucleus of the alpha-carbon toward the geometric center of the side chain:

```
    H-moment = sum(Hn*Sn)
    
    H-moment = sum(Hn*sin(delta))**2 + sum(Hn*cos(delta))**2
    
    where:
            Hn is the hydrophobicity of the residue n

            sin(delta) is the sine of the angle delta in radians
                       having the periodic structure divided into
                       windows (for this calculus it is 100)

            cos(delta) is the cosine of the angle delta in radians
                       having the periodic structure divided into
                       windows (for this calculus it is 100)
```

The charge, instability index and isoelectric point were calculated as mentioned in the previous section and can be compared 
against AMP and non-AMP sets using Z-score as shown in the **Fig. 2d-f**.

The helical wheel (**Fig. 3**) is useful to illustrate the properties of alpha-helices, such as the concentration of 
hydrophobic amino acids on one side of the helix, with polar or hydrophilic amino acids on the other. 

<figure class="figure">
    <img style="float: center;" src="figures/helicalwheel_AMP10.000_000.png" width="300" height="300">
    <figcaption class="figure-caption">Fig. 3. Amino acids helical wheel with the hydrophobic moment indicated.</figcaption>
</figure>

<br/>The helical wheel is drawn in a rotating manner where the angle of rotation between consecutive amino acids is 100°.
This is usually found in globular proteins, where one face of the helix is oriented toward the hydrophobic core and 
the another is solvent-exposed. The H-moment and direction is shown inside the wheel pointing to its maximum. 
The function used in this graph as well as its color codes were taken from [modlAMP](https://doi.org/10.1093/bioinformatics/btx285).
The residues are colored by the amphipathic scale:

```
The amphipatic color code from modlAMP uses 8 colors:

G, A                        Beige
N, Q                        Purple
S, T                        Pink
K, R                        Blue
H                           Light blue
D, E                        Red bordeaux
P                           Green
F, L, W, M, V, I, C, Y      Yellow
```

**Figures 4-7** compute a profile by residues using a scanning with a fixed window size and different scale parameters.
An amino acid scale is a numerical value assigned to each type of amino acid according to some specific feature in which 
they are classified or measured. To make a profile we also can use sequence positions or even the amino acids sequence
colored by amino acids properties. In these figures we used the Lesk's color scale to code sequences in the X-axis
as follows:

```
The colour scheme from Lesk
It uses 5 groups (note Histidine): 

    Small nonpolar        G, A, S, T                    Orange
    Hydrophobic           C, V, I, L, P, F, Y, M, W     Green
    Polar                 N, Q, H                       Magenta
    Negatively charged    D, E                          Red
    Positively charged    K, R                          Blue
    
```

Similarly to the expasy’s [ProtScale](http://www.expasy.org/cgi-bin/protscale.pl), we set parameters for the
computation of a scale profile:

 + WindowSize:        The length of the interval to use for the profile computation.
                      For a window size n, we use the i-(n-1)/2 neighboring residues on each side to compute the score for residue i.
                      
 + Edge:              The central amino acid of the window always has a weight of 1.
                      By default, the amino acids at the remaining window positions have the same weight.
                       
The most frequently used scales are the hydrophobicity scales (**Fig. 4**) and the adopted by the AMPSphere was established by
[Parker et al. (1986)](https://pubmed.ncbi.nlm.nih.gov/2430611/). Parker is an experimental hydrophobicity scale derived by measuring
HPLC retention times of peptide libraries. It presents two adjacent copies of a variable residue in a random coil peptide, one more
exposed located toward the N-terminus of the peptide and one packed between the other copy of the residue and a Leucine residue
(Ac–GXXLLLKK–amide).

<figure class="figure">
    <img style="float: center;" src="figures/hydrophobicity_Parker_AMP10.000_000.png" width="500" height="300">
    <figcaption class="figure-caption">Fig. 4. Profile of hydrophobicity of residues of AMP10.000_000 using relative scale of Parker.</figcaption>
</figure>

<br/>This scale is interesting to understand whether hydrophobic or hydrophylic stretches are present in the peptide.
If the hydrophobicity is above 0.5, it is considered hydrophobic ([Pane et al., 2017](https://doi.org/10.1016/j.jtbi.2017.02.012)).

The profile of residues free energy of transfer from water to membrane lipid (Ez) in **Fig. 5** was conceived initially by 
[Senes et al. (2007)](https://pubmed.ncbi.nlm.nih.gov/17174324/). It is important for AMPs to have a low energy of transfer
allowing them to insert theirselves easily in the lipid membranes, triggiring their effects. The scale adopted in this graph
was adapted from [modlAMP](https://doi.org/10.1093/bioinformatics/btx285).
    
<figure class="figure">
    <img style="float: center;" src="figures/EZenergy_AMP10.000_000.png" width="500" height="300">
    <figcaption class="figure-caption">Fig. 5. Profile of AMP10.000_000 residues free energy of transfer from water to membrane lipid.</figcaption>
</figure>

<br/>The free energy of transfer was estimated as the by a reverse-Boltzman relationship of potential calculated from the 
propensities for occurrence of each residue as a function of depth in the lipid bilayer
[Senes et al. (2007)](https://pubmed.ncbi.nlm.nih.gov/17174324/).

Complementary to the hydrophobicity, the solvent accessibility (SA) can tell us which residues are exposed or buried,
as shown in **Fig. 6**. It is calculated using the Emini Surface fractional probability (EM) scale in the
[Bio.SeqUtils.ProtParam](https://biopython.org/wiki/ProtParam) module. The scale was proposed by
[Emini et al. (1987)](https://pubmed.ncbi.nlm.nih.gov/2991600/) based on the formulae:

```
  Sn = (n+4+i)*(0.37)-6
  
  where
        Sn is the surface probability of residue n
        dn is the fractional surface probability value of the amino acid n
        i vary from 1 to 6 depending of its position in the window
```

Values greater than 1.0 indicate an increased probability for being found on the surface.

<figure class="figure">
    <img style="float: center;" src="figures/SA_AMP10.000_000.png" width="500" height="300">
    <figcaption class="figure-caption:bold">Fig. 6. Profile of solvent accessibility of residues of AMP10.000_000.</figcaption>
</figure>

<br/>The calculated flexibility profile (**Fig. 7**) is important to show if regions submitted to higher free energies of transfer could
actually bend theirselves into a more favorable conformation. Other important conclusions could rise from flexibility and insights 
from the amino acids sequences trend to form secondary structures. Therefore, an accurate analysis of the peptide flexibility can lead
to valuable ideas of how the peptide can behave. The scale adopted in the profile calculation was obtained from normalized flexibility
parameters (B-values), average [Vihinen, 1994](https://onlinelibrary.wiley.com/doi/10.1002/prot.340190207) optimized to be used in a
fixed window of 9.

<figure class="figure">
    <img style="float: center;" src="figures/flexibility_AMP10.000_000.png" width="500" height="300">
    <figcaption class="figure-caption">Fig. 7. Profile of flexibility of residues of AMP10.000_000.</figcaption>
</figure>







