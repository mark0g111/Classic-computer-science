def linear_contains(gene, key_codon):
    for codon in gene:
        if codon == key_codon:
            return True
    return False
