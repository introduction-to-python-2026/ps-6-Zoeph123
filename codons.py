def create_codon_dict(file_path):
    codon_dict = {}

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            codon = parts[0]
            amino_acid = " ".join(parts[1:])

            codon_dict[codon] = amino_acid

    return codon_dict

codons = create_codon_dict("data/codons.txt")
