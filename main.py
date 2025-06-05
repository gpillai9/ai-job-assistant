from resume_parser import extract_resume_text
resume_path = "sample_data/sample_resume.pdf"
resume_text = extract_resume_text(resume_path)
print(resume_text)