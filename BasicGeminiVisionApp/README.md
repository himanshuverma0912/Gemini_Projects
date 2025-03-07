# Gemini Image Analysis Demo

This is a Streamlit web application that demonstrates how to use the Google Gemini Large Language Model (LLM) to analyze images. You can upload an image and optionally provide a text prompt to ask questions or get descriptions about the image.

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

1.  **Save the code:** Save the Python code as a `.py` file (e.g., `image_app.py`).
2.  **Open a terminal:** Navigate to the directory where you saved the file.
3.  **Run the Streamlit application:**
    ```bash
    streamlit run image_app.py
    ```
4.  **Open your browser:** Streamlit will provide a local URL (e.g., `http://localhost:8501`). Open this URL in your web browser.

## How to Use

1.  **Upload an image:** Click the "Choose an image..." button and select an image file (JPG, JPEG, or PNG).
2.  **Optional: Enter a prompt:** Type a question or description related to the image in the "Input Prompt" text field.
3.  **Click "Tell me about Image":** Click the button to send the image and prompt (if provided) to the Gemini model.
4.  **View the response:** The response from the Gemini model will be displayed below the button.

## Explanation

* **`.env` file:** This file securely stores your API key.
* **Streamlit:** This library simplifies the creation of interactive web applications in Python.
* **Google Generative AI:** This library facilitates interaction with Google's LLMs, including Gemini.
* **Pillow (PIL):** This library is used for image processing, allowing the application to open and display uploaded images.
* **Gemini Model ("gemini-2.0-flash"):** This is a fast version of the Gemini model used for image analysis.
* **`get_gemini_response()` function:** This function sends the image and optional text prompt to the Gemini model and returns the response.

## Notes

* Ensure your API key is correct and has the necessary permissions.
* The quality of the image analysis may vary depending on the image's complexity and the prompt provided.
* The `gemini-2.0-flash` model is designed for speed, so it might not be as detailed as other Gemini models.
* The application supports JPG, JPEG, and PNG image formats.