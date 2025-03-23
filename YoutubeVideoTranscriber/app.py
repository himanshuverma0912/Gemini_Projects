import streamlit as st  # Import the Streamlit library for creating web applications.
from dotenv import load_dotenv  # Import the library to load environment variables from a .env file.
load_dotenv()  # Load the environment variables from the .env file into the system.

import google.generativeai as genai  # Import the Google Generative AI library.
import os  # Import the operating system library for interacting with the system.
from youtube_transcript_api import YouTubeTranscriptApi  # Import the YouTubeTranscriptApi library to get video transcripts.

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))  # Configure the Google Generative AI with your API key, fetched from the environment variables.

prompt = """You are a Youtube video sumarizer.You will be taking the transcripted text and summarizing the entire video and providing the important summary in points within 250 words.Please provide the summary of the given text here:"""  # Define a prompt for the Gemini model to summarize the video.

def extract_transcript_details(youtube_video_url):  # Define a function to extract the transcript from a YouTube video URL.
    try:
        video_id = youtube_video_url.split("=")[1]  # Extract the video ID from the YouTube URL.
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)  # Get the transcript from the YouTube video.
        transcript = ""  # Initialize an empty string to store the transcript text.
        for i in transcript_text:  # Iterate through the transcript text.
            transcript += ""+i["text"]  # Append each segment of the transcript to the 'transcript' string.
        return transcript  # Return the extracted transcript text.
    except Exception as e:  # Handle any exceptions that occur during transcript extraction.
        raise e  # Raise the exception.

def generate_gemini_context(transcript_text,prompt):  # Define a function to generate a summary of the transcript using the Gemini model.
    model = genai.GenerativeModel("gemini-2.0-flash")  # Create an instance of the Gemini model (specifically, the "flash" version for faster responses).
    response = model.generate_content(prompt+transcript_text)  # Send the transcript text and prompt to the Gemini model.
    return response.text  # Return the generated summary text.

st.title("Youtube transcriber")  # Set the title of the Streamlit web page.
youtube_link = st.text_input("Enter youtube video link")  # Create a text input field for the user to enter the YouTube video link.

if youtube_link:  # Check if the user has entered a YouTube link.
    video_id = youtube_link.split("=")[1]  # Extract the video ID from the YouTube URL.
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg",use_container_width=True) # Display the thumbnail of the YouTube video.

if st.button("Get Detailed Notes"):  # Create a button that the user can click to generate the summary.
    transcript_text = extract_transcript_details(youtube_link)  # Extract the transcript from the YouTube video.
    if transcript_text:  # Check if the transcript was successfully extracted.
        summary = generate_gemini_context(transcript_text,prompt)  # Generate a summary of the transcript using the Gemini model.
        st.markdown("## Detailed Notes:")  # Display a header for the summary.
        st.write(summary)  # Display the generated summary on the web page.