from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import speech_recognition as sr
from speaking import speak

import os
import sys
user = str(sys.argv[1])
print(f'User : {user}')
options = webdriver.ChromeOptions()
options.add_argument("start-maximized") 
options.add_argument("disable-infobars") 
options.add_argument("--disable-extensions") 
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage") 
options.add_argument("--no-sandbox") 
options.add_argument("user-data-dir=/home/shubharthak/.config/google-chrome/")
#options.headless = True
driver = webdriver.Chrome(executable_path='/home/shubharthak/.wdm/drivers/chromedriver/linux64/98.0.4758.80/chromedriver', options=options)
driver.get('https://web.whatsapp.com/')
print(driver.title)
search_box = WebDriverWait(driver, 600).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')))
search_box.click()
print('Clicked the search button')
search_box.send_keys(user + Keys.RETURN)
message_box = WebDriverWait(driver, 10**5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/header/div[2]/div[2]/span')))
print(message_box.text)
while True:
    message_box = WebDriverWait(driver, 10**5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#main > header > div._24-Ff > div.zzgSd._3e6xi > span')))

    if 'online' in message_box.text or 'typing' in message_box.text:
        speak(f'{user} is Online') 
    else:
        print('Not online')
#/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/header/div[2]/div[2]/span
#main > header > div._24-Ff > div.zzgSd._3e6xi > span
#//*[@id="main"]/header/div[2]/div[2]
