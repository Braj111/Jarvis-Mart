import selenium.webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config import CHROME_PROFILE_PATH
import urllib
import time

ph = ['918804407259', '919470412429']
message = "Whatsapp Automation Test Message"
def whatsappautomation(ph, message):
    options = selenium.webdriver.ChromeOptions()
    options.add_argument(CHROME_PROFILE_PATH)
    #options.add_argument('headless')
    #options.add_argument('window-size=200x300')
    #options.add_argument("disable-gpu")



    browser = selenium.webdriver.Chrome(executable_path='./chromedriver.exe',options= options)

    #browser.minimize_window()

    safe_string = urllib.parse.quote_plus(message)
    browser.get("https://api.whatsapp.com/send/?phone="+ph+"&text="+safe_string+"&app_absent=0")
    #

    element0 = EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div/a'))
    WebDriverWait(browser, 20).until(element0)

    bt1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div/a')
    bt1.click()

    element = EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/a"))
    WebDriverWait(browser, 20).until(element)
    #element.click()
    #time.sleep(2)
    bt2 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/a')
    bt2.click()

    element1 = EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span"))
    WebDriverWait(browser, 30).until(element1)
    time.sleep(1)
    bt3 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
    bt3.click()
    browser.quit()
    
