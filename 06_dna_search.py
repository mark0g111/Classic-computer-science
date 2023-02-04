from enum import IntEnum
from typing import Tuple, List

from binary_contains import binary_contains
from linear_contains import linear_contains

Nucleotide = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

gene_str = 'ACGTGGCTCTCTAACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT'


def string_to_gene(s):
    gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            return gene
        codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)
    return gene


if __name__ == '__main__':
    acg = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
    gat = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
    my_gene = string_to_gene(gene_str)

    print(linear_contains(my_gene, acg))
    print(linear_contains(my_gene, gat))

    my_sorted_gene = sorted(my_gene)
    print(binary_contains(my_sorted_gene, acg))
    print(binary_contains(my_sorted_gene, gat))
