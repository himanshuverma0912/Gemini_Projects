import streamlit as st  # Import the Streamlit library for creating web applications.
import google.generativeai as genai  # Import the Google Generative AI library.
import os  # Import the operating system library for interacting with the system.
from dotenv import load_dotenv  # Import the library to load environment variables from a .env file.
load_dotenv()  # Load the environment variables from the .env file into the system.
from PIL import Image  # Import the Pillow (PIL) library for image processing.

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))  # Configure the Google Generative AI with your API key, fetched from the environment variables.

def get_gemini_response(input_prompt,image):  # Define a function to get a response from the Gemini model, taking a prompt and image data as input.
    model = genai.GenerativeModel('gemini-2.0-flash')  # Create an instance of the Gemini model (specifically, the "flash" version for faster responses).
    response = model.generate_content([input_prompt,image[0]])  # Send the prompt and image data to the Gemini model.
    return response.text  # Return only the text part of the model's response.

def input_image_setup(uploaded_file):  # Define a function to process the uploaded image file.
    if uploaded_file is not None:  # Check if a file has been uploaded.
        bytes_data = uploaded_file.getvalue()  # Get the raw bytes of the uploaded file.
        image_parts = [  # Create a list containing image data in the format expected by the Gemini model.
            {
                "mime_type" : uploaded_file.type,  # Store the MIME type of the uploaded file (e.g., image/jpeg).
                "data" : bytes_data  # Store the raw bytes of the image data.
            }
        ]
        return image_parts  # Return the list of image parts.
    else:
        raise FileNotFoundError("No File Uploaded")  # Raise an error if no file was uploaded.

st.set_page_config(page_title = "Gemini Health App")  # Set the title of the Streamlit web page.
st.header("Gemini Health App")  # Display a header on the web page.
uploaded_file = st.file_uploader("Choose an image...",type=["jpg","jpeg","png"])  # Create a file uploader to allow the user to upload an image.
image = ""  # Initialize a variable to store the uploaded image.
if uploaded_file is not None:  # Check if a file has been uploaded.
    image = Image.open(uploaded_file)  # Open the uploaded image using the Pillow library.
    st.image(image,caption = "Uploaded Image",use_container_width=True)  # Display the uploaded image on the web page.
submit = st.button("Tel me about total calories")  # Create a button that the user can click to submit their request to analyze the image.

input_prompt=""" You are an expert in nutritionist where you need to see the food items from the image and calculate the total calories,also provide the details of every food items with calories intake in below format:
1. Item 1 - number of calories
2. Item 2 - number of calories
Finally you can also mention whether the food is healthy or not and also mention the percentage split of the ratio of carbohydrates,fats,fibers,sugar and other important things required in our diet.""" # Define a prompt to instruct the Gemini model about its role.

if submit:  # Check if the submit button has been clicked.
    image_data = input_image_setup(uploaded_file)  # Process the uploaded image to prepare it for the Gemini model.
    response = get_gemini_response(input_prompt,image_data)  # Get the response from the Gemini model using the provided prompt and image data.
    st.header("The Response is")  # Display a header to indicate the response.
    st.write(response)  # Display the response from the Gemini model on the web page.