#!/bin/bash

smi_file="$1"
out_dir="$2"

mkdir -p ${out_dir}
mkdir -p ${out_dir}/SMI
mkdir -p ${out_dir}/SDF
mkdir -p ${out_dir}/smina

protein="../data/Template/7QGT_protein_dockprep.mol2"
ligand="../data/Template/7QGT_ligand.sdf"


tail -n +2 ${smi_file} | while IFS=, read -r ID SMILES; do

	echo "$SMILES" > ${out_dir}/SMI/${ID}.smi
	
	obabel ${out_dir}/SMI/${ID}.smi -O ${out_dir}/SDF/${ID}.sdf --gen3d -p 7.4
	
	./smina.static -r ${protein} -l ${out_dir}/SDF/${ID}.sdf --autobox_ligand ${ligand} \
	--size_x 30 --size_y 30 --size_z 30 --exhaustiveness 8 --num_modes 1 --seed 36 \
	-o ${out_dir}/smina/${ID}_smina.sdf > ${out_dir}/smina/${ID}_smina.txt
	
	echo "Finish docking ${ID}"
	
done 

