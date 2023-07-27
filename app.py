# importing pckg
import streamlit as st
import pandas as pd

import sys
import os

# Page configuration
st.set_page_config(
    page_title = 'Visualisierung',
    page_icon = ":bar_chart:",
    layout = 'wide'
)

# file size
def get_filesize(file):
    size_bytes = sys.getsizeof(file)
    size_mb = size_bytes / (1024**2)
    return size_mb

# file validation
def validate_file(file):
    filename = file.name
    name, ext = os.path.splitext(filename)
    if ext in (".csv", ".xlsx"):
        return ext
    else:
        return False

with st.sidebar:
    uploaded_file = st.file_uploader("Dateien sollen .csv, .xlsx Format haben und nicht mehr als 10 MB")


if uploaded_file is not None:
    ext = validate_file(uploaded_file)
    if ext:
        filesize = get_filesize(uploaded_file)
        if filesize <= 10:
            if ext == ".csv":
                 df = pd.read_csv(uploaded_file, encoding= 'unicode_escape')

            else:
                 xl_file = pd.ExcelFile(uploaded_file)
                 sheet_tuple = tuple(xl_file.sheet_names)
                 sheet_name = st.sidebar.selectbox("Wähle:",sheet_tuple)
                 df = xl_file.parse(sheet_name)


            # generate report (takes time)
            with st.spinner("Bericht wird erstellt..."):
                 pr = ProfileReport(df)

            st_profile_report(pr)
        else:
                st.error(f"Die maximale erlaubte Dateigröße beträgt 10 MB. Aber empfangen wurden {filesize} MB")

    else:
        st.error('Bitte lade nur .csv oder .xlsx Dateien hoch')

else:
    st.title('Data Profiler')
    st.info('Lade deine Dateien in der linken Seitenleiste hoch, um ein Profiling zu erstellen')
    