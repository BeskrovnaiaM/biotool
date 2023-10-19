from typing import Dict, List, Union

RNA_DICT = {'F': 'UUY', 'L': 'YUN', 'I': 'AUH', 'M': 'AUG',
            'V': 'GUN', 'S': 'WSN', 'P': 'CCN', 'T': 'ACN',
            'A': 'GCN', 'Y': 'UAY', 'H': 'CAY', 'Q': 'CAR',
            'N': 'AAY', 'K': 'AAR', 'D': 'GAY', 'E': 'GAR',
            'C': 'UGY', 'R': 'MGN', 'G': 'GGN', 'W': 'UGG'}
POLAR_AA = {'D', 'E', 'R', 'K', 'H', 'N', 'Q', 'S', 'T', 'Y', 'C'}
NONPOLAR_AA = {'A', 'G', 'V', 'L', 'I', 'P', 'F', 'M', 'W'}
DNA_AA = {'F': 'TTY', 'L': '(TTR or CTN)', 'I': 'ATH', 'M': 'ATG', 'V': 'GTN', 'S': '(TCN or AGY)', 'P': 'CCN', 'T': 'ACN', 'A': 'GCN',
          'Y': 'TAY', 'H': 'CAY', 'Q': 'CAR', 'N': 'AAY', 'K': 'AAR', 'D': 'GAY', 'E': 'GAR', 'C': 'TGY', 'W': '(CGN or AGR)', 'R': 'AGY', 'G': 'GGN'}
ABBREVIATION_THREE_TO_ONE = {'ALA':'A', 'CYS':'C', 'ASP':'D', 'GLU':'E', 'PHE':'F',
                             'GLY':'G', 'HIS':'H', 'ILE':'I', 'LYS':'K', 'LEU':'L',
                             'MET':'M', 'ASN':'N', 'PRO':'P', 'GLN':'Q', 'ARG':'R',
                             'SER':'S', 'TRE':'T', 'VAL':'V', 'TRP':'W', 'TYR':'Y'}
AMINO_ACIDS_ONE_LETTER = POLAR_AA.union(NONPOLAR_AA)
AMINO_ACIDS_THREE_LETTER = {'ALA', 'CYS', 'ASP', 'GLU', 'PHE',
                             'GLY', 'HIS', 'ILE', 'LYS', 'LEU',
                             'MET', 'ASN', 'PRO', 'GLN', 'ARG',
                             'SER', 'TRE', 'VAL', 'TRP', 'TYR'}
POSITIVE_CHARGE = ['R', 'K', 'H'],
NEGATIVE_CHARGE = ['D', 'E']


def to_rna(seq: str) -> str:
    result = ''.join(RNA_DICT[base] for base in seq)
    return result


def define_charge(seq: str) -> Dict[str, int]:
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    for aa in seq:
        if aa in POSITIVE_CHARGE:
            positive_count += 1
        elif aa in NEGATIVE_CHARGE:
            negative_count += 1
        else:
            neutral_count += 1
    result = {
        'Positive': positive_count,
        'Negative': negative_count,
        'Neutral': neutral_count
    }
    return result


def define_polarity(seq: str) -> Dict[str, int]:
    polarity_count = {'Polar': 0, 'Nonpolar': 0}
    for aminoacid in seq:
        if aminoacid in POLAR_AA:
            polarity_count['Polar'] += 1
        else:
            polarity_count['Nonpolar'] += 1
    return polarity_count


def to_dna(seq: str) -> str:
    sequence_dna = []
    for aminoacid in seq:
        sequence_dna.append(DNA_AA[aminoacid])
    return ''.join(sequence_dna)


def change_abbreviation(seq: str) -> str:
    one_letter_seq = [ABBREVIATION_THREE_TO_ONE[amino_acid] for amino_acid in seq.split("-")]
    return "".join(one_letter_seq)


def is_correct_seq(seq: str) -> bool:
    unique_amino_acids = set(seq)
    unique_amino_acids_three = set(seq.split("-"))
    check = unique_amino_acids <= AMINO_ACIDS_ONE_LETTER or unique_amino_acids_three <= AMINO_ACIDS_THREE_LETTER
    return check