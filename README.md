# AI-Powered Image Inpainting in Streamlit

Pre-trained Model: We use the SimpleLama pre-trained model for image inpainting. This model is known for its effectiveness in generating realistic inpainting results by leveraging advanced deep learning techniques.
Model Initialization: The SimpleLama model is initialized once at the beginning of the application.
Image and Mask Upload: Users can upload an image and a corresponding mask through the Streamlit interface.
Image Processing: The uploaded images are processed to be compatible with the SimpleLama model.
Inpainting Execution: The model takes the image and mask as input, performs inpainting, and generates the inpainted image.
Result Handling: The inpainted image is displayed to the user and can be downloaded directly from the web interface.



How to run on the system

1. Run the Streamlit application from the terminal which is inside the main.py: streamlit run app.py

2. Open the provided local URL in your web browser.

3. Upload an image and a mask to see the inpainting result.

4. Click on the "Inpaint" button to process the image.

5. Download the inpainted image using the provided download button.



## The code is based on the Repo:

1. https://github.com/advimman/lama
2.  https://github.com/enesmsahin/simple-lama-inpainting
