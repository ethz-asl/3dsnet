# Written by the mighty Pierre-Alain Langlois


import argparse
from os import listdir
from os.path import isfile, join
# import pymesh
import trimesh
import numpy as np
import copy


def shuffle_pc(file, output_path):
    """
    Function to shuffle a point cloud produced by virtual scanner.
    """
    mesh = trimesh.load_mesh(file)
    vertices = copy.deepcopy(mesh.vertices)
    permutation = np.random.permutation(len(vertices))
    vertices = vertices[permutation]
    new_mesh = trimesh.Trimesh(vertices, faces = mesh.faces)
    new_mesh.add_attribute("vertex_nx")
    new_mesh.set_attribute("vertex_nx", mesh.get_vertex_attribute("vertex_nx")[permutation])
    new_mesh.add_attribute("vertex_ny")
    new_mesh.set_attribute("vertex_ny", mesh.get_vertex_attribute("vertex_ny")[permutation])
    new_mesh.add_attribute("vertex_nz")
    new_mesh.set_attribute("vertex_nz", mesh.get_vertex_attribute("vertex_nz")[permutation])
    new_mesh.export(output_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Input file", required=True)
    parser.add_argument("--output", help="Output file", required=True)
    args = parser.parse_args()
    shuffle_pc(args.input, args.output)


if __name__ == "__main__":
    main()
