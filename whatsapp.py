from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from speaking import speak
import os
import sys
user = str(sys.argv[1])
print(f'User : {user}')
message = sys.argv[2:]
text = ""
print(message)
print(type(message))
for x  in message:
    text += x + " " 
print(f'Message : {text}')
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
print(f'Writing message to {user}')
message_box = WebDriverWait(driver, 600).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')))
message_box.click()
print(text)
print(type(text))
message_box.send_keys(text + Keys.RETURN)
print('Message Sent Successfully')
time.sleep(2)
driver.quit()

