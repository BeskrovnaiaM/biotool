import os

def convert_fasta_to_dic(input_path: str) -> dict:
    seqs = dict()
    end_of_file = True
    with open(os.path.join(input_path)) as input_file:
        while end_of_file:
            name = input_file.readline()
            sequence = input_file.readline()
            comment = input_file.readline()
            quality = input_file.readline()
            name = name.strip()
            comment = comment.strip()
            sequence = sequence.strip()
            quality = quality.strip()
            if not name:
                end_of_file = False
            else:
                seqs[name] = (sequence, comment, quality)
    return seqs


def convert_dic_to_fasta(input_path: str, result_filter: dict, output_filename: None = None) -> None:
    out_dir = 'fastq_filtrator_results'
    if output_filename is None:
        output_filename = os.path.basename(input_path)
    output_path = os.path.join(out_dir, output_filename)
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    with open(os.path.join(output_path), mode = 'w') as output_file:
        for name, (sequence, comment, quality) in result_filter.items():
            output_file.write(name + '\n' + sequence + '\n'  + comment + '\n' + quality + '\n')


def length_filter(seqs: dict, length_bounds: int = (0,2**32)) -> list:
    length_output = []
    for name, (sequence, comment, quality) in seqs.items():
        if len(sequence) <= length_bounds[1] and len(sequence) >= length_bounds[0]:
            length_output.append(name)
    return length_output


def gc_filter(seqs: dict, gc_bounds: int = (0,100)) -> list:
    gc_output = []
    for name, (sequence, comment, quality) in seqs.items():
        gc_nuc_count = 0
        for nuc in sequence:
            if nuc == 'G' or nuc == 'C':
                gc_nuc_count += 1
        gc_count = gc_nuc_count / len(sequence)*100
        if gc_count <= gc_bounds[1] and gc_count >= gc_bounds[0]:
            gc_output.append(name)
    return gc_output


def quality_filter(seqs: dict, quality_threshold: int = (0)) -> list:
    quality_output = []
    for name, (sequence, comment, quality) in seqs.items():
        score_nuc_count = 0
        for score in quality:
            score_nuc_count += ord(score) - 33
        score_seq_count = score_nuc_count / len(sequence)
        if score_seq_count >= quality_threshold:
            quality_output.append(name)
    return quality_output