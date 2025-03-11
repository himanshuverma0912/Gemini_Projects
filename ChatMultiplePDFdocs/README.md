# Chat with Multiple PDFs using Gemini

This Streamlit application allows you to chat with the content of multiple PDF documents using Google's Gemini LLM.

## Prerequisites

Before running this application, ensure you have:

1.  **Python 3.7+ installed.**
2.  **A Google Cloud Project with the Gemini API enabled and an API key.**
3.  **The following Python libraries installed:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **A `.env` file in the same directory as your script, containing your API key:**

    ```
    GOOGLE_API_KEY=YOUR_API_KEY
    ```

    Replace `YOUR_API_KEY` with your actual Google Cloud API key.

## How to Run

1.  **Save the Python code:** Save the code as a `.py` file (e.g., `pdf_chat.py`).
2.  **Open a terminal:** Navigate to the directory where you saved the file.
3.  **Run the Streamlit app:**

    ```bash
    streamlit run pdf_chat.py
    ```

4.  **Open your browser:** Streamlit will provide a local URL (e.g., `http://localhost:8501`). Open this URL in your browser.

## How to Use

1.  **Upload PDF files:** In the sidebar, click "Upload your PDF files and click on submit" and select the PDF documents you want to chat with.
2.  **Click "Submit and Process":** Click the button to process the uploaded PDFs. This will extract the text, split it into chunks, and create a vector store.
3.  **Ask a question:** In the main area, enter your question in the "Ask question from pdf files" text input.
4.  **View the response:** The response from the Gemini model, based on the content of the PDFs, will be displayed below the input field.

## Explanation

* **`.env` file:** Stores your Google Cloud API key securely.
* **Streamlit:** Provides the web interface for the application.
* **PyPDF2:** Used for reading and extracting text from PDF files.
* **LangChain:** A framework for developing applications powered by language models.
* **`langchain-google-genai`:** LangChain integrations for Google Generative AI models.
* **FAISS:** Used for creating a vector store to efficiently search for relevant text chunks.
* **`get_pdf_text()` function:** Extracts text from the uploaded PDF documents.
* **`get_text_chunks()` function:** Splits the extracted text into smaller chunks.
* **`get_vector_store()` function:** Creates a FAISS vector store from the text chunks and embeddings.
* **`get_conversational_chain()` function:** Creates a question-answering chain using Gemini.
* **`user_input()` function:** Handles user input, retrieves relevant documents from the vector store, and generates a response using the conversational chain.
* **`main()` function:** Sets up the Streamlit application and handles user interactions.

## Notes

* The accuracy of the responses depends on the quality and content of the PDF documents.
* The application creates and saves a local FAISS index (`faiss_index`) for efficient document retrieval. This index will be used for subsequent queries.
* Ensure your API key has the correct permissions to access the Gemini API.
* The gemini-2.0-flash model is optimized for faster responses, so for very complex or detailed queries, other gemini models might yield better results.
* The application handles multiple pdf files, and combines the text from all of them before creating the vector store.