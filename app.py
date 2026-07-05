import streamlit as st
from utils.pdf_generator import generate_resume_pdf
from models.career_profile import career_profile
from agents.coordinator_agent import run_career_analysis

st.set_page_config(
    page_title="Shakti AI",
    page_icon="🌸",
    layout="wide"
)
st.sidebar.title("🌸 Shakti AI")

st.sidebar.write("AI Career Coach")

st.sidebar.info("""
### Features

✅ Career Assessment

✅ AI Skill Gap Analysis

✅ AI Learning Roadmap

✅ AI Resume Builder

✅  AI Interview Coach

🤖 Powered by Google Gemini
""")

st.title("🌸 Shakti AI")
st.caption(
    "AI-Powered Career Restart Coach for Women Returning to Work"
)
st.subheader("Career Reboot for Women Returning to Work")
st.success("Your development environment is working successfully! 🎉")

st.header("Career Assessment")

name = st.text_input("Full Name")
email = st.text_input("Email Address")
education = st.selectbox(
    "Highest Education",
    [
        "B.Tech / B.E",
        "B.Sc",
        "B.Com",
        "BCA",
        "MCA",
        "M.Tech",
        "MBA",
        "Other"
    ]
)

previous_job = st.text_input("Previous Job Role")

# NEW FIELD
experience_years = st.number_input(
    "Years of Experience",
    min_value=0,
    max_value=30,
    step=1
)

# NEW FIELD
industry = st.selectbox(
    "Industry",
    [
        "IT",
        "Banking",
        "Healthcare",
        "Education",
        "Manufacturing",
        "Other"
    ]
)

skills = st.text_area(
    "Current Skills (Separate with commas)"
)

career_gap = st.number_input(
    "Career Gap (Years)",
    min_value=0,
    max_value=30,
    step=1
)

# NEW FIELD
career_break_reason = st.selectbox(
    "Reason for Career Break",
    [
        "Child Care",
        "Family Responsibilities",
        "Higher Education",
        "Health",
        "Personal Reasons",
        "Other"
    ]
)

# NEW FIELD
study_hours = st.selectbox(
    "Available Study Hours per Week",
    [
        "5 Hours",
        "10 Hours",
        "15 Hours",
        "20+ Hours"
    ]
)

# NEW FIELD
confidence = st.slider(
    "Confidence to Restart Career",
    1,
    10,
    5
)

goal = st.selectbox(
    "Career Goal",
    [
        "Software Testing",
        "Software Development",
        "Data Analytics",
        "AI / Machine Learning",
        "Project Management",
        "Not Sure Yet"
    ]
)
submitted = st.button("Analyze My Career")

if submitted:
    if not name.strip():
       st.error("Please enter your name.")
       st.stop()

    if not email.strip():
        st.error("Please enter your email address.")
        st.stop()

    if "@" not in email:
        st.error("Please enter a valid email address.")
        st.stop()

    if not previous_job.strip():
        st.error("Please enter your previous job role.")
        st.stop()

    if not skills.strip():
        st.error("Please enter at least one skill.")
        st.stop()

    career_profile["name"] = name
    career_profile["email"] = email
    career_profile["education"] = education
    career_profile["previous_job_title"] = previous_job
    career_profile["experience_years"] = experience_years
    career_profile["industry"] = industry
    career_profile["skills"] = [skill.strip() for skill in skills.split(",")]
    career_profile["career_break_years"] = career_gap
    career_profile["career_break_reason"] = career_break_reason
    career_profile["study_hours_per_week"] = study_hours
    career_profile["confidence_level"] = confidence
    career_profile["career_goal"] = goal
    #st.write(career_profile)
    progress = st.progress(0)
    st.success(f"Welcome {name}! 🌸")
    st.info("Your career profile has been successfully analyzed.")

    col1, col2 = st.columns(2)

    with col1:
     st.write(f"**Email:** {email}")
     st.write(f"**Education:** {education}")
     st.write(f"**Previous Job:** {previous_job}")

    with col2:
     st.write(f"**Career Gap:** {career_gap} years")
     st.write(f"**Career Goal:** {goal}")
     st.write(f"**Skills:** {skills}")
    score = max(100 - career_gap * 4, 45)

    st.subheader("📊 Career Readiness")

    st.metric(
    "Career Readiness Score",
    f"{score}/100"
)

    st.progress(score) 

    st.divider()
   
    with st.spinner("🤖 Shakti AI is analyzing your career profile..."):

      
      results = run_career_analysis(career_profile)
       
   
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📋 Assessment",
    "📊 Skill Gap",
    "🗺️ Roadmap",
    "📄 Resume",
    "🎤 Interview"
 ])

    with tab1:
     st.markdown(results["assessment"])

    st.download_button(
        "📥 Download Assessment",
        results["assessment"],
        file_name="assessment.txt",
        mime="text/plain",
    )

    with tab2:
     st.markdown(results["skill_gap"])

    with tab3:
     st.markdown(results["roadmap"])

    st.download_button(
        "📥 Download Roadmap",
        results["roadmap"],
        file_name="roadmap.txt",
        mime="text/plain",
    )

    with tab4:
     st.markdown(results["resume"])

    pdf_file = generate_resume_pdf(results["resume"])

    with open(pdf_file, "rb") as file: 

     st.download_button(
        "📥 Download Resume (PDF)",
        file,
        file_name="resume.pdf",
        mime="application/pdf",
    )

    with tab5:
     st.markdown(results["interview"])

    st.download_button(
        "📥 Download Interview Questions",
        results["interview"],
        file_name="interview_questions.txt",
        mime="text/plain",
    )

st.caption(
    "🌸 Shakti AI | Built with Streamlit, Python and Google Gemini AI"
)    