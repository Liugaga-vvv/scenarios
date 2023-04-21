# Environment Management

```bash
# Create a new Conda environment called "environment_management"
conda create --name environment_management

# Activate the "environment_management" environment
conda activate environment_management

# Install the following packages: h5py, scipy, nose
conda install h5py scipy nose

# Export the "environment_management" environment to an environment file called "environment.yml"
conda env export > environment.yml

# Deactivate the "environment_management" environment
conda deactivate

# Create a new Conda environment called "imported_environment" and import the "environment.yml" file into the "imported_environment" environment
conda env create --name imported_environment --file environment.yml
```
