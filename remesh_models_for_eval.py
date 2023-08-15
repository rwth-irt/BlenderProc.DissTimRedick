# Author: Tomas Hodan (hodantom@cmp.felk.cvut.cz)
# Center for Machine Perception, Czech Technical University in Prague

"""'Uniformly' resamples and decimates 3D object models for evaluation.

Note: Models of some T-LESS objects were processed by Blender (using the Remesh modifier).
"""

import os
import numpy as np
import open3d as o3d

models_in_path = "/home/rd/code/BlenderProc/bop_datasets/steri/models_cad"
models_out_path = "/home/rd/code/BlenderProc/bop_datasets/steri/models_eval"
if not os.path.exists(models_out_path):
    os.makedirs(models_out_path)

# Path to scripts/meshlab_scripts/remesh_for_eval.mlx.
meshlab_script_path = "remesh_for_eval_cell=0.25.mlx"

# Process models of all objects in the selected dataset.
# Iterate over all files in models_path and enumerate the ids
for obj_id, file_name in enumerate(os.listdir(models_in_path)):
    print("Processing object {}".format(file_name))
    model_in_path = os.path.join(models_in_path, file_name)
    model_out_path = os.path.join(models_out_path, file_name)

    mesh = o3d.io.read_triangle_mesh(model_in_path)
    # Preprocessing
    mesh.remove_unreferenced_vertices()
    mesh.remove_duplicated_vertices()
    mesh.remove_degenerate_triangles()
    mesh.compute_vertex_normals()
    # Resampling
    n_vertices = int(1.0 * len(mesh.vertices))
    points = mesh.sample_points_uniformly(n_vertices)
    radii = [1, 2, 5, 10, 20, 50]
    rec_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
        points, o3d.utility.DoubleVector(radii)
    )
    # o3d.visualization.draw_geometries([rec_mesh])
    o3d.io.write_triangle_mesh(model_out_path, rec_mesh)

print("Done.")
