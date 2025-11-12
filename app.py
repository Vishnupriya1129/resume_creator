from flask import Flask, render_template, request, jsonify, send_file
from utils.pdf_generator import generate_resume_pdf
from utils.ats_calculator import calculate_ats_score
import os
from datetime import datetime
import uuid

app = Flask(__name__)

# Ensure folders exist
os.makedirs("generated_resumes", exist_ok=True)

@app.route('/')
def home():
    return render_template('resume_form.html')

@app.route('/ats-checker')
def ats_checker_page():
    return render_template('ats_checker.html')

@app.route('/api/generate-resume', methods=['POST'])
def generate_resume():
    try:
        data = request.form.to_dict()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{data.get('name','user')}_resume_{timestamp}_{uuid.uuid4().hex[:6]}.pdf"
        filepath = generate_resume_pdf(data, filename)
        return jsonify({"success": True, "download_url": f"/download/{filename}"})
    except Exception as e:
        return jsonify({"success": False, "error": f"Failed to generate resume: {str(e)}"})

@app.route('/download/<filename>')
def download_resume(filename):
    filepath = os.path.join("generated_resumes", filename)
    if not os.path.exists(filepath):
        return jsonify({"error": "File not found"}), 404
    return send_file(filepath, as_attachment=True)

@app.route('/api/check-ats', methods=['POST'])
def check_ats():
    try:
        resume_file = request.files['resume']
        job_description = request.form['job_description']

        # Extract resume text (mock extraction)
        resume_text = resume_file.read().decode('latin1')

        # Calculate ATS score
        result = calculate_ats_score(resume_text, job_description)
        return jsonify({"success": True, **result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
