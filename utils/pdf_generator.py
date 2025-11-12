import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_RIGHT

def generate_resume_pdf(data, filename):
    output_dir = "generated_resumes"
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    doc = SimpleDocTemplate(filepath, pagesize=A4,
                            rightMargin=40, leftMargin=300, topMargin=60, bottomMargin=60)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='RightAlign', alignment=TA_RIGHT))
    styles.add(ParagraphStyle(name='BoldBlack', textColor='black', fontName='Helvetica-Bold'))
    story = []

    story.append(Paragraph(f"<font size=20 color='#00ff88'><b>{data.get('name','')}</b></font>", styles["RightAlign"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(f"<b>Email:</b> {data.get('email','')}", styles["RightAlign"]))
    story.append(Paragraph(f"<b>Phone:</b> {data.get('phone','')}", styles["RightAlign"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(f"<b>Summary:</b> {data.get('summary','')}", styles["RightAlign"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>Technical Skills:</b>", styles["BoldBlack"]))
    story.append(Paragraph(data.get("technical_skills",""), styles["RightAlign"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Non-Technical Skills:</b>", styles["BoldBlack"]))
    story.append(Paragraph(data.get("non_technical_skills",""), styles["RightAlign"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Education:</b>", styles["BoldBlack"]))
    story.append(Paragraph(data.get("education",""), styles["RightAlign"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Certifications / Seminars:</b>", styles["BoldBlack"]))
    story.append(Paragraph(data.get("certifications",""), styles["RightAlign"]))
    story.append(Spacer(1, 10))

    for label, key in [("LinkedIn", "linkedin"), ("GitHub", "github"), ("Portfolio", "portfolio")]:
        url = data.get(key)
        if url:
            story.append(Paragraph(f"<b>{label}:</b> {url}", styles["RightAlign"]))
            story.append(Spacer(1, 8))

    doc.build(story)
    return filepath
