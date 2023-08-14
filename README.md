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

# Generating datasets
Run the scripts
```sh
./generate_lm.sh
```