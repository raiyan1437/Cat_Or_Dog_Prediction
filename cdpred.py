from cdmodel import load_model
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import keras.preprocessing


def app():
    with st.spinner('Model is being loaded..'):
        model = load_model()
    st.subheader("""
    **NOTE:** This app work best only when you uplode image of a Cat or Dog.
    """)
    file = st.file_uploader(
        "Please upload a Picture of CAT or DOG ", type=["jpg", "jpeg", "png"])
    st.set_option('deprecation.showfileUploaderEncoding', False)

    if file is None:
        st.write("""
        Please upload an image file
        """)
    else:
        if st.button("Predict"):
            try:
                pic = Image.open(file)            
                st.image(pic, use_column_width=True)
                test_img = tf.image.resize(pic, [64, 64])
                img = keras.preprocessing.image.img_to_array(test_img)
                img = np.expand_dims(img, axis=0)

                cnn = model.predict(img)
                if cnn[0][0] == 1:
                    pred = "It's a DOG"
                else if cnn[0][0] == 0:
                    pred = "It's a CAT"
                else
                    pred ="it is niether a cat nor a dog"
                st.success(pred)
            except:
                st.error("Invalid Image Type For This Model")
