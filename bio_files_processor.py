def convert_multiline_fasta_to_oneline(input_fasta: str, output_fasta: str = None) -> None:
    list_of_seqlines = []
    out_dir = 'files_processor_results'
    if output_fasta is None:
        output_fasta = os.path.basename(input_fasta)
        output_path = os.path.join(out_dir, output_fasta)
    else:
        output_filename = output_fasta + '.fasta'
        output_path = os.path.join(out_dir, output_filename)
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    with open(os.path.join(input_fasta)) as input_file:
        for line in input_file:
            if not line.startswith('>'):
                line = line.strip()
                list_of_seqlines.append(line)            
    oneline_seqs = ''.join(list_of_seqlines)
    with open(os.path.join(output_path), mode = 'w') as output_file:
        output_file.write(oneline_seqs)