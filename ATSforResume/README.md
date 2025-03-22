# ATS Resume Analysis with Gemini

This Streamlit application uses Google's Gemini LLM to analyze resumes in PDF format against a given job description, simulating an Application Tracking System (ATS). It provides a score and highlights missing keywords.

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

1.  **Save the Python code:** Save the code as a `.py` file (e.g., `ats_resume_analysis.py`).
2.  **Open a terminal:** Navigate to the directory where you saved the file.
3.  **Run the Streamlit app:**

    ```bash
    streamlit run ats_resume_analysis.py
    ```

4.  **Open your browser:** Streamlit will provide a local URL (e.g., `http://localhost:8501`). Open this URL in your browser.

## How to Use

1.  **Enter the Job Description:** In the "Job Description" text area, paste the job description you want to compare the resume against.
2.  **Upload Your Resume (PDF):** Click "Upload Your Resume(PDF)..." and select the PDF resume you want to analyze.
3.  **Click "Submit":** Click the button to send the resume and job description to the Gemini model for analysis.
4.  **View the Response:** The application will display a score (out of 100) and a list of missing keywords from the resume, based on the job description.

## Explanation

* **`.env` file:** Stores your Google Cloud API key securely.
* **Streamlit:** Provides the web interface for the application.
* **Google Generative AI:** Enables interaction with the Gemini LLM.
* **PyPDF2:** Used for extracting text from PDF files.
* **`get_gemini_response()` function:** Sends the resume text and job description to the Gemini model and returns the response.
* **`extract_text_from_pdf()` function:** Extracts text from the uploaded PDF resume.
* **Prompt Template:** The application uses a predefined prompt to instruct the model to act as an ATS, analyze the resume, and provide a score and missing keywords.

## Notes

* The accuracy of the analysis depends on the clarity and content of the resume and job description.
* The application provides an estimate of the resume's suitability. Consider professional resume review services for in-depth analysis.
* Ensure your API key has the correct permissions to access the Gemini API.
* The gemini-2.0-flash model is used for faster responses. For more detailed analysis, consider using other Gemini models.
* The application expects the uploaded file to be a PDF.