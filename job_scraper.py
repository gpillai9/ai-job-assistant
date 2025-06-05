import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
def scrape_indeed(url):
    service = Service('./chromedriver.exe')  # update this path
    driver = webdriver.Chrome(service=service)

    driver.get(url)
    try:
        # Wait for the job description element to load if needed
        job_desc_element = driver.find_element(By.ID, 'jobDescriptionText')
        job_desc_text = job_desc_element.text
    except Exception as e:
        print(f"Error: {e}")
        job_desc_text = None

    driver.quit()
    return job_desc_text
    