import streamlit as st
import os
from PIL import Image

def app():
    st.title("Elevation")

    # Folder path where images are stored
    image_folder = "data/elevation"

    # Get list of image files (1.jpg to 14.jpg)
    image_files = [os.path.join(image_folder, f"{i}.jpg") for i in range(1, 15)]

    # Create 3 columns for layout
    cols = st.columns(3)

    # Dictionary to track selected image
    selected_image = None

    # Display images in a grid
    for idx, image_file in enumerate(image_files):
        with cols[idx % 3]:
            img = Image.open(image_file)
            st.image(img, caption=f"Image {idx + 1}",  use_container_width=True)
            if st.button(f"Select Image {idx + 1}"):
                selected_image = image_file

    # Display the selected image in a larger view
    if selected_image:
        st.write("Selected Image:")
        selected_img = Image.open(selected_image)
        st.image(selected_img, caption="Selected Image",  use_container_width=True)

