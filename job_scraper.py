import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def scrape_indeed(url):
    service = Service('./chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get('https://www.google.com')
    print(driver.title)
    driver.quit()
    '''
    service = Service('./chromedriver.exe')  # update this path
    driver = webdriver.Chrome(service=service)

    driver.get(url)

    try:
        # Wait for the job description element to load if needed
        wait = WebDriverWait(driver, 10)
        job_desc_element = wait.until(EC.presence_of_element_located((By.ID, "overview")))
        job_desc_text = job_desc_element.text
    except Exception as e:
        print(f"Error: {e}")
        job_desc_text = None

    driver.quit()
    return job_desc_text
    '''