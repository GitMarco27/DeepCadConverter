import sys
import trimesh


def convert_cad(source, dest, args):
    # General info found on https://trimsh.org/trimesh.interfaces.gmsh.html Returns a surface mesh from CAD model in
    # Open Cascade Breap (.brep), Step (.stp or .step) and Iges formats Or returns a surface mesh from 3D volume mesh
    # using gmsh. For a list of possible options to pass to GMSH, check: http://gmsh.info/doc/texinfo/gmsh.html
    mesh = trimesh.Trimesh(**trimesh.interfaces.gmsh.load_gmsh(file_name=source, gmsh_args=[
        ("Mesh.Algorithm", int(args[0])),  # Different algorithm types, check them out
        ("Mesh.CharacteristicLengthFromCurvature", int(args[1])),  # Tuning the smoothness, + smothness = + time
        ("General.NumThreads", int(args[2])),  # Multithreading capability
        ("Mesh.MinimumCirclePoints", int(args[3]))]))

    # scene = mesh.scene()

    # window_conf = gl.Config(double_buffer=True, depth_size=6)
    # png = scene.save_image(resolution=[1920, 1080],
    #                        window_conf=window_conf,
    #                        visible=False)

    # rendered = Image.open(trimesh.util.wrap_as_stream(png))
    # rendered.save('tmp.png')

    mesh.export(dest)

    # png = PIL.Image.open(scene.save_image(resolution=(1920, 1080)))


if __name__ == "__main__":
    convert_cad(sys.argv[1], sys.argv[2], args=sys.argv[3:])


