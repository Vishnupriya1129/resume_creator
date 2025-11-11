import streamlit as st
import pdfkit
import tempfile

st.set_page_config(page_title="Resume Builder", page_icon="📄")

st.title("ATS-Friendly Resume Builder")

# ----- User Input -----
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
summary = st.text_area("Professional Summary")
skills = st.text_area("Skills (comma-separated)")
experience = st.text_area("Experience (one per line)")
education = st.text_area("Education (one per line)")

# ----- Generate PDF -----
def create_pdf(name, email, phone, summary, skills, experience, education):
    html_content = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1 {{ color: #333; font-size: 28px; }}
            h2 {{ color: #555; font-size: 20px; border-bottom: 1px solid #ccc; padding-bottom: 3px; }}
            p, li {{ font-size: 14px; line-height: 1.5; }}
            ul {{ padding-left: 20px; }}
        </style>
    </head>
    <body>
        <h1>{name}</h1>
        <p><strong>Email:</strong> {email} | <strong>Phone:</strong> {phone}</p>
        {f"<h2>Professional Summary</h2><p>{summary}</p>" if summary else ""}
        {f"<h2>Skills</h2><ul>" + "".join(f"<li>{s.strip()}</li>" for s in skills.split(',')) + "</ul>" if skills else ""}
        {f"<h2>Experience</h2><ul>" + "".join(f"<li>{e.strip()}</li>" for e in experience.split('\n')) + "</ul>" if experience else ""}
        {f"<h2>Education</h2><ul>" + "".join(f"<li>{ed.strip()}</li>" for ed in education.split('\n')) + "</ul>" if education else ""}
    </body>
    </html>
    """

    # Save PDF to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdfkit.from_string(html_content, temp_file.name)
    return temp_file.name

if st.button("Generate Resume PDF"):
    if not name:
        st.warning("Please enter your name!")
    else:
        pdf_file = create_pdf(name, email, phone, summary, skills, experience, education)
        with open(pdf_file, "rb") as f:
            st.download_button(
                label="Download Resume PDF",
                data=f,
                file_name=f"{name.replace(' ', '_')}_Resume.pdf",
                mime="application/pdf"
            )
        st.success("Your resume is ready!")
