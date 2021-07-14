# Help with the AMP cards

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

These results are obtained using ProtParam including the molecular weight, theoretical pI, instability index, aliphatic index and grand average of hydropathicity (GRAVY).

The molar extinction comes from the Lambert-Beer law and indicates how much light a protein absorbs at a given wavelength. This can be used to the determination of the protein concentration in a given solution from its absorbance. The molar extinction coefficient takes in consideration the contents of specific amino acids in the native protein in water, specially tyrosine, tryptophan and cystine (because cysteine does not absorb light considerably at wavelengths >260 nm). Protein extinction coefficients used the Edelhoch method ([Edelhoch (1967)](https://pubmed.ncbi.nlm.nih.gov/6049437/)), with the extinction coefficients for Trp and Tyr determined by [Pace et al. (1995)](https://pubmed.ncbi.nlm.nih.gov/8563639/). The calculus can be simplified by:

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

Two values are produced by ProtParam, one assuming all cysteine residues appear as half cystines, and the second assuming that no cysteine appears as half cystine.

The aromaticity is calculated as described by [Lobry, 1994]() and is the relative frequency of Phe + Trp + Tyr.

The Grand Average of Hydropathy (GRAVY) value for a peptide or protein is calculated as in [Kyte and Doolittle (1982)](https://pubmed.ncbi.nlm.nih.gov/7108955/). It consists in the sum of hydropathy values of each residues in the peptide and divided by the total length of the sequence.

The instability index (II) is an estimate of the peptide stability in a test tube at 4°C. This technique considers the statistical analysis of 12 unstable and 32 stable proteins ([Guruprasad, et al. 1990](https://pubmed.ncbi.nlm.nih.gov/2075190/)). The analysis revealed certain dipeptides significantly happening in the unstable proteins when compared with stable ones. Then, it was assigned a weight value of instability to each of the 400 different dipeptides (DIWV). Therefore, the II is defined as:


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

Protein isoelectric point (pI) is calculated using pK values of amino acids described in Bjellqvist et al.([1993](https://pubmed.ncbi.nlm.nih.gov/8125050/) and [1994](https://pubmed.ncbi.nlm.nih.gov/8055880/)) under pH 7.0 at 25°C. Molecular weight (MW) values are given in x10^3 Daltons (kDa). This MW is obtained by adding the average isotopic masses of amino acids in the protein and the mass of one water molecule.

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

Be aware that:

 + Prediction of protein pI for highly basic proteins is yet to be studied and possibly the current predictions may not be adequate.
 + pI predictions for small proteins can be problematic.
 + It is not taken in account the effects of post-translational modifications.
 + The molar extinction calculus assumes that no [other] chromophores that absorb at 280 nm are present in the protein.
 + Molar extinction can have more than 10% error for proteins without Trp residues.
