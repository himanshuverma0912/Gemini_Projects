from dotenv import load_dotenv  # Import the library to load environment variables from a .env file.
load_dotenv()  # Load the environment variables from the .env file into the system.

import streamlit as st  # Import the Streamlit library for creating web applications.
import os  # Import the operating system library for interacting with the system.
import google.generativeai as genai  # Import the Google Generative AI library.

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))  # Configure the Google Generative AI with your API key, fetched from the environment variables.

model = genai.GenerativeModel("gemini-2.0-flash")  # Create an instance of the Gemini model (specifically, the "flash" version for faster responses).

chat = model.start_chat(history=[]) # Initialize a chat session with the Gemini model. This allows the model to remember previous messages.

def get_gemini_response(question):  # Define a function to get a response from the Gemini model.
    response = chat.send_message(question,stream=True)  # Send the user's question to the Gemini model and retrieve the response in chunks (stream=True).
    return response  # Return the response object, which contains the response chunks.

st.set_page_config(page_title="Conversational Q&A Demo")  # Set the title of the Streamlit web page.
st.header("Gemini LLM App")  # Display a header on the web page.

if 'chat_history' not in st.session_state: # Check if the chat history exists in the session state.
    st.session_state['chat_history']=[] # If not, create an empty list to store the chat history.

input = st.text_input("Input:",key="input")  # Create a text input field for the user to enter their question.
submit = st.button("Ask Question")  # Create a button that the user can click to submit their question.

if submit and input:  # Check if the submit button has been clicked and if the user has entered any text.
    response = get_gemini_response(input)  # Get the response from the Gemini model using the user's input.

    st.session_state['chat_history'].append(("You",input)) # Add the user's question to the chat history.

    st.subheader("The response is")  # Display a subheader to indicate the response.
    for chunk in response: # Iterate through the response chunks.
        st.write(chunk.text) # Display each chunk of the response on the web page.
        st.session_state['chat_history'].append(("Bot",chunk.text)) # Add the bot's response to the chat history.
st.subheader("The Chat History is ") # Display a subheader for the chat history.
for role,text in st.session_state['chat_history']: # Iterate through the chat history.
    st.write(f"{role} : {text}") # Display each message in the chat history, showing who said it (You or Bot).