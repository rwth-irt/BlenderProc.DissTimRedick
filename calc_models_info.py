# @license BSD-3 https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2023, Institute of Automatic Control - RWTH Aachen University
# All rights reserved.

from bop_toolkit_lib import inout, misc

import os
import numpy as np
import open3d as o3d

# Put the instrument meshes as Stanford PLY in this location
# The files are renamed according the BOP convention and
models_path = "/home/rd/code/BlenderProc/bop_datasets/steri/models_cad"

models_info = {}
# Iterate over all files in models_path and enumerate the ids
for obj_id, file_name in enumerate(os.listdir(models_path)):
    misc.log("Processing object {}".format(file_name))
    file_path = os.path.join(models_path, file_name)
    # Calculate 3D bounding box.
    mesh = o3d.io.read_triangle_mesh(file_path)
    bbox = mesh.get_axis_aligned_bounding_box()
    ref_pt = mesh.get_min_bound()
    max_pt = mesh.get_max_bound()
    size = max_pt - ref_pt
    print("Bounding box ref: {}, size: {}".format(ref_pt, size))
    # Calculated diameter.
    min_bbox = mesh.get_minimal_oriented_bounding_box()
    diameter = np.linalg.norm(
        np.asarray(min_bbox.get_max_bound()) - np.asarray(min_bbox.get_min_bound())
    )
    print("Diameter: {}".format(diameter))
    # Extract file_name without extension
    original_id = os.path.splitext(file_name)[0]
    models_info[obj_id] = {
        "min_x": ref_pt[0],
        "min_y": ref_pt[1],
        "min_z": ref_pt[2],
        "size_x": size[0],
        "size_y": size[1],
        "size_z": size[2],
        "diameter": diameter,
        "original_id": original_id,
    }

    # Rename the files to 00000x format
    new_file_name = "obj_{:06d}.ply".format(obj_id)
    misc.log("Rename {} to {}".format(file_name, new_file_name))
    new_file_path = os.path.join(models_path, new_file_name)
    os.rename(file_path, new_file_path)

# Save the calculated info about the object models.
models_info_path = os.path.join(models_path, "models_info.json")
inout.save_json(models_info_path, models_info)
