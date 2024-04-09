import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

email = "Krawiecki2001k@gmail.com"
password = "Krawiec730342138"

def decline_cookies():
    decline = driver.find_element(By.XPATH, '/html/body/div[1]/div/section/div/div[2]/button[2]')
    decline.click()
def log_in():
    login_page = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
    login_page.click()
    time.sleep(0.5)
    email_input = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[1]/input')
    password_input = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[2]/input')
    email_input.send_keys(email)
    email_input.send_keys(Keys.ENTER)
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

linkedin_page = "https://www.linkedin.com/jobs/search/?currentJobId=3365854641&f_" \
                "AL=true&f_PP=101496088&geoId=105072130&keywords=python&location=Polska&refresh=true&sortBy=R"
chrome_driver_path = "C:\Development\chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get(linkedin_page)
time.sleep(0.5)
decline_cookies()
time.sleep(0.5)
log_in()
while True:
    pass