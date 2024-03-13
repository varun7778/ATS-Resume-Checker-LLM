# ATS-Resume-Checker-LLM

This project utilizes Streamlit to create a web application called Smart ATS that helps users improve their resumes for Applicant Tracking Systems (ATS). 

Model Used: 'gemini-pro'

### Functionalities:

* JD Match Percentage: Analyzes how well a resume matches a given job description and provides a percentage score.
* Missing Keywords: Identifies keywords present in the job description but missing from the resume.
* Cover Letter Generation: Generates a cover letter tailored to the specific job description using information extracted from the resume.

### Technologies Used:

* Streamlit: Python library for building web apps.
* Google GenerativeAI: Google's API for accessing large language models like Gemini.
* PyPDF2: Python library for working with PDF files.
* dotenv: Python library for managing environment variables.

### Setup Instructions:

1. Install Libraries:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a Google Cloud Project and Enable GenerativeAI:
   - Follow Google's instructions to create a project and enable the GenerativeAI service ([https://cloud.google.com/ai/generative-ai](https://cloud.google.com/ai/generative-ai))
3. Create a `.env` File:
   - Create a file named `.env` in your project directory.
   - Add the following line, replacing `YOUR_API_KEY` with your actual GenerativeAI API key:
     ```
     GOOGLE_API_KEY=YOUR_API_KEY
     ```

### Running the App:

1. Open a terminal in your project directory.
2. Run the following command:
   ```bash
   streamlit run app.py
   ```
3. This will launch the Streamlit app in your web browser.

### How to Use the App:

1. Enter the Job Description in the text area.
2. Upload your resume as a PDF file.
3. Click the desired button:
    * Main: Provides a summary of the resume analysis using the default prompt (displays all functionalities).
    * Get Match: Calculates the percentage match between the resume and the job description.
    * Get Missing Keywords: Identifies missing keywords from the job description.
    * Get Cover Letter: Generates a cover letter based on the resume and job description (uses a modified prompt).

The results will be displayed below the respective buttons.
