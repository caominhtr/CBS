import argparse
import pandas as pd
import os
import warnings
import subprocess

warnings.filterwarnings("ignore", category=DeprecationWarning)

from preprocess import validate_smiles
from PLEC import PLEC_generate
from model_specific import infer_model


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="Input SMILES file (.smi)")
    parser.add_argument("-o", "--outdir", required=True, help="Output directory")
    args = parser.parse_args()

    smi_file = args.file
    outdir = args.outdir

    os.makedirs(outdir, exist_ok=True)

    validate_smiles(smi_file, outdir)

    validated_smi = os.path.join(outdir, "1.SMILES_validated.csv")

    subprocess.run(["./docking.sh", validated_smi, outdir],check=True)

    df_smi = pd.read_csv(validated_smi)

    PLEC_list = []
    PLEC_path = os.path.join(outdir, "2.PLEC_data.csv")

    for id in df_smi['ID']:
        smina_generated = os.path.join(outdir, "smina",f"{id}_smina.sdf")
        PLEC_list.append(PLEC_generate(smina_generated, id))


    pd.DataFrame(PLEC_list).to_csv(PLEC_path, index = False)

    print("Finish PLEC generation!")

    df_plec = pd.read_csv(PLEC_path)

    final_path = os.path.join(outdir, "3.Final_result.csv")
    df_final = infer_model(df_plec)

    df_final.to_csv(final_path, index = False)

    print(f"Finish calculation. Results are saved in {final_path}")

if __name__ == "__main__":
    main()