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

# Object model conversions
* If you have a set of models available as **Stanford PLY files** with units in mm, you can use the following script to convert them to the format required by BOP via the *calc_models_info.py*.
  Please look into the python file to modify the path to the PLY files.
