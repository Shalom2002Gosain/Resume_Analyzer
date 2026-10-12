import streamlit as st

from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from matcher import calculate_similarity


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #6b7280;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 24px;
        font-weight: 600;
        margin-top: 20px;
    }

    .score-card {
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #e5e7eb;
        margin-bottom: 20px;
    }

    .score {
        font-size: 45px;
        font-weight: 700;
    }

    .skill-box {
        padding: 8px 12px;
        border-radius: 8px;
        border: 1px solid #e5e7eb;
        margin: 5px 0;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">📄 AI Resume Analyzer & Job Matcher</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Analyze your resume against a job description using NLP and '
    'semantic similarity.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# INPUT SECTION
# ============================================================

col1, col2 = st.columns(2)


with col1:

    st.markdown(
        '<div class="section-title">📄 Resume</div>',
        unsafe_allow_html=True
    )

    resume_file = st.file_uploader(
        "Upload your resume",
        type=["pdf"],
        help="Upload your resume in PDF format."
    )


with col2:

    st.markdown(
        '<div class="section-title">💼 Job Description</div>',
        unsafe_allow_html=True
    )

    job_description = st.text_area(
        "Paste the job description",
        height=200,
        placeholder=(
            "Paste the complete job description here..."
        )
    )


st.write("")


# ============================================================
# ANALYZE BUTTON
# ============================================================

analyze = st.button(
    "🔍 Analyze Resume",
    use_container_width=True,
    type="primary"
)


# ============================================================
# ANALYSIS
# ============================================================

if analyze:

    # Validate resume
    if resume_file is None:

        st.error(
            "Please upload your resume before starting the analysis."
        )

        st.stop()


    # Validate job description
    if not job_description.strip():

        st.error(
            "Please enter a job description before starting the analysis."
        )

        st.stop()


    # ========================================================
    # EXTRACT RESUME TEXT
    # ========================================================

    with st.spinner("Analyzing your resume..."):

        resume_text = extract_text_from_pdf(
            resume_file
        )


        # ====================================================
        # EXTRACT SKILLS
        # ====================================================

        resume_skills = extract_skills(
            resume_text
        )

        job_skills = extract_skills(
            job_description
        )


        # ====================================================
        # MATCHING SKILLS
        # ====================================================

        matching_skills = [
            skill
            for skill in resume_skills
            if skill in job_skills
        ]


        # ====================================================
        # MISSING SKILLS
        # ====================================================

        missing_skills = [
            skill
            for skill in job_skills
            if skill not in resume_skills
        ]


        # ====================================================
        # SIMILARITY SCORE
        # ====================================================

        similarity_score = calculate_similarity(
            resume_text,
            job_description
        )


    # ========================================================
    # RESULTS
    # ========================================================

    st.divider()

    st.markdown(
        '<div class="section-title">📊 Resume Analysis</div>',
        unsafe_allow_html=True
    )

    # ========================================================
    # SCORE
    # ========================================================

    st.markdown(
        f"""
        <div class="score-card">
            <div>Resume Match Score</div>
            <div class="score">{similarity_score}%</div>
            <div>Overall similarity with the job description</div>
        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # SUMMARY METRICS
    # ========================================================

    metric1, metric2, metric3, metric4 = st.columns(4)


    with metric1:

        st.metric(
            "Resume Skills",
            len(resume_skills)
        )


    with metric2:

        st.metric(
            "Required Skills",
            len(job_skills)
        )


    with metric3:

        st.metric(
            "Matching Skills",
            len(matching_skills)
        )


    with metric4:

        st.metric(
            "Missing Skills",
            len(missing_skills)
        )


    st.write("")


    # ========================================================
    # SKILL ANALYSIS
    # ========================================================

    col1, col2 = st.columns(2)


    # ========================================================
    # RESUME SKILLS
    # ========================================================

    with col1:

        st.subheader(
            "🛠️ Skills Detected in Resume"
        )

        if resume_skills:

            for skill in resume_skills:

                st.write(
                    f"✅ {skill}"
                )

        else:

            st.info(
                "No skills were detected in the resume."
            )


    # ========================================================
    # JOB REQUIREMENTS
    # ========================================================

    with col2:

        st.subheader(
            "💼 Skills Required by Job"
        )

        if job_skills:

            for skill in job_skills:

                st.write(
                    f"📌 {skill}"
                )

        else:

            st.info(
                "No required skills were detected."
            )


    st.divider()


    # ========================================================
    # MATCHING & MISSING SKILLS
    # ========================================================

    col1, col2 = st.columns(2)


    # ========================================================
    # MATCHING SKILLS
    # ========================================================

    with col1:

        st.subheader(
            "✅ Matching Skills"
        )

        if matching_skills:

            for skill in matching_skills:

                st.success(
                    skill
                )

        else:

            st.info(
                "No matching skills were found."
            )


    # ========================================================
    # MISSING SKILLS
    # ========================================================

    with col2:

        st.subheader(
            "⚠️ Missing Skills"
        )

        if missing_skills:

            for skill in missing_skills:

                st.warning(
                    skill
                )

        else:

            st.success(
                "Your resume contains all detected job skills."
            )


    # ========================================================
    # RECOMMENDATION
    # ========================================================

    st.divider()

    st.subheader(
        "💡 Resume Recommendation"
    )


    if similarity_score >= 80:

        st.success(
            "Excellent Match — Your resume is strongly aligned "
            "with the job requirements."
        )


    elif similarity_score >= 60:

        st.info(
            "Good Match — Consider adding some missing skills "
            "and relevant keywords to improve your resume."
        )


    elif similarity_score >= 40:

        st.warning(
            "Moderate Match — Your resume should be tailored "
            "more closely to the job description."
        )


    else:

        st.error(
            "Low Match — Consider significantly tailoring your "
            "resume to the required skills and keywords."
        )


    # ========================================================
    # EXTRACTED TEXT
    # ========================================================

    with st.expander(
        "📃 View Extracted Resume Text"
    ):

        st.text_area(
            "Resume Content",
            resume_text,
            height=400
        )