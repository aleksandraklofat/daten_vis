# importing pckg
import streamlit as st
import pandas as pd

import sys
import os

# Page configuration
st.set_page_config(
    page_title = 'Visualisierung',
    page_icon = ':cloud:',
    layout = 'wide'
)

# file size
def get_filesize(file):
    size_bytes = sys.getsizeof(file)
    size_mb = size_bytes / (1024**2)
    return size_mb