from monty.serialization import loadfn
import json
from ase import Atoms
from ase.io import write
import numpy as np

def decode_ndarray(data):
    dtype = data['__ndarray__'][1]
    values = np.array(data['__ndarray__'][2], dtype=dtype)
    return values.reshape(data['__ndarray__'][0])

def init_ase_atoms_from_dict(doc):
    decoded_data = json.loads(doc['atoms']['atoms_json'])
    numbers = decode_ndarray(decoded_data['numbers'])
    positions = decode_ndarray(decoded_data['positions'])
    charges = decode_ndarray(decoded_data['initial_charges'])
    magmoms = decode_ndarray(decoded_data['initial_magmoms'])
    cell = decode_ndarray(decoded_data['cell'])
    pbc = decode_ndarray(decoded_data['pbc'])
    # Initialize the ASE Atoms object
    atoms = Atoms(numbers=numbers, positions=positions, charges=charges, magmoms=magmoms, cell=cell, pbc=pbc)
    return(atoms)

def get_free_energy(doc):
    return doc["energy"]+doc["enthalpy"]-298.15*doc["entropy"]

mol_json = "bfo_hiprgen_small_dataset.json"

database_entries = loadfn(mol_json)

for doc in database_entries:
    atoms = init_ase_atoms_from_dict(doc)
    free_energy = get_free_energy(doc)
    write("tmp_xyz/"+doc["name"]+".xyz", atoms)
    print(free_energy, "\t" ,doc["name"])