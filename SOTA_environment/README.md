## Environment for SOTA end-to-end DL-based docking tools
To install environment for each DL-based docking tools, please run:
```
conda env create -f environment_{docking-tool}.yaml
```
Note that, for DeepDock, `deepdock_python36` is only used for generating mesh input files, while `deepdock_python38` is used for docking and scoring.