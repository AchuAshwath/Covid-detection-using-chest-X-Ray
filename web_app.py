from PIL import Image
import streamlit as st

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


image = Image.open("D:/achu/programs/miniProject/kjr-21-e25-g001-l-a.jpg")
st.image(image, use_column_width=True)

print(type(image))

