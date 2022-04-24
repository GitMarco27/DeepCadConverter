import gmsh
import streamlit as st
import trimesh

@st.cache
def convert_cad(geometry):
    mesh = trimesh.Trimesh(**trimesh.interfaces.gmsh.load_gmsh(file_name=geometry, gmsh_args=[
        ("Mesh.Algorithm", 1),  # Different algorithm types, check them out
        ("Mesh.CharacteristicLengthFromCurvature", 50),  # Tuning the smoothness, + smothness = + time
        ("General.NumThreads", 10),  # Multithreading capability
        ("Mesh.MinimumCirclePoints", 32)]))
    return mesh

# Add sidebar to the app
st.sidebar.markdown("### My first Awesome App")
st.sidebar.markdown("Welcome to my first awesome app. This app is built using Streamlit and uses data source from redfin housing market data. I hope you enjoy!")

# Add title and subtitle to the main interface of the app
st.title("CAD to STL converter")
st.markdown('### By Marco Sanguineti')

data = st.file_uploader("Upload your cad files", type={"iges", "igs"})
# new_data = convert_cad(data)
# if data is not None:
#     st.download_button('Download Geometry', data=data.read())

