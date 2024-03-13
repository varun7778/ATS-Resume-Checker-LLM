import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv() ## load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

#Prompt Template

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field, diverse industries and current hiring trends. 
Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""
input_prompt_test = """
Consider You are a skilled or very experienced ATS (Application tracking system) with indepth knowledge of 
tech field, various industries and current hiring trends. Now Your task is to Match/Evaluate the resume
based on the given job application.Also,Consider the job market is highly competitve and provide the required 
assistance to improve the resumes. 
 Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""


input_prompt2="""
Hey Act Like a skilled or very experience ATS(Application Tracking System) with a deep understanding of tech field, diverse industries and current hiring trends. 
Your task is to evaluate the resume based on the given job description. You must consider the job market is very competitive and you should provide
best assistance for improving the resumes. Assign the percentage Matching based on Jd.
resume:{text}
description:{jd}

I want the response as one number that is the percentage Matching value (For example: Match = 67%)

"""

input_prompt3="""
Hey Act Like a hiring manager and a very experience ATS(Application Tracking System) with a deep understanding of tech field, diverse industries and current hiring trends mostly related to AI/ML engineering. 
Your task is to evaluate the resume based on the given job description. You must consider the job market is very competitive and you should provide
best assistance for improving the resumes. Find the missing keywords from the job description and my resume.

resume:{text}
description:{jd}

I want the response in one single string having all the MissingKeywords in an array.

"""

input_prompt4="""
Act like a hiring manager and expert cover letter writer who has dedicated over 15 years to mastering the craft and create cover letters for successful job applicants. 
You create compelling, customized cover letters that are tailored to the specific job description they're applying for.

You have a comprehensive understanding of diverse industries, current hiring trends, and Applicant Tracking Systems (ATS).

Your cover letters are compelling narratives that showcase the candidate's qualifications for the position but also their distinctive strengths. You know how to reveal individual strengths, career objectives, and challenges.

In order to fulfill your job, first take my information from my resume and then identify the key words, expertise & requirements the job demands, but also from the job description. 
Next, read, analyze and match my information to suit the job's requirements in their description. 
Finally, write the best cover letter possible, matching my information with the job description.

resume:{text}
description:{jd}

"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Main")
submit1 = st.button("Get Match")
submit2 = st.button("Get Missing Keywords")
submit3 = st.button("Get Cover Letter")


if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt)
        st.subheader(response)


if submit1:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt2)
        st.subheader(response)

if submit2:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt3)
        st.subheader(response)

if submit3:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt_test)
        st.subheader(response)