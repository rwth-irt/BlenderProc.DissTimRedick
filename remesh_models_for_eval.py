import numpy as np
import os
import open3d as o3d
import shutil

models_in_path = "bop_datasets/steri/models_cad"
models_out_path = "bop_datasets/steri/models_eval"
if not os.path.exists(models_out_path):
    os.makedirs(models_out_path)

# Process models of all objects in the selected dataset.
# Iterate over all files in models_path and enumerate the ids
for obj_id, file_name in enumerate(os.listdir(models_in_path)):
    model_in_path = os.path.join(models_in_path, file_name)
    model_out_path = os.path.join(models_out_path, file_name)
    # Only process ply files
    if not file_name.endswith("ply"):
        print("Copy non *.ply file {}".format(file_name))
        # copy the file to the output folder
        shutil.copyfile(model_in_path, model_out_path)
        continue

    # Do not remesh if out file already exists
    if os.path.exists(model_out_path):
        continue
    mesh = o3d.io.read_triangle_mesh(model_in_path)

    print("Processing object {}".format(file_name))
    # Preprocessing
    mesh = mesh.remove_unreferenced_vertices()
    mesh = mesh.remove_duplicated_vertices()
    mesh = mesh.remove_degenerate_triangles()
    mesh = mesh.compute_triangle_normals()
    mesh = mesh.compute_vertex_normals()

    # Calc diameter for mesh density. 0.5% is not suitable for thin instrument
    min_bbox = mesh.get_minimal_oriented_bounding_box()
    diameter = np.linalg.norm(
        np.asarray(min_bbox.get_max_bound()) - np.asarray(min_bbox.get_min_bound())
    )
    mesh_density = 0.25 / 100 * diameter

    # Resampling
    n_vertices = 300_000
    points = mesh.sample_points_uniformly(n_vertices, use_triangle_normal=True)
    rec_mesh, _ = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
        points, width=mesh_density
    )

    # Set normals and color for visualization
    rec_mesh = rec_mesh.compute_vertex_normals()
    rec_mesh = rec_mesh.compute_triangle_normals()
    rec_mesh.paint_uniform_color(np.asarray([0.9, 0.9, 1]))

    # Visually inspect
    # o3d.visualization.draw_geometries(
    #     [rec_mesh],
    #     mesh_show_wireframe=True,
    #     mesh_show_back_face=True,
    #     window_name=file_name,
    # )

    o3d.io.write_triangle_mesh(model_out_path, rec_mesh)

print("Done.")
