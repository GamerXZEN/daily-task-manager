import streamlit as sl
from PIL import Image

sl.title("Grayscale Camera")

with sl.expander("Start Camera"):
	camera_image = sl.camera_input("Camera")

uploaded_image = sl.file_uploader("Upload Image")

if camera_image:
	img = Image.open(camera_image)
	gray_img = img.convert("L")
	sl.image(gray_img)

if uploaded_image:
	img = Image.open(uploaded_image)
	gray_img = img.convert("L")
	sl.image(gray_img)
