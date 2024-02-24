import sys
import os
from typing import Dict, List, Union

import modules.dna_rna_tools as dna_rna
import modules.protein_tool as protein
import modules.fastqc_filter as fasta



def fastqc_filter(input_path: str, output_filename: None = None, 
                  length_bounds: int = (0, 2**32), quality_threshold: int = 0, 
                  gc_bounds: int = (0,100)) -> None:
    result_filter = dict()
    seqs = fasta.convert_fasta_to_dic(input_path)
    filter_set = set(set(fasta.gc_filter(seqs, gc_bounds))&set(fasta.quality_filter(seqs, quality_threshold))&set(fasta.length_filter(seqs, length_bounds)))
    for name, (sequence, comment, quality) in seqs.items():
        if name in filter_set:
            result_filter[name] = (sequence, comment, quality)
    fasta.convert_dic_to_fasta(input_path, result_filter, output_filename)


def protein_tool(*args: str) -> Union[str, List[Union[Dict[str, int], str]]]:
    *seqs, operation = args
    operations = {
                   'one letter': protein.change_abbreviation, 'RNA': protein.to_rna, 'DNA': protein.to_dna, 
                   'charge': protein.define_charge, 'polarity': protein.define_polarity
                 }
    output = []
    for seq in seqs:
        answer = protein.is_correct_seq(seq.upper())
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
                'transcribe': dna_rna.seq_transcribe, 'reverse': dna_rna.seq_reverse, 'complement': dna_rna.seq_complement, 
                'reverse_complement': dna_rna.seq_reverse_complement
                }
    for seq in seqs:
        answer = dna_rna.is_dna_or_rna(seq)
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