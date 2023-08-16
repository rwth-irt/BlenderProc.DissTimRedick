# @license BSD-3 https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2023, Institute of Automatic Control - RWTH Aachen University
# All rights reserved.

# Virtual environment
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip setuptools

# BOP toolkit for mask and scene_gt_info annotations
git clone https://github.com/thodan/bop_toolkit
cd bop_toolkit
# cocoapi fails for bop_toolkit requirements.txt
pip install -r ../bop_toolkit_req.txt 
pip install -e .
cd ..

# For model infos and remeshing
pip install open3d

# BlenderProc
# pip install blenderproc
git clone https://github.com/DLR-RM/BlenderProc
cd BlenderProc
pip install -e .
cd ..
