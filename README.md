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

Since the *steri* dataset is not officially part of the BOP datasets, you will have to replace the `dataset_params.py` file with the provided one.
Then simply run
```sh
./generate_steri.sh
```