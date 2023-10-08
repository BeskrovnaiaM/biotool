# biotool
> Author: Margarita Beskrovnaia

Bioinformatics tool for processing DNA, protein and FASTQ sequences. This utility includes three main functions:
1) dna_rna_tools - for processing DNA and RNA sequences
2) protein_tool - for processing protein sequences
3) fastqc_filter - for filtering sequences from FASTQ files

## Table of Contents

- [Installation](#installation)
- [Functions](#functions)
  - [protein_tool](#protein_tool)
  - [dna_rna_tools](#dna_rna_tools)
  - [fastqc_filter](#fastqc_filter)

## Installation

You can clone this repository or download the source code. 

##### Requirements:

Python3

## Functions
Biotools.py contains three main functions for processing different types of data. The modules folder contains modules containing functions for processing requests for each of the main functions. If you want to call specific functions from these modules (why not?), you can use these functions, adding module's attributes to it (f for fastqc_filter, p for protein_tool, dr for dna_rna_tools), for example, `f.gc_filter()`,`p.to_dna()`, `dr.seq_reverse()`. Name's of function are given in subtitles for this purpose. 
### protein_tool
The program can process one or more amino acid sequences written in a one-letter format and also does not take into account the size of the input and output letters. Tool can work with amino acids which are mentioned in table below.
| One letter amino acid         | Three letter amino acid     |
|-------------------------------|-----------------------------|
| A                             |            Ala              |
| C                             |            Cys              |
| D                             |            Asp              |
| E                             |            Glu              |
| F                             |            Phe              |
| G                             |            Gly              |
| H                             |            His              |
| I                             |            Ile              |
| K                             |            Lys              |
| L                             |            Leu              |
| M                             |            Met              |
| N                             |            Asn              |
| P                             |            Pro              |
| Q                             |            Gln              |
| R                             |            Arg              |
| S                             |            Ser              |
| T                             |            Tre              |
| V                             |            Val              |
| W                             |            Trp              |
| Y                             |            Tyr              |
#### change_abbreviation(seq)
Name's operation: `one letter`.
Sequences are written in three-letter format, can be converted to one-letter format. Amino acids must be separeted by "-". 

- seq: Amino acid sequence (str).
- Returns: string of one-letter format of sequence or list of sequences.
##### Example:
```python
protein_tool('aLa-CyS', 'one letter') #input ignore letter's size
'AC'
protein_tool('Ala-Cys', 'Ala', 'one letter')
['AC', 'A']
```
#### to_dna
Name's operation: `DNA`.
Transforms aminoacid sequence to according DNA sequence. 

Arguments:
- sequence: aminoacid sequence to transform into DNA.

Returns:
- String of according DNA sequence.
##### Example:
```python
protein_tool('AsDr', 'DNA')
'GCN(TCN or AGY)GAYAGY'
protein_tool('YWNGAS', 'DNA')
'TAY(CGN or AGR)AAYGGNGCN(TCN or AGY)'
```
#### to_rna
Name's operation: `RNA`.
Translates an amino acid sequence into an RNA sequence. 

Arguments:
- seq: Amino acid sequence (str).
- rna_dict: Dictionary defining the correspondence of amino acids to RNA triplets (default, standard code).

Returns: 
- String or list of RNA sequences.
##### Example:
```python
protein_tool('FM', 'RNA')
'UUYAUG'
```
#### define_charge
Name's operation: `charge`.
Counts the number of amino acids with positive charge, negative charge, and neutral amino acids in the sequence. 

Arguments:
- seq: Amino acid sequence (string).
- positive_charge: List of amino acids with positive charge (default is ['R', 'K', 'H']).
- negative_charge: List of amino acids with negative charge (default is ['D', 'E']).

Returns: 
- Dictionary (or list of dictionaries) containing the counts of amino acids and their labels.

##### Example:
```python
protein_tool('ASDRKHDE', 'charge')
{'Positive': 3, 'Negative': 3, 'Neutral': 2}
```
#### define_polarity
Name's operation: `polarity`.
Counts polar and nonpolar aminoacids in sequence. 

Arguments:
- sequence: sequence in which we count polar and nonpolar aminoacids. \newline

Returns:
- Dictionary with keys 'Polar', 'Nonpolar' and appropriate aminoacid counters as values.
##### Example:
```python
protein_tool('ASDR', 'polarity')
[{'Polar': 3, 'Nonpolar': 1}]
```
#### Troubleshooting
Sequences containing characters that do not code for amino acids will be removed from the analysis. The program will write an error and display the sequence with which the problem occurred.
##### Example:
```python
protein_tool('ASDR', 'ala1', 'polarity')
Something wrong with ala1
[{'Polar': 3, 'Nonpolar': 1}]
```
Sequences specified in a three-letter format are accepted only by the function for changing the recording format. In other cases, the program will produce either an error or incorrect calculations.
##### Example:
```python
protein_tool('AGFHGF', 'Ala-ala', 'DNA') # key error "-"
protein_tool('AGFHGF', 'Ala-ala', 'polarity')
[{'Polar': 1, 'Nonpolar': 5}, {'Polar': 0, 'Nonpolar': 7}] # "-" is counted as non-polar
```
### dna_rna_tools

This utility was created to work with sequences of nucleic acids. It can take several sequences to the input and perform the procedures described below. The program preserves the symbol register (exp. **complement AtGc** - **TaCg**).

#### seq_transcribe

Name's operation: `transcribe` — print a transcribed sequence. If a sequence is given to the input of the RNA, it will report this. 

Arguments:

- sequence: DNA sequence, str.

Returns:

- transcribed sequence, str.
##### Example:
 ```python
dna_rna_tools('ATG', 'transcribe')
'AUG'
dna_rna_tools('AUG', 'transcribe') # 'You have already RNA sequence'
```
#### seq_reverse
Name's operation: `reverse` — print reverse sequence.

Arguments:

- sequence: DNA/RNA sequence, str.

Returns:

- reversed DNA/RNA sequence, str.
##### Example:
```python
run_dna_rna_tools('ATG', 'reverse')
'GTA'
```
#### seq_complement
Name's operation: `complement` — print complemenatry sequence.

Arguments:

- sequence: DNA/RNA sequence, str.

Returns:

- complementary DNA/RNA sequence, str.
##### Example:
```python
run_dna_rna_tools('AtG', 'complement')
'TaC'
```
#### seq_reverse_complement
Name's operation: `reverse_complement` — print the reverse complementary sequence.

Arguments:

- sequence: DNA/RNA sequence, str.

Returns:

- reversed complementary DNA/RNA sequence, str.
##### Example:
```python
run_dna_rna_tools('ATg', 'reverse_complement')
'cAT'
```
If the sequence cannot be defined as RNA or DNA, the program will report this.
##### Example:
```python
run_dna_rna_tools('ATug', 'reverse_complement')
'Something wrong with sequence'
```
You can analyze several sequences at once.
##### Example:
```python
run_dna_rna_tools('ATG', 'aT', 'reverse')
['GTA', 'Ta']
run_dna_rna_tools('aut', 'ATGC', 'transcribe')
Something wrong with sequence aut
'AUGC'
```
### fastqc_filter

The function can take a dictionary from sequences to the input and filter them in terms of the quality of reads, length and GC content. You can set the necessary value for the filter, if this parameter is not indicated, then the filter will work on default values:
1) `gc_bounds` = (0,100) 
2) `quality_threshold` = 0
3) `length_bounds` = (0, 2**32)

Arguments:

- dict of FASTQ. All examples of functions working will be proceed with EXAMPLE_FASTQC.
##### Example:
```python
EXAMPLE_FASTQ = {
    # 'name' : ('sequence', 'quality')
    '@SRX079804:1:SRR292678:1:1101:21885:21885': ('ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA', 'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD'),
    '@SRX079804:1:SRR292678:1:1101:24563:24563': ('ATTAGCGAGGAGGAGTGCTGAGAAGATGTCGCCTACGCCGTTGAAATTCCCTTCAATCAGGGGGTACTGGAGGATACGAGTTTGTGTG', 'BFFFFFFFB@B@A<@D>BDDACDDDEBEDEFFFBFFFEFFDFFF=CC@DDFD8FFFFFFF8/+.2,@7<<:?B/:<><-><@.A*C>D'),
    '@SRX079804:1:SRR292678:1:1101:30161:30161': ('GAACGACAGCAGCTCCTGCATAACCGCGTCCTTCTTCTTTAGCGTTGTGCAAAGCATGTTTTGTATTACGGGCATCTCGAGCGAATC', 'DFFFEGDGGGGFGGEDCCDCEFFFFCCCCCB>CEBFGFBGGG?DE=:6@=>A<A>D?D8DCEE:>EEABE5D@5:DDCA;EEE-DCD'),
    '@SRX079804:1:SRR292678:1:1101:47176:47176': ('TGAAGCGTCGATAGAAGTTAGCAAACCCGCGGAACTTCCGTACATCAGACACATTCCGGGGGGTGGGCCAATCCATGATGCCTTTG', 'FF@FFBEEEEFFEFFD@EDEFFB=DFEEFFFE8FFE8EEDBFDFEEBE+E<C<C@FFFFF;;338<??D:@=DD:8DDDD@EE?EB'),
    '@SRX079804:1:SRR292678:1:1101:149302:149302': ('TAGGGTTGTATTTGCAGATCCATGGCATGCCAAAAAGAACATCGTCCCGTCCAATATCTGCAACATACCAGTTGGTTGGTA', '@;CBA=:@;@DBDCDEEE/EEEEEEF@>FBEEB=EFA>EEBD=DAEEEEB9)99>B99BC)@,@<9CDD=C,5;B::?@;A'),
    '@SRX079804:1:SRR292678:1:1101:170868:170868': ('CTGCCGAGACTGTTCTCAGACATGGAAAGCTCGATTCGCATACACTCGCTGAGTAAGAGAGTCACACCAAATCACAGATT', 'E;FFFEGFGIGGFBG;C6D<@C7CDGFEFGFHDFEHHHBBHHFDFEFBAEEEEDE@A2=DA:??C3<BCA7@DCDEG*EB'),
    '@SRX079804:1:SRR292678:1:1101:171075:171075': ('CATTATAGTAATACGGAAGATGACTTGCTGTTATCATTACAGCTCCATCGCATGAATAATTCTCTAATATAGTTGTCAT', 'HGHHHHGFHHHHFHHEHHHHFGEHFGFGGGHHEEGHHEEHBHHFGDDECEGGGEFGF<FGGIIGEBGDFFFGFFGGFGF'),
    '@SRX079804:1:SRR292678:1:1101:175500:175500': ('GACGCCGTGGCTGCACTATTTGAGGCACCTGTCCTCGAAGGGAAGTTCATCTCGACGCGTGTCACTATGACATGAATG', 'GGGGGFFCFEEEFFDGFBGGGA5DG@5DDCBDDE=GFADDFF5BE49<<<BDD?CE<A<8:59;@C.C9CECBAC=DE'),
    '@SRX079804:1:SRR292678:1:1101:190136:190136': ('GAACCTTCTTTAATTTATCTAGAGCCCAAATTTTAGTCAATCTATCAACTAAAATACCTACTGCTACTACAAGTATT', 'DACD@BEECEDE.BEDDDDD,>:@>EEBEEHEFEHHFFHH?FGBGFBBD77B;;C?FFFFGGFED.BBABBG@DBBE'),
    '@SRX079804:1:SRR292678:1:1101:190845:190845': ('CCTCAGCGTGGATTGCCGCTCATGCAGGAGCAGATAATCCCTTCGCCATCCCATTAAGCGCCGTTGTCGGTATTCC', 'FF@FFCFEECEBEC@@BBBBDFBBFFDFFEFFEB8FFFFFFFFEFCEB/>BBA@AFFFEEEEECE;ACD@DBBEEE'),
    '@SRX079804:1:SRR292678:1:1101:198993:198993': ('AGTTATTTATGCATCATTCTCATGTATGAGCCAACAAGATAGTACAAGTTTTATTGCTATGAGTTCAGTACAACA', '<<<=;@B??@<>@><48876EADEG6B<A@*;398@.=BB<7:>.BB@.?+98204<:<>@?A=@EFEFFFEEFB'),
    '@SRX079804:1:SRR292678:1:1101:204480:204480': ('AGTGAGACACCCCTGAACATTCCTAGTAAGACATCTTTGAATATTACTAGTTAGCCACACTTTAAAATGACCCG', '<98;<@@@:@CD@BCCDD=DBBCEBBAAA@9???@BCDBCGF=GEGDFGDBEEEEEFFFF=EDEE=DCD@@BBC')
    }
```
Returns:
- dict of sequences
##### Example with default values
```python
fastqc_filter(EXAMPLE_FASTQ) #return all seq from EXAMPLE_FASTQ
```
##### Example with custom quality_filter
```python
fastqc_filter(EXAMPLE_FASTQ, quality_threshold=(34))
{'@SRX079804:1:SRR292678:1:1101:21885:21885': ('ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA',
  'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD'),
 '@SRX079804:1:SRR292678:1:1101:171075:171075': ('CATTATAGTAATACGGAAGATGACTTGCTGTTATCATTACAGCTCCATCGCATGAATAATTCTCTAATATAGTTGTCAT',
  'HGHHHHGFHHHHFHHEHHHHFGEHFGFGGGHHEEGHHEEHBHHFGDDECEGGGEFGF<FGGIIGEBGDFFFGFFGGFGF'),
 '@SRX079804:1:SRR292678:1:1101:190845:190845': ('CCTCAGCGTGGATTGCCGCTCATGCAGGAGCAGATAATCCCTTCGCCATCCCATTAAGCGCCGTTGTCGGTATTCC',
  'FF@FFCFEECEBEC@@BBBBDFBBFFDFFEFFEB8FFFFFFFFEFCEB/>BBA@AFFFEEEEECE;ACD@DBBEEE')}
```
##### Example with custom length_filter
```python
fastqc_filter(EXAMPLE_FASTQ, length_bounds=(0,77))
{'@SRX079804:1:SRR292678:1:1101:190136:190136': ('GAACCTTCTTTAATTTATCTAGAGCCCAAATTTTAGTCAATCTATCAACTAAAATACCTACTGCTACTACAAGTATT',
  'DACD@BEECEDE.BEDDDDD,>:@>EEBEEHEFEHHFFHH?FGBGFBBD77B;;C?FFFFGGFED.BBABBG@DBBE'),
 '@SRX079804:1:SRR292678:1:1101:190845:190845': ('CCTCAGCGTGGATTGCCGCTCATGCAGGAGCAGATAATCCCTTCGCCATCCCATTAAGCGCCGTTGTCGGTATTCC',
  'FF@FFCFEECEBEC@@BBBBDFBBFFDFFEFFEB8FFFFFFFFEFCEB/>BBA@AFFFEEEEECE;ACD@DBBEEE'),
 '@SRX079804:1:SRR292678:1:1101:198993:198993': ('AGTTATTTATGCATCATTCTCATGTATGAGCCAACAAGATAGTACAAGTTTTATTGCTATGAGTTCAGTACAACA',
  '<<<=;@B??@<>@><48876EADEG6B<A@*;398@.=BB<7:>.BB@.?+98204<:<>@?A=@EFEFFFEEFB'),
 '@SRX079804:1:SRR292678:1:1101:204480:204480': ('AGTGAGACACCCCTGAACATTCCTAGTAAGACATCTTTGAATATTACTAGTTAGCCACACTTTAAAATGACCCG',
  '<98;<@@@:@CD@BCCDD=DBBCEBBAAA@9???@BCDBCGF=GEGDFGDBEEEEEFFFF=EDEE=DCD@@BBC')}
```

##### Example with custom gc_filter
```python
fastqc_filter(EXAMPLE_FASTQ, gc_bounds=(0,30))
{'@SRX079804:1:SRR292678:1:1101:190136:190136': ('GAACCTTCTTTAATTTATCTAGAGCCCAAATTTTAGTCAATCTATCAACTAAAATACCTACTGCTACTACAAGTATT',
  'DACD@BEECEDE.BEDDDDD,>:@>EEBEEHEFEHHFFHH?FGBGFBBD77B;;C?FFFFGGFED.BBABBG@DBBE')}
```
##### Example with custom gc_filter and length_filter
```python
fastqc_filter(EXAMPLE_FASTQ, gc_bounds=(0,35), length_bounds=(0,75))
{'@SRX079804:1:SRR292678:1:1101:198993:198993': ('AGTTATTTATGCATCATTCTCATGTATGAGCCAACAAGATAGTACAAGTTTTATTGCTATGAGTTCAGTACAACA',
  '<<<=;@B??@<>@><48876EADEG6B<A@*;398@.=BB<7:>.BB@.?+98204<:<>@?A=@EFEFFFEEFB')}
```
