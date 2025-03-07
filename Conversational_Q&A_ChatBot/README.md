# Gemini Conversational Q&A Demo

This is a Streamlit web application that demonstrates a conversational Q&A system using the Google Gemini Large Language Model (LLM). It allows you to have a continuous conversation with the Gemini model, remembering previous messages.

## Prerequisites

Before you can run this application, you need to:

1.  **Install Python:** Make sure you have Python 3.7 or later installed on your system.
2.  **Create a Google Cloud Project and Enable the Gemini API:**
    * Go to the Google Cloud Console.
    * Create a new project or select an existing one.
    * Enable the Gemini API for your project.
    * Generate an API key.
3.  **Install the required Python libraries:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Create a `.env` file:** In the same directory as your Python script, create a file named `.env` and add your Google API key:
    ```
    GOOGLE_API_KEY=YOUR_API_KEY
    ```
    Replace `YOUR_API_KEY` with your actual API key.

## How to Run

1.  **Save the code:** Save the Python code as a `.py` file (e.g., `chat_app.py`).
2.  **Open a terminal:** Navigate to the directory where you saved the file.
3.  **Run the Streamlit application:**
    ```bash
    streamlit run chat_app.py
    ```
4.  **Open your browser:** Streamlit will provide a local URL (e.g., `http://localhost:8501`). Open this URL in your web browser.

## How to Use

1.  **Enter your question:** Type your question into the text input field.
2.  **Click "Ask Question":** Click the button to send your question to the Gemini model.
3.  **View the response:** The response from the Gemini model will be displayed below the button.
4.  **Continue the conversation:** You can enter more questions, and the model will remember the previous messages in the conversation.
5.  **View the Chat History:** All of the conversation history will be displayed at the bottom of the page.

## Explanation

* **`.env` file:** This file securely stores your API key.
* **Streamlit:** This library simplifies the creation of interactive web applications in Python.
* **Google Generative AI:** This library facilitates interaction with Google's LLMs, including Gemini.
* **Gemini Model ("gemini-2.0-flash"):** This is a fast version of the Gemini model used for conversational interactions.
* **`chat = model.start_chat(history=[])`:** This line initializes a chat session, allowing the model to maintain context.
* **`get_gemini_response()` function:** This function sends the user's question to the Gemini model and returns the response in chunks, enabling streaming output.
* **`st.session_state`:** This Streamlit feature is used to store the chat history, ensuring that the conversation persists across interactions.

## Notes

* Ensure your API key is correct and has the necessary permissions.
* The quality of the conversation may vary depending on the complexity of the questions.
* The `gemini-2.0-flash` model is designed for speed, so it might not be as detailed as other Gemini models.
* The chat history is stored in the user's browser session, so it will be cleared when the browser tab is closed.