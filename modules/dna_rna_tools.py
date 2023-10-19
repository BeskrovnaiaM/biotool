RNA_COMP = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G', 'a': 'u', 'u': 'a' ,'g': 'c', 'c': 'g'}
DNA_COMP = {'A':'T', 'T': 'A', 'G': 'C', 'C': 'G', 'a': 't', 't': 'a', 'g': 'c', 'c': 'g'}
NUC_FOR_DNA = {'A','T','G','C','a','t','g','c'}
NUC_FOR_RNA = {'A','U','G','C','a','u','g','c'}



def seq_transcribe(seq: str) -> str:
    unique_char_seq = set(seq)
    if 'U' in unique_char_seq or 'u' in unique_char_seq:
        print('You have already RNA sequence', file=sys.stdout)
        return seq
    else:
        return seq.replace('T','U').replace('t','u')


def seq_reverse(seq: str) -> str:
    return seq[::-1]


def seq_complement(seq: str) -> str:
    seq_list = list(seq)
    unique_char_seq = set(seq_list)
    comp_seq = []
    unique_char_seq = set(seq)
    if 'U' in unique_char_seq or 'u' in unique_char_seq:
        comp_seq = [RNA_COMP[nuc] for nuc in seq]
    else:
        comp_seq = [DNA_COMP[nuc] for nuc in seq]
    return ''.join(comp_seq)


def seq_reverse_complement(seq: str) -> str:
    return seq_complement(seq_reverse(seq))


def is_dna_or_rna(seq: str) -> bool:
    unique_char_seq = set(seq)
    return unique_char_seq <= NUC_FOR_DNA or unique_char_seq <= NUC_FOR_RNA