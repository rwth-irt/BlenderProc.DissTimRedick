import numpy as np
import os
import open3d as o3d

models_in_path = "/home/rd/code/BlenderProc/bop_datasets/steri/models_cad"
models_out_path = "/home/rd/code/BlenderProc/bop_datasets/steri/models_eval"
if not os.path.exists(models_out_path):
    os.makedirs(models_out_path)

# Process models of all objects in the selected dataset.
# Iterate over all files in models_path and enumerate the ids
for obj_id, file_name in enumerate(os.listdir(models_in_path)):
    print("Processing object {}".format(file_name))
    model_in_path = os.path.join(models_in_path, file_name)
    model_out_path = os.path.join(models_out_path, file_name)

    mesh = o3d.io.read_triangle_mesh(model_in_path)
    # Preprocessing
    mesh = mesh.remove_unreferenced_vertices()
    mesh = mesh.remove_duplicated_vertices()
    mesh = mesh.remove_degenerate_triangles()
    mesh = mesh.compute_triangle_normals()
    mesh = mesh.compute_vertex_normals()

    # Resampling
    n_vertices = 100_000
    points = mesh.sample_points_uniformly(n_vertices, use_triangle_normal=True)
    radii = o3d.utility.DoubleVector([0.1, 1, 10, 50, 200])
    rec_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
        points, radii
    )

    # Voxel simplification to reduce computational overhead
    min_bbox = mesh.get_minimal_oriented_bounding_box()
    diameter = np.linalg.norm(
        np.asarray(min_bbox.get_max_bound()) - np.asarray(min_bbox.get_min_bound())
    )
    voxel_size = 0.25 / 100 * diameter
    rec_mesh = rec_mesh.simplify_vertex_clustering(voxel_size)

    rec_mesh = rec_mesh.compute_vertex_normals()
    rec_mesh = rec_mesh.compute_triangle_normals()
    o3d.visualization.draw_geometries([rec_mesh], mesh_show_wireframe=True)

    o3d.io.write_triangle_mesh(model_out_path, rec_mesh)

print("Done.")
