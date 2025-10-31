To install from `environment.yml`, you might need to create an osx64 environment with conda-forge channels:
```
conda config --add channels conda-forge
CONDA_SUBDIR=osx-64 conda env create -f environment.yml
conda activate stat-rethink2-pymc
conda config --env --set subdir osx-64
```
