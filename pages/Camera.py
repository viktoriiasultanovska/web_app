import streamlit as st
from PIL import Image

uploaded_image = st.file_uploader("Upload Image")

def convert_image_to_grayscale(image):
    # Create a pillow image instance
    img = Image.open(image)
    # Convert the pillow image to grayscale
    return img.convert("L")


def render_gray_image(img):
    # Render the grayscale image
    st.image(img)


if uploaded_image:
    gray_img = convert_image_to_grayscale(uploaded_image)
    render_gray_image(gray_img)

with st.expander('Start camera'):
    # Start the camera
    camera_image = st.camera_input('Camera')

if camera_image:
    gray_img = convert_image_to_grayscale(camera_image)
    render_gray_image(gray_img)
