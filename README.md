# 📄 AI Resume Analyzer & Job Matcher

An AI-powered resume analysis application built with **Python,
Streamlit, and Natural Language Processing (NLP)**. It helps job seekers
evaluate how closely their resumes match a job description by
identifying relevant skills, missing skills, and an overall resume match
score.

## 🚀 Features

-   **Resume Upload:** Upload your resume in PDF format.
-   **Job Description Analysis:** Paste a job description for
    comparison.
-   **Resume Text Extraction:** Extract text from PDF resumes.
-   **Skill Extraction:** Identify skills from resumes and job
    descriptions.
-   **Matching Skills:** Display skills that appear in both the resume
    and job requirements.
-   **Missing Skills Detection:** Highlight job-related skills not
    detected in the resume.
-   **Resume Match Score:** Calculate a similarity score between the
    resume and job description.
-   **Resume Recommendations:** Provide feedback based on the match
    score.
-   **Interactive Dashboard:** View analysis results in a user-friendly
    Streamlit interface.

## 🛠️ Technologies Used

-   Python
-   Streamlit
-   PyPDF2 (if used by the resume parser)
-   Natural Language Processing (NLP)
-   Text similarity / semantic similarity
-   HTML and CSS for custom interface styling

## 📂 Project Structure

``` text
AI-Resume-Analyzer/
├── app.py                 # Main Streamlit application
├── resume_parser.py       # Extract text from PDF resumes
├── skill_extractor.py     # Extract skills from text
├── matcher.py             # Calculate resume similarity
├── requirements.txt       # Project dependencies
├── .env                   # Optional local environment variables
├── .gitignore             # Files excluded from Git
└── README.md              # Project documentation
```

*Adjust filenames above to match your actual project files.*

## ⚙️ Installation and Setup

### 1. Clone the repository

``` bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2. Create a virtual environment

``` bash
python -m venv venv
```

Activate it on Windows:

``` bash
venv\\Scripts\\activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file, install the packages
required by your project modules. For example:

``` bash
pip install streamlit PyPDF2 scikit-learn
```

Install any additional dependencies imported by `resume_parser.py`,
`skill_extractor.py`, and `matcher.py`.

### 4. Run the application

``` bash
streamlit run app.py
```

The application should open in your browser. If it does not, visit the
local URL shown in the terminal, typically `http://localhost:8501`.

## 🧠 How It Works

1.  **Upload Resume:** The user uploads a PDF resume.
2.  **Enter Job Description:** The user pastes the target job
    description.
3.  **Extract Text:** The resume parser extracts readable text from the
    PDF.
4.  **Extract Skills:** The skill extractor identifies skills in both
    texts.
5.  **Compare Skills:** The application identifies matching and missing
    skills.
6.  **Calculate Similarity:** The matcher calculates a similarity score
    between the resume and job description.
7.  **Display Results:** The dashboard presents the score, skill
    analysis, and recommendation.

## 📊 Analysis Results

  -----------------------------------------------------------------------
  Metric                              Description
  ----------------------------------- -----------------------------------
  Resume Skills                       Number of skills detected in the
                                      resume

  Required Skills                     Number of skills detected in the
                                      job description

  Matching Skills                     Skills detected in both the resume
                                      and job requirements

  Missing Skills                      Job-related skills not detected in
                                      the resume

  Resume Match Score                  Overall text similarity score
  -----------------------------------------------------------------------

### Match score guidance

The application currently uses these thresholds:

-   **80--100%:** Excellent Match
-   **60--79%:** Good Match
-   **40--59%:** Moderate Match
-   **Below 40%:** Low Match

These are configurable guidelines, not validated probabilities of
getting hired.

## 🔐 Environment Variables and Security

If your implementation uses API keys, store them in a local `.env` file
and load them through environment variables.

Example:

``` env
YOUR_API_KEY=your_api_key_here
```

Never upload `.env` or expose secret API keys on GitHub.

Add these entries to `.gitignore`:

``` gitignore
.env
venv/
__pycache__/
*.py[cod]
.streamlit/secrets.toml
```

Only include environment variables that your code actually uses. The
supplied main application code does not itself require an API key.

## 🔮 Future Improvements

-   AI-generated resume improvement suggestions
-   Job-specific keyword optimization
-   Downloadable analysis reports
-   Support for DOCX resumes
-   Resume analysis history
-   Improved skill recognition using NLP models
-   Job recommendation functionality
-   Secure deployment as a public web application

## ⚠️ Limitations

-   The current interface accepts PDF resumes only.
-   Skill extraction accuracy depends on the skill extractor
    implementation.
-   Scanned PDFs may require OCR if they do not contain extractable
    text.
-   Similarity scores do not guarantee interview selection or hiring
    success.
-   Users should review detected skills and recommendations before
    updating their resumes.

## 👨‍💻 Author

**Shalom Gosain**\
B.Tech in Computer Science and Engineering \| AI/ML Engineer

-   **GitHub:** https://github.com/Shalom2002Gosain
-   **LinkedIn:** https://www.linkedin.com/in/shalom-gosain/
-   **Portfolio:** https://shalom2002gosain.github.io

## 📜 License

This project is available for educational and portfolio purposes. Add an
open-source license, such as the MIT License, if you want to permit
reuse and redistribution under its terms.
