document.getElementById('resumeForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    // Get form data
    const formData = {
        fullname: document.getElementById('fullname').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        location: document.getElementById('location').value,
        summary: document.getElementById('summary').value,
        skills: document.getElementById('skills').value,
        experience: document.getElementById('experience').value,
        education: document.getElementById('education').value,
        certifications: document.getElementById('certifications').value,
        linkedin: document.getElementById('linkedin').value,
        github: document.getElementById('github').value,
        portfolio: document.getElementById('portfolio').value,
        job_title: document.getElementById('job_title').value
    };

    // Hide error message
    document.getElementById('errorMessage').style.display = 'none';
    document.getElementById('successMessage').style.display = 'none';

    try {
        // Send request to backend
        const response = await fetch('/api/generate-resume', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        const result = await response.json();

        if (response.ok) {
            // Show success message
            document.getElementById('successText').textContent = 'Resume generated successfully!';
            document.getElementById('downloadLink').href = result.download_url;
            document.getElementById('successMessage').style.display = 'flex';

            // Optionally auto-download
            // window.location.href = result.download_url;
        } else {
            throw new Error(result.error);
        }
    } catch (error) {
        document.getElementById('errorText').textContent = `Error: ${error.message}`;
        document.getElementById('errorMessage').style.display = 'block';
    }
});
