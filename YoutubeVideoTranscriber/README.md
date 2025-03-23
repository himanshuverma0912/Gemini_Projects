# YouTube Video Summarizer with Gemini

This Streamlit application allows you to summarize YouTube video transcripts using Google's Gemini LLM. You provide a YouTube video link, and the application extracts the transcript, summarizes it, and displays the summary.

## Features

* **YouTube Link Input:** Allows users to input a YouTube video link.
* **Transcript Extraction:** Extracts the video transcript using the `youtube_transcript_api` library.
* **Video Thumbnail Display:** Displays the thumbnail of the YouTube video.
* **Summary Generation:** Uses the Gemini LLM to generate a concise summary of the transcript.
* **Detailed Notes Display:** Presents the generated summary in a readable format.

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

1.  **Save the Python code:** Save the code as a `.py` file (e.g., `youtube_summarizer.py`).
2.  **Open a terminal:** Navigate to the directory where you saved the file.
3.  **Run the Streamlit app:**

    ```bash
    streamlit run youtube_summarizer.py
    ```

4.  **Open your browser:** Streamlit will provide a local URL (e.g., `http://localhost:8501`). Open this URL in your browser.

## How to Use

1.  **Enter YouTube Link:** Paste the YouTube video link into the "Enter youtube video link" text input.
2.  **View Video Thumbnail:** The application will display the thumbnail of the YouTube video.
3.  **Click "Get Detailed Notes":** Click the button to extract the transcript and generate a summary.
4.  **View Summary:** The generated summary will be displayed on the page.

## Code Flow Explanation

1.  **Import Libraries:** The application imports necessary libraries, including Streamlit, dotenv, Google Generative AI, os, and youtube-transcript-api.
2.  **Load Environment Variables:** The `.env` file is loaded to retrieve the Google API key.
3.  **Configure Gemini API:** The Google Generative AI library is configured with the API key.
4.  **Define Prompt:** A prompt is defined to instruct the Gemini model to summarize the transcript.
5.  **`extract_transcript_details()` function:**
    * Takes a YouTube video URL as input.
    * Extracts the video ID from the URL.
    * Uses the `YouTubeTranscriptApi.get_transcript()` function to fetch the video transcript.
    * Concatenates the transcript segments into a single string.
    * Returns the extracted transcript text.
    * Handles potential exceptions during transcript extraction.
6.  **`generate_gemini_context()` function:**
    * Takes the transcript text and prompt as input.
    * Creates an instance of the Gemini model.
    * Sends the prompt and transcript to the Gemini model for summarization.
    * Returns the generated summary text.
7.  **Streamlit App Setup:**
    * Sets the page title.
    * Creates a text input field for the YouTube link.
    * Displays the video thumbnail if a link is provided.
    * Creates a "Get Detailed Notes" button.
8.  **Button Click Logic:**
    * When the button is clicked:
        * The `extract_transcript_details()` function is called to get the transcript.
        * If the transcript is extracted successfully:
            * The `generate_gemini_context()` function is called to generate the summary.
            * The summary is displayed on the page.

## Notes

* Ensure your API key has the correct permissions to access the Gemini API.
* The accuracy of the summary depends on the quality of the video transcript and the Gemini model's capabilities.
* The `youtube-transcript-api` library might not work for all YouTube videos (e.g., videos with disabled transcripts).
* The gemini-2.0-flash model is used for faster responses. For more detailed summaries, consider using other Gemini models.