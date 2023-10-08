def length_filter(seqs: dict, length_bounds: int = (0,2**32)) -> list:
    length_output = []
    for name, (sequence, quality) in seqs.items():
        if len(sequence) <= length_bounds[1] and len(sequence) >= length_bounds[0]:
            length_output.append(name)
    return length_output


def gc_filter(seqs: dict, gc_bounds: int = (0,100)) -> list:
    gc_output = []
    for name, (sequence, quality) in seqs.items():
        gc_nuc_count = 0
        for nuc in sequence:
            if nuc == 'G' or nuc == 'C':
                gc_nuc_count += 1
        gc_count = gc_nuc_count/len(sequence)*100
        if gc_count <= gc_bounds[1] and gc_count >= gc_bounds[0]:
            gc_output.append(name)
    return gc_output


def quality_filter(seqs: dict, quality_threshold: int = (0)) -> list:
    quality_output = []
    for name, (sequence, quality) in seqs.items():
        score_nuc_count = 0
        for score in quality:
            score_nuc_count += ord(score) - 33
        score_seq_count = score_nuc_count/len(sequence)
        if score_seq_count >= quality_threshold:
            quality_output.append(name)
    return quality_output