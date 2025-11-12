def calculate_ats_score(resume_text, job_description):
    resume_words = set(resume_text.lower().split())
    job_words = set(job_description.lower().split())
    matched = resume_words.intersection(job_words)
    total = len(job_words)
    score = int((len(matched) / total) * 100) if total > 0 else 0
    return {
        "ats_score": score,
        "matched_keywords": list(matched),
        "total_keywords": total
    }
