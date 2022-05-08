from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
username = os.environ.get('mymail')
password = os.environ.get('mypass')
options = webdriver.ChromeOptions()
options.add_argument("start-maximized") 
options.add_argument("disable-infobars") 
options.add_argument("--disable-extensions") 
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage") 
options.add_argument("--no-sandbox") 
options.add_argument("user-data-dir=/home/shubharthak/.config/google-chrome/")
options.headless = True
driver = webdriver.Chrome(executable_path='/home/shubharthak/.wdm/drivers/chromedriver/linux64/98.0.4758.80/chromedriver', options=options)
driver.get('https://www.google.com/android/find')
print(driver.title)
view = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="refresh-button-4068740523376078557"]/div')))
print('clicking the ring button')
btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="4068740523376078557"]/div/div/div[1]/div/button/div[1]'))).click()
print('clicked ring button')


