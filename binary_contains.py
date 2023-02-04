def binary_contains(gene, key_codon):
    low = 0
    high = len(gene) - 1
    while low <= high:
        mid = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False
