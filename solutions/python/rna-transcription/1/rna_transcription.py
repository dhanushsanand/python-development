def to_rna(dna_strand:str):
    list_dna = list(dna_strand)
    for i in range(len(list_dna)):
        if list_dna[i] == 'G':
            list_dna[i] = 'C'
        elif list_dna[i] == 'C':
            list_dna[i] = 'G'
        elif list_dna[i] == 'T':
            list_dna[i] = 'A'
        elif list_dna[i] == 'A':
            list_dna[i] = 'U'
    return "".join(list_dna)
