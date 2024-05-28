import streamlit as st
from simple_lama_inpainting import SimpleLama
from PIL import Image
import os

# Initialize the SimpleLama model
simple_lama = SimpleLama()

# Streamlit application
st.title("Image Inpainting with SimpleLama")

# Upload image and mask
uploaded_image = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
uploaded_mask = st.file_uploader("Choose a mask...", type=["png", "jpg", "jpeg"])

if uploaded_image is not None and uploaded_mask is not None:
    # Open the image and mask
    image = Image.open(uploaded_image)
    mask = Image.open(uploaded_mask).convert('L')
    
    # Display the uploaded image and mask
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.image(mask, caption='Uploaded Mask', use_column_width=True)
    
    if st.button('Inpaint'):
        # Perform inpainting
        result = simple_lama(image, mask)
        
        # Display the result
        st.image(result, caption='Inpainted Image', use_column_width=True)
        
        # Save the result
        result_path = "inpainted_result.jpg"
        result.save(result_path)
        
        # Provide a download link
        with open(result_path, "rb") as file:
            btn = st.download_button(
                label="Download inpainted image",
                data=file,
                file_name="inpainted_result.jpg",
                mime="image/jpeg"
            )

