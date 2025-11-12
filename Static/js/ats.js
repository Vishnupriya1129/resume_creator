document.getElementById('atsForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    document.getElementById('atsErrorMessage').style.display = 'none';
    document.getElementById('atsResults').style.display = 'none';

    const form = e.target;
    const formData = new FormData();

    const resumeFile = form.querySelector('input[name="resume"]').files[0];
    if (!resumeFile) {
        return showAtsError('Please upload your resume PDF file.');
    }
    formData.append('resume', resumeFile);

    const jobDescription = form.querySelector('textarea[name="job_description"]').value.trim();
    if (!jobDescription) {
        return showAtsError('Please enter the job description.');
    }
    formData.append('job_description', jobDescription);

    const linkedinUrl = form.querySelector('input[name="linkedin_url"]').value.trim();
    if (linkedinUrl) formData.append('linkedin_url', linkedinUrl);

    const githubUrl = form.querySelector('input[name="github_url"]').value.trim();
    if (githubUrl) formData.append('github_url', githubUrl);

    const portfolioUrl = form.querySelector('input[name="portfolio_url"]').value.trim();
    if (portfolioUrl) formData.append('portfolio_url', portfolioUrl);

    document.getElementById('atsLoading').style.display = 'block';

    try {
        const response = await fetch('/api/check-ats', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (response.ok && result.success) {
            displayAtsResults(result.data);
        } else {
            showAtsError(result.error || 'Failed to check ATS score.');
        }
    } catch (error) {
        showAtsError('Network or server error.');
    } finally {
        document.getElementById('atsLoading').style.display = 'none';
    }
});

function displayAtsResults(data) {
    document.getElementById('atsResults').style.display = 'block';
    document.getElementById('scoreValue').textContent = data.score + '%';
    document.getElementById('scoreFeedback').textContent = data.feedback || '';

    document.getElementById('matchedCount').textContent = data.matched_count || 0;
    document.getElementById('totalKeywords').textContent = data.total_keywords || 0;

    const keywordsList = document.getElementById('keywordsList');
    keywordsList.innerHTML = '';

    (data.keywords || []).forEach(kw => {
        const span = document.createElement('span');
        span.textContent = kw.word;
        span.style.padding = '6px 10px';
        span.style.borderRadius = '12px';
        span.style.fontSize = '12px';
        span.style.fontWeight = '600';
        span.style.color = kw.matched ? '#155724' : '#721c24';
        span.style.backgroundColor = kw.matched ? '#d4edda' : '#f8d7da';
        span.style.border = kw.matched ? '1px solid #c3e6cb' : '1px solid #f5c6cb';
        keywordsList.appendChild(span);
    });
}

function showAtsError(message) {
    const errDiv = document.getElementById('atsErrorMessage');
    errDiv.querySelector('span').textContent = message;
    errDiv.style.display = 'block';
    document.getElementById('atsResults').style.display = 'none';
}
