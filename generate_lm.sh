# @license BSD-3 https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2023, Institute of Automatic Control - RWTH Aachen University
# All rights reserved.

source venv/bin/activate

blenderproc run main_lm_upright.py \
  /home/rd/code/PoseErrors.jl/datasets \
  cctextures \
  output \
  --num_scenes=1 # 25 images per scene -> 150 images total
