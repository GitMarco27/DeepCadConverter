import sys
import trimesh


def convert_cad(source, dest):
    mesh = trimesh.Trimesh(**trimesh.interfaces.gmsh.load_gmsh(file_name=source, gmsh_args=[
        ("Mesh.Algorithm", 1),  # Different algorithm types, check them out
        ("Mesh.CharacteristicLengthFromCurvature", 50),  # Tuning the smoothness, + smothness = + time
        ("General.NumThreads", 10),  # Multithreading capability
        ("Mesh.MinimumCirclePoints", 32)]))
    mesh.export(dest)


if __name__ == "__main__":
    convert_cad(sys.argv[1], sys.argv[2])


