import streamlit as st  # Import the Streamlit library for creating web applications.
from PyPDF2 import PdfReader  # Import PyPDF2 for reading PDF files.
from langchain.text_splitter import RecursiveCharacterTextSplitter  # Import LangChain's text splitter for breaking text into chunks.
import os  # Import the operating system library for interacting with the system.
import io  # Import the io module for working with input/output streams.
from io import BytesIO  # Import BytesIO for working with in-memory byte streams.

from langchain_google_genai import GoogleGenerativeAIEmbeddings  # Import LangChain's Google Generative AI embeddings.
from langchain_google_genai import ChatGoogleGenerativeAI  # Import LangChain's Google Generative AI chat model.
import google.generativeai as genai  # Import the Google Generative AI library.
from langchain_community.vectorstores import FAISS  # Import FAISS for creating vector stores.
from langchain.chains.question_answering import load_qa_chain  # Import LangChain's question-answering chain.
from langchain.prompts import PromptTemplate  # Import LangChain's prompt template.
from dotenv import load_dotenv  # Import the library to load environment variables from a .env file.

load_dotenv()  # Load the environment variables from the .env file into the system.

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Configure the Google Generative AI with your API key, fetched from the environment variables.

def get_pdf_text(pdf_docs):  # Define a function to extract text from PDF documents.
    text=""  # Initialize an empty string to store the extracted text.
    for pdf in pdf_docs:  # Iterate through the uploaded PDF documents.
        pdf_bytes = pdf.read()  # Read the PDF file into bytes.
        pdf_file = io.BytesIO(pdf_bytes)  # Create a file-like object from the bytes.
        pdf_reader = PdfReader(pdf_file)  # Create a PDF reader object from the file-like object.
        for page in pdf_reader.pages:  # Iterate through the pages of the PDF.
            text+=page.extract_text()  # Extract text from each page and append it to the 'text' string.
    return text  # Return the extracted text.

def get_text_chunks(text):  # Define a function to split the text into smaller chunks.
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 10000,chunk_overlap = 1000)  # Create a recursive character text splitter.
    chunks = text_splitter.split_text(text)  # Split the text into chunks.
    return chunks  # Return the list of text chunks.

def get_vector_store(text_chunks):  # Define a function to create a vector store from the text chunks.
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")  # Create embeddings using Google Generative AI.
    vecotr_store = FAISS.from_texts(text_chunks,embedding = embeddings)  # Create a FAISS vector store from the text chunks and embeddings.
    vecotr_store.save_local("faiss_index") #save the vector store locally.

def get_conversational_chain():  # Define a function to create a conversational chain for question answering.
    prompt_template = """Answer the question as detailed as possible from the provided context,make sure to provide all the details, if the answer is not in provided context just say, "answer is not available in the context",don't provide the wrong answer \n\n
    Context : \n {context} ? \n
    Question : \n {question} \n
    Answer :
    """  # Define a prompt template for the question-answering chain.

    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=0.3)  # Create a ChatGoogleGenerativeAI model.
    prompt = PromptTemplate(template=prompt_template,input_variables=["context","question"])  # Create a prompt template object.
    chain = load_qa_chain(model,chain_type="stuff",prompt=prompt)  # Create a question-answering chain.
    return chain  # Return the question-answering chain.

def user_input(user_question):  # Define a function to handle user input and generate a response.
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")  # Create embeddings using Google Generative AI.
    new_db = FAISS.load_local("faiss_index",embeddings,allow_dangerous_deserialization=True)  # Load the local FAISS vector store.
    docs = new_db.similarity_search(user_question)  # Perform a similarity search to find relevant documents.
    chain = get_conversational_chain()  # Get the conversational chain.
    response = chain(  # Process the user's question using the conversational chain.
        {
            "input_documents" : docs,  # Pass the relevant documents to the chain.
            "question" : user_question  # Pass the user's question to the chain.
        },
        return_only_outputs=True  # Return only the output text.
    )
    print(response) # print the response to the terminal.
    st.write("Reply : ",response["output_text"])  # Display the response on the web page.

def main():  # Define the main function.
    st.set_page_config("Chat with multiple PDFs")  # Set the page configuration.
    st.header("Chat with multiple PDFs")  # Display a header on the web page.
    user_question = st.text_input("Ask question from pdf files")  # Create a text input field for the user's question.
    if user_question:  # Check if the user has entered a question.
        user_input(user_question)  # Process the user's question.
    with st.sidebar:  # Create a sidebar.
        st.title("Menu : ")  # Display a title in the sidebar.
        pdf_docs = st.file_uploader("Upload your PDF files and click on submit",type="pdf",accept_multiple_files=True)  # Create a file uploader for PDF documents.
        if st.button("Submit and Process"):  # Create a submit button.
            with st.spinner("Processing"):  # Display a spinner while processing.
                raw_text = get_pdf_text(pdf_docs)  # Extract text from the uploaded PDF documents.
                text_chunks = get_text_chunks(raw_text)  # Split the extracted text into chunks.
                get_vector_store(text_chunks)  # Create a vector store from the text chunks.
                st.success("Done")  # Display a success message.

if __name__=="__main__":  # Check if the script is being run directly.
    main()  # Call the main function.