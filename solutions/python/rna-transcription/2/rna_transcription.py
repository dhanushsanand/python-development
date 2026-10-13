def to_rna(dna_strand:str):
    rna = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    rna_seq = ""
    for character in dna_strand:
        rna_seq += rna[character]
    return rna_seq