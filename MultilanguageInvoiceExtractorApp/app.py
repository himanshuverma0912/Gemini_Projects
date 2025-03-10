from dotenv import load_dotenv  # Import the library to load environment variables from a .env file.
load_dotenv()  # Load the environment variables from the .env file into the system.

import streamlit as st  # Import the Streamlit library for creating web applications.
import os  # Import the operating system library for interacting with the system.
import google.generativeai as genai  # Import the Google Generative AI library.
from PIL import Image # Import the Pillow (PIL) library for image processing.

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))  # Configure the Google Generative AI with your API key, fetched from the environment variables.

model = genai.GenerativeModel("gemini-2.0-flash")  # Create an instance of the Gemini model (specifically, the "flash" version for faster responses).

def get_gemini_response(input,image,prompt): # Define a function to get a response from the Gemini model, taking text, image data, and prompt as input.
    response = model.generate_content([input,image[0],prompt]) # Send the combined input to the Gemini model.
    return response.text # Return only the text part of the model's response.

def input_image_details(uploaded_file): # Define a function to process the uploaded image file.
    if uploaded_file is not None: # Check if a file has been uploaded.
        bytes_data = uploaded_file.getvalue() # Get the raw bytes of the uploaded file.
        image_parts = [ # Create a list containing image data in the format expected by the Gemini model.
            {
                "mime_type": uploaded_file.type, # Store the MIME type of the uploaded file (e.g., image/jpeg).
                "data": bytes_data # Store the raw bytes of the image data.
            }
        ]
        return image_parts # Return the list of image parts.
    else:
        raise FileNotFoundError("No File Uploaded") # Raise an error if no file was uploaded.

st.set_page_config(page_title="Multilanguage Invoice extractor") # Set the title of the Streamlit web page.
st.header("Multilanguage Invoice extractor") # Display a header on the web page.
input = st.text_input("Input prompt:",key="input") # Create a text input field for the user to enter their question or prompt about the invoice.
uploaded_file = st.file_uploader("Choose an image of invoice",type=["jpeg","jpg","png"]) # Create a file uploader to allow the user to upload an invoice image.

image="" # Initialize a variable to store the uploaded image.
if uploaded_file is not None: # Check if a file has been uploaded.
    image = Image.open(uploaded_file) # Open the uploaded image using the Pillow library.
    st.image(image,caption="uploaded image",use_container_width=True) # Display the uploaded image on the web page.

submit = st.button("Tell me about the invoice") # Create a button that the user can click to submit their request to analyze the invoice.

input_prompt=""" You are an expert in understanding invoices.We will upload an image as invoice and you will have to answer any questions based on uploaded invoive image""" # Define a default prompt to instruct the Gemini model about its role.

if submit: # Check if the submit button has been clicked.
    image_data=input_image_details(uploaded_file) # Process the uploaded image to prepare it for the Gemini model.
    response = get_gemini_response(input_prompt,image_data,input) # Get the response from the Gemini model using the default prompt, image data, and user input.
    st.subheader("The Response is ") # Display a subheader to indicate the response.
    st.write(response) # Display the response from the Gemini model on the web page.