#!/usr/bin/env bash

# Conda environment name
name="Fasta" # Change it whenever you want a new env

# Create the env only if it doesn't already exist
if conda env list | awk '{print $1}' | grep -qx "$name"; then
    echo "Env '$name' already exists, skipping creation."
else
    conda create -y -n "$name" python=3.12 pip ipython ipykernel # You can choose the python version here and some 3rd party modules. pip highly recommended.
fi
# Install other 3rd party tools
conda install -y -n "$name" -c conda-forge --override-channels pandas numpy biopython # Installs pandas, numpy and biopython via conda-forge channel