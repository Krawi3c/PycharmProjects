import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from threading import Timer


def click_cookie():
    cookie = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[15]/div[8]/button')
    cookie.click()

def click_consent():
    consent = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p')
    consent.click()

def choose_language():
    my_language = driver.find_element(By.ID, "langSelect-PL")
    my_language.click()

def upgrade():
    upgrades_shop = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[19]/div[3]/div[5]')
    upgrades = upgrades_shop.find_elements(By.CLASS_NAME, "enabled")
    for upgrade in upgrades:
        upgrade.click()
def buy_item():
    shop = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[19]/div[3]/div[6]')
    items = shop.find_elements(By.CLASS_NAME, "enabled")
    for item in items:
        item.click()
chrome_driver_path = "C:\Development\chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("https://orteil.dashnet.org/cookieclicker/")

consent = Timer(0.5, click_consent)
consent.start()
language = Timer(1.5, choose_language)
language.start()
time.sleep(6)
while True:
    click_cookie()
    upgrade()
    buy_item()
