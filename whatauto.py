import selenium.webdriver
from config import CHROME_PROFILE_PATH
import urllib
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def whatsappautomation(phone, message):
    options = selenium.webdriver.ChromeOptions()
    options.add_argument(CHROME_PROFILE_PATH)

    browser = selenium.webdriver.Chrome(executable_path='./chromedriver.exe',options= options)

    safe_string = urllib.parse.quote_plus(message)
    browser.get("https://api.whatsapp.com/send/?phone="+phone+"&text="+safe_string+"&app_absent=0")

    element1 = EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div/a'))
    WebDriverWait(browser, 20).until(element1)

    button1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div/a')
    button1.click()

    element = EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/a"))
    WebDriverWait(browser, 20).until(element)

    button2 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/a')
    button2.click()

    element1 = EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span"))
    WebDriverWait(browser, 30).until(element1)
    time.sleep(1)

    button3 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
    button3.click()
    browser.quit()
    
