import streamlit as st  # Import the Streamlit library for creating web applications.
import google.generativeai as genai  # Import the Google Generative AI library.
import os  # Import the operating system library for interacting with the system.
import PyPDF2 as pdf  # Import PyPDF2 for working with PDF files.

from dotenv import load_dotenv  # Import the library to load environment variables from a .env file.
load_dotenv()  # Load the environment variables from the .env file into the system.

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Configure the Google Generative AI with your API key, fetched from the environment variables.

# Get Gemini Response
def get_gemini_response(input):  # Define a function to get a response from the Gemini model.
    model = genai.GenerativeModel("gemini-2.0-flash")  # Create an instance of the Gemini model (specifically, the "flash" version for faster responses).
    response = model.generate_content(input)  # Send the user's input to the Gemini model.
    return response.text  # Return the text part of the model's response.

# Extract text from pdf
def extract_text_from_pdf(pdf_file):  # Define a function to extract text from a PDF file.
    reader = pdf.PdfReader(pdf_file)  # Create a PDF reader object.
    text = ""  # Initialize an empty string to store the extracted text.
    for page in reader.pages:  # Iterate through the pages of the PDF.
        text += str(page.extract_text())  # Extract text from each page and append it to the 'text' string.
    return text  # Return the extracted text.

# Prompt Template
input_prompt = """
    Hey Act like a skilled or very experienced ATS(Application Tracking System) with a deep 
    understanding of tech field, software engineering, data science,bug data and eveyrthing related to tech field.
    You will be given a job description and a set of resume details. Your task is to review the resume.
    Based on the job description and the resume, provide a score out of 100 on how well the candidate and missing keywords with high accuracy.
    resume: {text}
    desscription: {job_description}

    I want the response in one single string having the structure
    {{"score": "score", "missing_keywords": [list of missing keywords]}}
    Example response: {{"score": 85, "missing_keywords": ["Python", "Data Analysis"]}}
"""  # Define a prompt template to guide the Gemini model's response.

# Streamlit App
st.title("ATS Tracking System")  # Set the title of the Streamlit web page.
st.text("Improve Your Resume ATS")  # Display a text message on the web page.
job_description = st.text_area("Job Description")  # Create a text area for the user to enter the job description.
# To get the pdf file
st.subheader("Paste Your Resume (PDF)")  # Display a subheader on the web page.
# file uploader
st.text("Upload Your Resume(PDF)")  # Display a text message on the web page.
uploaded_file = st.file_uploader("Upload Your Resume(PDF)...", type="pdf", help="Please upload the PDF")  # Create a file uploader for PDF files.

submit = st.button("Submit")  # Create a submit button.

if submit:  # Check if the submit button has been clicked.
    if uploaded_file is not None:  # Check if a file has been uploaded.
        text = extract_text_from_pdf(uploaded_file)  # Extract text from the uploaded PDF file.
        final_prompt = input_prompt.format(text=text, job_description=job_description) #format the input prompt with the extracted text and job description.
        response = get_gemini_response(final_prompt)  # Get the response from the Gemini model.
        response = response.replace("```json", "").replace("```", "").strip() #remove json code blocks from the response.
        st.subheader(response)  # Display the response on the web page.
    else:
        st.warning("Please upload a PDF resume.")  # Display a warning message if no file was uploaded.