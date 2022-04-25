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
st.markdown('*By Marco Sanguineti - GitMarco27*')
st.markdown('---')

# Loading data
data = st.file_uploader("Upload your cad files", type={"iges", "igs", "step", "stp"}, accept_multiple_files=True)

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
        for cad in data:
            source = os.path.join("tempDir", cad.name)
            dest = os.path.join("tempDir", os.path.splitext(cad.name)[0]+'.stl')
            with open(os.path.join("tempDir", cad.name), "wb") as f:
                f.write(cad.getbuffer())

            os.system(f'{sys.executable} cad_converter.py {source} {dest}')

        st.markdown('Your .stl files are ready!')

        shutil.make_archive('archive', 'zip', 'tempDir')

        with open('archive.zip', 'rb') as f:
            st.download_button('Download', f, file_name='archive.zip')

