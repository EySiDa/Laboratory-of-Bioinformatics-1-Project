from sys import argv #allows for script to accept command line arguments
import json

def make_fasta(file):
    with open(file, "r") as x: #opens JSON file in read mode and assigns the file object to x
        data = json.load(x)

    with open("OUTPUT_FASTA_NAME", "w") as output: #creates a file named "OUTPUT_FASTA_NAME"
        for item in data:
            d = item.get("data", {})
            ids = d.get("rcsb_entry_container_identifiers", {}) # retrieves the identifiers for the entry
            pdb_id = ids.get("entry_id") #extracts the PDB ID from the identifiers
            polymers = d.get("polymer_entities", []) #retrieves a list of polymer entities
            if pdb_id and polymers:
                for polymer in polymers:
                    seq = polymer.get("entity_poly", {}).get("pdbx_seq_one_letter_code_can") #retrieves the sequence of the polymer in one-letter code format
                    for inst in polymer.get("polymer_entity_instances", []):
                        chain = inst.get("rcsb_polymer_entity_instance_container_identifiers", {}).get("auth_asym_id") #retrieves the chain identifier for the polymer instance
                        if seq and chain:
                            output.write(f">{pdb_id}_{chain}\n{seq}\n")

if __name__ == "__main__": #checks script is being run directly
    if len(argv) >= 2:
        make_fasta(argv[1])

