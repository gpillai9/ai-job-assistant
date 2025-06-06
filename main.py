from resume_parser import extract_resume_text
from job_scraper import scrape_indeed
'''
resume_path = "sample_data/sample_resume.pdf"
resume_text = extract_resume_text(resume_path)
print(resume_text)
'''
job_url = "https://www.ashbyhq.com/careers?ashby_jid=83e83bad-be57-4f31-94d1-10020a20ccae"
job_description = scrape_indeed(job_url)
if job_description:
    print("Job Description Extracted:\n")
    print(job_description)
else:
    print("Failed to extract job description.")