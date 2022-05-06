from PIL import Image
import streamlit as st
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import numpy as np
from keras.preprocessing import image

model= tf.keras.models.load_model('bestmodel.h5') # Loading the Tensorflow Saved Model

def get_img_array(img_path):
  """
  Input : Takes in image path as input 
  Output : Gives out Pre-Processed image
  """
  path = img_path
  img = image.load_img(path, target_size=(224,224,3))
  img = image.img_to_array(img)
  img = np.expand_dims(img , axis= 0 )
  
  return img

st.write("""
# Covid-19 Test
 This app predicts if the given x-ray is covid positive or not!
""")

# creating the sidebar
st.sidebar.header("Upload Image")
st.sidebar.markdown("""
[Example Jpeg input file](https://github.com/AchuAshwath/MiniProject/blob/main/IM-0143-0001.jpeg)
""")

upload_file = st.sidebar.file_uploader("Upload your jpeg file here", type=["jpeg", "jpg"])

st.write("""***""")


