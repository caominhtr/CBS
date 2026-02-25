import oddt
from oddt.fingerprints import PLEC
import pandas as pd
import numpy as np


def PLEC_generate(ligand_sdf, id):
    protein = next(oddt.toolkit.readfile('mol2', f'../data/Template/7QGT_protein_dockprep.mol2'))
    ligand = next(oddt.toolkit.readfile('sdf', ligand_sdf))
    features = PLEC(ligand = ligand, protein = protein, size = 1024,
                    depth_protein = 4, depth_ligand = 2,
                    distance_cutoff = 4.5, sparse = False)

    return np.array(features.tolist() + [f'{id}'])

