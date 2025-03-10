# Multilingual Invoice Extractor with Gemini

This Streamlit application demonstrates how to use Google's Gemini LLM to extract information from invoice images, even across different languages.

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

1.  **Save the Python code:** Save the code as a `.py` file (e.g., `invoice_extractor.py`).
2.  **Open a terminal:** Navigate to the directory where you saved the file.
3.  **Run the Streamlit app:**

    ```bash
    streamlit run invoice_extractor.py
    ```

4.  **Open your browser:** Streamlit will provide a local URL (e.g., `http://localhost:8501`). Open this URL in your browser.

## How to Use

1.  **Upload an invoice image:** Click "Choose an image of invoice" and select a JPEG, JPG, or PNG image of an invoice.
2.  **Optional: Enter a prompt:** In the "Input prompt" field, you can enter specific questions about the invoice (e.g., "What is the total amount?", "Who is the vendor?"). If left blank the model will try to extract general information.
3.  **Click "Tell me about the invoice":** Click the button to send the image and prompt to the Gemini model.
4.  **View the response:** The extracted information from the invoice will be displayed below the button.

## Explanation

* **`.env` file:** Stores your Google Cloud API key securely.
* **Streamlit:** Provides the web interface for the application.
* **Google Generative AI:** Enables interaction with the Gemini LLM.
* **Pillow (PIL):** Used for opening and displaying the uploaded image.
* **`get_gemini_response()` function:** Sends the image and prompt to the Gemini model and returns the response.
* **`input_image_details()` function:** Prepares the uploaded image for processing by the Gemini model.
* **Default Prompt:** The application uses a default prompt to instruct the model to act as an invoice expert. This prompt can be modified to improve the model's accuracy.

## Notes

* The accuracy of the extracted information depends on the quality of the invoice image and the complexity of the invoice.
* The application is designed to handle multilingual invoices, but the performance may vary depending on the language.
* Ensure your API key has the correct permissions to access the Gemini API.
* The gemini-2.0-flash model is optimized for faster responses, so for complex or highly detailed invoices, other gemini models might yield better results.