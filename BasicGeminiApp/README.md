# Gemini LLM Q&A Demo

This is a simple web application that demonstrates how to use the Google Gemini Large Language Model (LLM) to answer questions.

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

1.  **Save the code:** Save the Python code as a `.py` file (e.g., `app.py`).
2.  **Open a terminal:** Navigate to the directory where you saved the file.
3.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
4.  **Open your browser:** Streamlit will provide a local URL (e.g., `http://localhost:8501`). Open this URL in your web browser.

## How to Use

1.  **Enter your question:** Type your question into the text input field.
2.  **Click "Ask Question":** Click the button to send your question to the Gemini model.
3.  **View the response:** The response from the Gemini model will be displayed below the button.

## Explanation

* **`.env` file:** This file stores your API key securely, preventing it from being exposed in your code.
* **Streamlit:** This library makes it easy to create interactive web applications with Python.
* **Google Generative AI:** This library allows you to interact with Google's LLMs, such as Gemini.
* **Gemini Model ("gemini-2.0-flash"):** This is a fast version of the Gemini model, suitable for quick responses.
* **`get_gemini_response()` function:** This function sends the user's question to the Gemini model and returns the response.

## Notes

* Ensure your API key is correct and has the necessary permissions.
* The quality of the responses may vary depending on the complexity of the question.
* The gemini-2.0-flash model is designed to be fast, and therefore may not be as thorough as other gemini models.