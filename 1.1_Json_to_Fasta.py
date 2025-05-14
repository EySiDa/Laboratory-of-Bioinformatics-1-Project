from sys import argv
import json

def make_fasta(file):
    with open(file, "r") as x:
        data = json.load(x)

    with open("OUTPUT_FASTA_NAME", "w") as output:
        for item in data:
            d = item.get("data", {})
            ids = d.get("rcsb_entry_container_identifiers", {})
            pdb_id = ids.get("entry_id")
            polymers = d.get("polymer_entities", [])
            if pdb_id and polymers:
                for polymer in polymers:
                    seq = polymer.get("entity_poly", {}).get("pdbx_seq_one_letter_code_can")
                    for inst in polymer.get("polymer_entity_instances", []):
                        chain = inst.get("rcsb_polymer_entity_instance_container_identifiers", {}).get("auth_asym_id")
                        if seq and chain:
                            output.write(f">{pdb_id}_{chain}\n{seq}\n")

if __name__ == "__main__":
    if len(argv) >= 2:
        make_fasta(argv[1])

