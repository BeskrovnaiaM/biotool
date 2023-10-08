import sys
import modules.dna_rna_tools as dr
import modules.protein_tool as p
import modules.fastqc_filter as f
from typing import Dict, List, Union


def fastqc_filter(seqs: dict, length_bounds: int = (0, 2**32), quality_threshold: int = 0, gc_bounds: int = (0,100)) -> dict:
    result = dict()
    filter_set = set(f.quality_filter(seqs, quality_threshold))&set(f.gc_filter(seqs, gc_bounds))&set(f.quality_filter(seqs, quality_threshold))&set(f.length_filter(seqs, length_bounds))
    for name, (sequence, quality) in seqs.items():
        if name in filter_set:
            result[name] = (sequence, quality)
    return result


def protein_tool(*args: str) -> Union[str, List[Union[Dict[str, int], str]]]:
    *seqs, operation = args
    operations = {'one letter': p.change_abbreviation, 'RNA': p.to_rna, 'DNA': p.to_dna, 'charge': p.define_charge, 'polarity': p.define_polarity}
    output = []
    for seq in seqs:
        answer = p.is_correct_seq(seq.upper())
        if answer:
            function_output = operations[operation](seq.upper())
            output.append(function_output)
        else:
            print(f'Something wrong with {seq}', file=sys.stderr)
        continue
    if len(output) == 1 and (operation == 'RNA' or operation == 'DNA' or operation == 'one letter'):
        return ''.join(output)
    else:
        return output


def dna_rna_tools(*args: str) -> Union[list, str]:
    *seqs, operation = args
    output = []
    operations = {
                'transcribe': dr.seq_transcribe, 'reverse': dr.seq_reverse, 'complement': dr.seq_complement, 
                'reverse_complement': dr.seq_reverse_complement
                }
    for seq in seqs:
        answer = dr.is_dna_or_rna(seq)
        if answer:
            new_seq = operations[operation](seq)
            output.append(new_seq)
        else:
          print(f'Something wrong with sequence {seq}', file=sys.stderr)
          continue
    if len(output) == 1:
      return ''.join(output)
    else:
      return output