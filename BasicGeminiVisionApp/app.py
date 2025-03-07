from dotenv import load_dotenv  # Import the library to load environment variables from a .env file.
load_dotenv()  # Load the environment variables from the .env file into the system.

import streamlit as st  # Import the Streamlit library for creating web applications.
import os  # Import the operating system library for interacting with the system.
import google.generativeai as genai  # Import the Google Generative AI library.
from PIL import Image # Import the Pillow (PIL) library for image processing.

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))  # Configure the Google Generative AI with your API key, fetched from the environment variables.

model = genai.GenerativeModel("gemini-2.0-flash")  # Create an instance of the Gemini model (specifically, the "flash" version for faster responses).

def get_gemini_response(input,image): # Define a function to get a response from the Gemini model, taking both text and image as input.
    if input!="": # Check if the user has provided text input.
        response = model.generate_content([input,image]) # If there is text input, send both the text and the image to the Gemini model.
    else:
        response = model.generate_content(image) # If there is no text input, send only the image to the Gemini model.
    return response.text # Return only the text part of the model's response.
st.set_page_config(page_title="Gemini Image Demo")  # Set the title of the Streamlit web page.
st.header("Gemini LLM App")  # Display a header on the web page.
input = st.text_input("Input Prompt:",key="input")  # Create a text input field for the user to enter their question or prompt about the image.

uploaded_file = st.file_uploader("Choose an image...",type = ["jpg","jpeg","png"]) # Create a file uploader to allow the user to upload an image.
image ="" # Initialize a variable to store the uploaded image.
if uploaded_file is not None: # Check if a file has been uploaded.
    image = Image.open(uploaded_file) # Open the uploaded image using the Pillow library.
    st.image(image,caption="Uploaded Image",use_container_width=True) # Display the uploaded image on the web page.

submit = st.button("Tell me about Image")  # Create a button that the user can click to submit their request to analyze the image.

if submit:  # Check if the submit button has been clicked.
    response = get_gemini_response(input,image) # Get the response from the Gemini model using the provided text input and uploaded image.
    st.subheader("The response is")  # Display a subheader to indicate the response.
    st.write(response)  # Display the response from the Gemini model on the web page.