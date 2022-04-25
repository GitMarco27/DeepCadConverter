import os
import shutil
import sys
import streamlit as st

# Add sidebar to the app
st.sidebar.markdown("### Cad to Stl Converter")
st.sidebar.markdown("This app is built using Streamlit and converts Cad files into an **Stl** format.")
st.sidebar.markdown("""
**Supported formats**:

    - .step / .stp
    - .iges / .igs

### Credits
**Marco Sanguineti**

* marco.sanguineti.info@gmail.com
* [LinkedIn](https://www.linkedin.com/in/marco-sanguineti-088604161/)
* [Medium](https://medium.com/@marcosanguineti) 

""")

# Add title and subtitle to the main interface of the app
st.title("CAD to STL converter")
st.image('resources/images/banner.png')
st.markdown('Marco Sanguineti - 2022')
st.markdown('---')

with st.expander("Settings"):
    st.markdown('Settings guidelines: [gmsh](http://gmsh.info/doc/texinfo/gmsh.html)')
    algo = st.text_input(label='Algorithm', value='1')
    car_length = st.text_input(label='CharacteristicLengthFromCurvature', value='50')
    num_threads = st.text_input(label='NumThreads', value='10')
    min_circle_points = st.text_input(label='MinimumCirclePoints', value='32')

    args = [algo, car_length, num_threads, min_circle_points]

# Loading data
data = st.file_uploader("Upload your cad files", type={"iges", "igs", "step", "stp"}, accept_multiple_files=True)
st.markdown('---')

# Converting files if requested
if st.button('Convert your files'):
    # Clearing files, if exist
    if not os.path.exists('tempDir'):
        os.mkdir('tempDir')
    for file in os.listdir('tempDir'):
        os.remove(os.path.join('tempDir', file))
    if os.path.exists('archive.zip'):
        os.remove('archive.zip')

    if len(data) > 0:
        with st.expander("Logs"):
            for cad in data:
                source = os.path.join("tempDir", cad.name)
                dest = os.path.join("tempDir", os.path.splitext(cad.name)[0]+'.stl')
                with open(os.path.join("tempDir", cad.name), "wb") as f:
                    f.write(cad.getbuffer())

                st.write(f'Working on {os.path.basename(source)}...')
                os.system(f'{sys.executable} cad_converter.py {source} {dest} '
                          f'{args[0]} {args[1]} {args[2]} {args[3]}')
                if os.path.exists(dest):
                    st.write(f'{os.path.basename(dest)}: completed')
                else:
                    st.write(f'{os.path.basename(dest)}: error detected')

        st.markdown('Your .stl files are ready! (Check logs for errors)')

        shutil.make_archive('archive', 'zip', 'tempDir')

        if os.path.exists('archive.zip'):
            with open('archive.zip', 'rb') as f:
                st.download_button('Download', f, file_name='archive.zip')

