def to_rna(dna_strand):
    if len(dna_strand) == 0:
        return ""
    rna = ""
    for char in dna_strand:
        if char == "G":
            rna += "C"
        elif char == "C":
            rna += "G"
        elif char == "T":
            rna += "A"
        elif char == "A":
            rna += "U"
    return rna
