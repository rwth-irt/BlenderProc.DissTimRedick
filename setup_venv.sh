# @license BSD-3 https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2023, Institute of Automatic Control - RWTH Aachen University
# All rights reserved.

# Virtual environment
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip setuptools

# For model infos and remeshing
pip install open3d

# BlenderProc
git clone https://github.com/DLR-RM/BlenderProc
cd BlenderProc
pip install -e .
cd ..
