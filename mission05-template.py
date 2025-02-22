# CS1010S --- Programming Methodology
# Mission 5

# Note that written answers are stored in """multi-line strings"""
# to allow us to run your code easily when grading your problem set.

import csv

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows


##########
# Task 1 #
##########

def replicate(dna_strand):
    dna_base_pairings = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    dna_strand = dna_strand[: : -1]
    c_strand = ""
    for base in dna_strand:
        c_strand += dna_base_pairings[base]
    return c_strand

##########
# Task 2 #
##########

def transcribe(dna_strand):
    dna_strand = dna_strand[: : -1]
    t_strand = ""
    for base in dna_strand:
        if base == "A":
            t_strand += "U"
        elif base == "T":
            t_strand += "A"
        elif base == "G":
            t_strand += "C"
        elif base == "C":
            t_strand += "G"
    return t_strand

def reverse_transcribe(rna_strand):
    rna_strand = rna_strand[: : -1]
    reversed_t_strand = ""
    for base in rna_strand:
        if base == "A":
            reversed_t_strand += "T"
        elif base == "U":
            reversed_t_strand += "A"
        elif base == "G":
            reversed_t_strand += "C"
        elif base == "C":
            reversed_t_strand += "G"
    return reversed_t_strand


# UNCOMMENT THE CODE BELOW AFTER YOU ARE DONE WITH TASK 2. THIS IS NOT OPTIONAL TESTING #
with open("dna.txt") as f:
    dna = f.read()
rna = transcribe(dna)

# print("## Q2 ##")
# print(rna[0:10:1]) # 'AAUAGUUUCU'
# print(transcribe("AAATGC")) # 'GCAUUU'
# print(transcribe("ATTGGGCCCC")) # 'GGGGCCCAAU'
# print(reverse_transcribe(transcribe("AAATGC"))) # 'AAATGC'
# print(reverse_transcribe("GGGGCCCAAU")) # 'ATTGGGCCCC'


##########
# Task 3 #
##########

def get_mapping(csv_filename):
    data = read_csv(csv_filename)[1:]
    dictionary = {}
    for row in data:
        dictionary[row[0]] = row[3]
    return dictionary


# UNCOMMENT THE CODE BELOW AFTER YOU ARE DONE WITH TASK 3. THIS IS NOT OPTIONAL TESTING #
codon2amino = get_mapping("codon_mapping.csv")

# print("## Q3 ##")
# print(codon2amino["ACA"]) # 'T'
# print(codon2amino["AUU"]) # 'I'
# print(codon2amino["CUC"]) # 'L'
# print(codon2amino["ACU"]) # 'T'
# print(codon2amino["UAG"]) # '_'
# print(codon2amino["UGA"]) # '_'


##########
# Task 4 #
##########

def translate(rna_strand):
    codon2amino = get_mapping("codon_mapping.csv")
    protein = ""
    if "AUG" in rna_strand:
        start_index = rna_strand.index("AUG")
    else:
        return None
    
    temp_rna_strand = rna_strand[start_index + 3:]
    stop_codons = ["UAA", "UAG", "UGA"]
    stop_index = None
    for i in range(start_index, len(rna_strand), 3):
        codon = rna_strand[i:i + 3]
        if codon in stop_codons:
            stop_index = i
            break
    
    if stop_index is None:
        return None 
        
    rna_strand = rna_strand[start_index:stop_index + 3]
    while len(rna_strand) >= 3:
        protein += codon2amino[rna_strand[:3]]
        rna_strand = rna_strand[3:]
    return protein

# print("## Q4 ##")
# print(translate("AUGUAA"))           # 'M_'
# print(translate("AGAGAUGCCCUGAGGG")) # 'MP_'
# protein = translate(rna)
# print(protein) # 'MANLTNFHLKIYIHTYIQLKHLSSGAFSLFSAHNSRSINYNYYFSFRDLNITYNHTHLTTY_'
