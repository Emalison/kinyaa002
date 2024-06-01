from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

def job_function():
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    driver.get("https://id.heroku.com/login")
    time.sleep(10)
    username2 = driver.find_element_by_id("email")
    password2 = driver.find_element_by_id("password")
    sele = "palakiki@yandex.com"
    pos = "pala900!"
    # 0770244721
    username2.send_keys(sele)
    password2.send_keys(pos)
    time.sleep(2)

    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/form/button").click()
    time.sleep(7)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/form[2]/button").click()


    for x in range(30):
        driver.get("https://dashboard.heroku.com/apps/jespa?web-console=jespa")
        time.sleep(8)

        password23 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/input')
        list55 = "python bet.py"
        #zef = random.choice(list55)
        time.sleep(5)
        print("Aha")
        password23.send_keys(list55)
        #time.sleep(2)
        #driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/p/a[2]').click()
        time.sleep(3)
        driver.find_element_by_id("run-console-button").click()
        print("Aha")
        time.sleep(100)
        print("Aha")

    driver.get("https://dashboard.heroku.com/logout")
    time.sleep(5)
job_function()
