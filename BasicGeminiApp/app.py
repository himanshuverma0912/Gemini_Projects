from dotenv import load_dotenv  # Import the library to load environment variables from a .env file.
load_dotenv()  # Load the environment variables from the .env file into the system.

import streamlit as st  # Import the Streamlit library for creating web applications.
import os  # Import the operating system library for interacting with the system.
import google.generativeai as genai  # Import the Google Generative AI library.

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))  # Configure the Google Generative AI with your API key, fetched from the environment variables.

model = genai.GenerativeModel("gemini-2.0-flash")  # Create an instance of the Gemini model (specifically, the "flash" version for faster responses).

def get_gemini_response(question):  # Define a function to get a response from the Gemini model.
    response = model.generate_content(question)  # Send the user's question to the Gemini model and store the response.
    return response.text  # Return only the text part of the model's response.

st.set_page_config(page_title="Q&A Demo")  # Set the title of the Streamlit web page.
st.header("Gemini LLM App")  # Display a header on the web page.
input = st.text_input("Input:",key="input")  # Create a text input field for the user to enter their question.
submit = st.button("Ask Question")  # Create a button that the user can click to submit their question.

if submit:  # Check if the submit button has been clicked.
    response = get_gemini_response(input)  # Get the response from the Gemini model using the user's input.
    st.subheader("The response is")  # Display a subheader to indicate the response.
    st.write(response)  # Display the response from the Gemini model on the web page.