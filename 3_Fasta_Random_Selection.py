import random
from Bio import SeqIO
import sys

def select_random(file):
    # Open the input fasta file and read all sequences
    records = list(SeqIO.parse(file, "fasta"))
    
    # Number of sequences to sample, hardcoded for simplicity
    sample_count = 105
    
    # Select random sequences - make sure we don't sample more than available records
    if sample_count > len(records):
        sample_count = len(records)
    
    sampled = random.sample(records, sample_count)
    
    # Write the sampled sequences to a new fasta file
    output_file = "test001final.fasta"
    with open(output_file, "w") as out:
        SeqIO.write(sampled, out, "fasta")
    
    print("Sampled sequences written to", output_file)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        input_file = sys.argv[1]
        select_random(input_file)

