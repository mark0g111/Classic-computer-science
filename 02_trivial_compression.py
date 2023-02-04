class CompressedGene:
    def __init__(self, gene):
        self.gene = gene

    def compress(self):
        self.bit_string = 1  # начальная метка
        for nucleotide in self.gene.upper():
            self.bit_string <<= 2  # сдвиг влево на 2 бита
            if nucleotide == "А":  # поменять 2 последних бита на 00
                self.bit_string |= 0b00
            elif nucleotide == "С":  # поменять 2 последних бита на 01
                self.bit_string |= 0b01
            elif nucleotide == "G":  # поменять 2 последних бита на 10
                self.bit_string |= 0b10
            elif nucleotide == "Т":  # поменять 2 последних бита на 11
                self.bit_string |= 0b11
            # else:
            #     raise ValueError("Invalid Nucleotide:{}".format(nucleotide))
        return self.bit_string

    def decompress(self):
        gene = ''

        for i in range(0, self.bit_string.bit_length() - 1, 2):
            # -1 чтобы исключить метку
            bits: int = self.bit_string >> i & 0b11
            # получить только 2 значимых бита
            if bits == 0b00:  # А
                gene += "А"
            elif bits == 0b01:  # с
                gene += "С"
            elif bits == 0b10:  # G
                gene += "G"
            elif bits == 0b11:  # т
                gene += "Т"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]  # [::-1] обращение строки посредством обратных срезов

    def __str__(self):
        # представление строки в виде красивого вывода
        return self.decompress()


if __name__ == '__main__':
    compressed = CompressedGene('AGGCTAAACG')
    print(compressed.compress())
    print(compressed)
