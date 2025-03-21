# Gemini Nutrition Analysis App

This Streamlit application uses Google's Gemini LLM to analyze food images and provide nutritional information, including calorie counts and dietary breakdowns.

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

1.  **Save the Python code:** Save the code as a `.py` file (e.g., `nutrition_app.py`).
2.  **Open a terminal:** Navigate to the directory where you saved the file.
3.  **Run the Streamlit app:**

    ```bash
    streamlit run nutrition_app.py
    ```

4.  **Open your browser:** Streamlit will provide a local URL (e.g., `http://localhost:8501`). Open this URL in your browser.

## How to Use

1.  **Upload a food image:** Click "Choose an image..." and select a JPEG, JPG, or PNG image of food.
2.  **Click "Tel me about total calories":** Click the button to send the image to the Gemini model for analysis.
3.  **View the response:** The nutritional analysis, including calorie counts for each food item and a dietary breakdown, will be displayed.

## Explanation

* **`.env` file:** Stores your Google Cloud API key securely.
* **Streamlit:** Provides the web interface for the application.
* **Google Generative AI:** Enables interaction with the Gemini LLM.
* **Pillow (PIL):** Used for opening and displaying the uploaded image.
* **`get_gemini_response()` function:** Sends the image and a predefined prompt to the Gemini model and returns the response.
* **`input_image_setup()` function:** Prepares the uploaded image for processing by the Gemini model.
* **Default Prompt:** The application uses a predefined prompt to instruct the model to analyze the food image and provide nutritional information.

## Notes

* The accuracy of the nutritional analysis depends on the clarity and detail of the food image.
* The application provides an estimate of calories and dietary breakdowns. Consult a professional nutritionist for precise dietary advice.
* Ensure your API key has the correct permissions to access the Gemini API.
* The gemini-2.0-flash model is optimized for faster responses. For more complex dietary analysis, consider using other Gemini models.
* The application is designed to identify and process common food items.