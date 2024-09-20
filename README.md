# About
This code has been produced during while writing my Ph.D. (Dr.-Ing.) thesis at the institut of automatic control, RWTH Aachen University.
If you find it helpful for your research please cite this:
> T. Redick, „Bayesian inference for CAD-based pose estimation on depth images for robotic manipulation“, RWTH Aachen University, 2024. doi: [10.18154/RWTH-2024-04533](https://doi.org/10.18154/RWTH-2024-04533).

# First use
Set up a virtual environment and install BlenderProc via pip:
```sh
chmod +x setup_venv.sh
./setup_venv.sh
```
Now activate the virtual environment and download the required resources:
```sh
source venv/bin/activate
blenderproc download cc_textures cc_textures
```

# Generating pose datasets
Run the scripts
```sh
./generate_lm.sh
./generate_lmo.sh
```

Since the *steri* dataset is not officially part of the BOP datasets, you will have to replace the `dataset_params.py` of the Blender installation with the provided one.
Something like *~/blender/blender-3.5.1-linux-x64/custom-python-packages/lib/python3.10/site-packages/bop_toolkit_lib/dataset_params.py*.
Reinstall the BOP toolkit:
```sh
pip install -e bop_toolkit
```

Then simply run
```sh
./generate_steri.sh
```
