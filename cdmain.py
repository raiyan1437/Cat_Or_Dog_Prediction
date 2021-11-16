from cdmodel import load_model
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import keras.preprocessing
import cdhome, cdpred, cdabout
pages = {
    "Home": cdhome,
    "Prediction": cdpred,
    "About": cdabout
}



st.sidebar.title("Navigation")
page = st.sidebar.radio("Pages", list(pages.keys()))
if page == None:
    cdhome.app()
else:
    pages[page].app()
