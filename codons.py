import os
path = "data/codons.txt"
with open(path, "r", encoding="utf-8") as f:
    rows = f.readlines()

f.close()

def create_codon_dict(file_path):
  codon_dict = {}
  with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            codon = parts[0].upper()
            amino_acid = " ".join(parts[1:]) 
            codon_dict[codon] = amino_acid
  return codon_dict

create_codon_dict(path)


def test_create_codon_dict():
    result = create_codon_dict("data/codons.txt")

    assert result['AAA'] == 'K', "Test Failed: 'AAA' should map to 'K'"
    assert result['AAC'] == 'N', "Test Failed: 'AAC' should map to 'N'"
    assert result['ACA'] == 'T', "Test Failed: 'ACA' should map to 'T'"
    assert result['ACC'] == 'T', "Test Failed: 'ACC' should map to 'T'"

    print("All tests passed successfully.")

test_create_codon_dict()
