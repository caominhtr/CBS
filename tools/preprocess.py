import os
import pandas as pd
from rdkit import Chem
from rdkit.Chem import  PandasTools, CanonSmiles
from rdkit.Chem.SaltRemover import SaltRemover



def validate_smiles(smi, outdir):

    df = pd.read_csv(smi)
    PandasTools.AddMoleculeColumnToFrame(df, 'SMILES','Structure')

    df_new = df[~df['Structure'].isna()].reset_index(drop = True)

    rem = SaltRemover()
    df_new['Canon_SMILES'] = df_new['Structure'].apply(lambda x: CanonSmiles(Chem.MolToSmiles(rem(x))))

    output_smi_validated = os.path.join(outdir, "1.SMILES_validated.csv")

    df_new[['ID','Canon_SMILES']].to_csv(output_smi_validated, index = False)  

