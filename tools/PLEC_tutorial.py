from PLEC import PLEC_generate
import os
import numpy as np

##### INPUTS: LIGAND IN SDF FORMAT
#/PLEC_tutorial/Ligand_*.sdf


#### CASE 1: GENERATE FINGERPRINT FOR 1 LIGAND

print('CASE 1: GENERATE FINGERPRINT FOR 1 LIGAND')

ligand_1_fp = PLEC_generate('./PLEC_tutorial/Ligand_1.sdf', 'Ligand_1')
print(ligand_1_fp)

print('')

#### CASE 2: GENERATE FINGERPRINT FOR A BATCH OF LIGAND

print('CASE 2: GENERATE FINGERPRINT FOR A BATCH OF LIGAND')
ligand_fp_list = []

for file in os.listdir('./PLEC_tutorial'):
    ligand_id = os.path.splitext(file)[0]
    ligand_fp_list.append(PLEC_generate(f'./PLEC_tutorial/{file}', ligand_id))

print(np.array(ligand_fp_list))
    
