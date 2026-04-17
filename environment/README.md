## Environment for SOTA end-to-end DL-based docking tools
To install environment for each DL-based docking tools, please run:
```
conda env create -f environment_{docking-tool}.yaml
```
Note that, for DeepDock, `deepdock_python36` is only used for generating mesh input files, while `deepdock_python38` is used for docking and scoring.

AlphaFold3 and Boltz-2(x) were launched using Singularity containers on an Ubuntu 22.04-based HPC.

For more information, please visit each docking tool GitHub: [DeepDock](https://github.com/OptiMaL-PSE-Lab/DeepDock), [Interformer](https://github.com/tencent-ailab/Interformer), [SurfDock](https://github.com/CAODH/SurfDock), [karmaDock](https://github.com/schrojunzhang/KarmaDock), [AlphaFold3](https://github.com/google-deepmind/alphafold3), [Boltz-2](https://github.com/jwohlwend/boltz)
