def job():
    def safi():
        from selenium import webdriver
        from datetime import datetime
        from selenium.webdriver.firefox.options import Options
        from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
        import os
        from selenium import webdriver
        from io import BytesIO
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

        options = webdriver.ChromeOptions()
        options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)
        driver.set_window_size(1366, 768)
        start_time = time.time()
        link = "https://splitthepot.games/betlion-ke/crashx/supersonic?token=e563240f-f670-4763-93d8-e5053f8cc1b4"
        driver.get(link)

        time.sleep(20)
        x_coordinate = 100
        y_coordinate = 200

        # Create an ActionChains object
        actions = ActionChains(driver)

        # Move the mouse cursor to the specified coordinates (X, Y)
        actions.move_by_offset(x_coordinate, y_coordinate).perform()

        # Perform a click at the specified coordinates
        actions.click().perform()

        time.sleep(5)
        # Scroll down 200 pixels

        driver.execute_script("window.scrollBy(0, 200);")
        driver.find_element(By.XPATH,
                            "/html/body/app-root/app-crashx/div/div/div[1]/stp-crash-multi/div[2]/div[2]/div[1]/div[1]/stp-form-field-group/stp-toggle/div/button/span[1]").click()
        # Locate the input field using the XPath
        input_field = driver.find_element(By.XPATH,
                                          "/html/body/app-root/app-crashx/div/div/div[1]/stp-crash-multi/div[2]/div[2]/div[2]/stp-all-in-one-stake-input/div[1]/div[2]/div[1]/input")

        # Clear the input field
        input_field.clear()

        # Write the value 1.00 into the input field
        input_field.send_keys("1.00")
        driver.find_element(By.XPATH,
                            "/html/body/app-root/app-crashx/div/div/div[1]/stp-crash-multi/div[2]/div[2]/div[1]/div[2]/stp-switch/label/span/span[1]").click()
        driver.find_element(By.XPATH,
                            "/html/body/app-root/app-crashx/div/div/div[1]/stp-crash-multi/div[2]/div[2]/div[2]/stp-all-in-one-stake-input/div[2]/button/span[2]").click()

        time.sleep(10)

        for x in range(3000):
            # Execute JavaScript to simulate a click at specific coordinates
            script = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 100 });" \
                     "document.elementFromPoint(1000, 200).dispatchEvent(evt);"
            driver.execute_script(script)
            script2 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 110 });" \
                      "document.elementFromPoint(1100, 110).dispatchEvent(evt);"
            driver.execute_script(script2)
            script3 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 120 });" \
                      "document.elementFromPoint(1100, 120).dispatchEvent(evt);"
            driver.execute_script(script3)

            script4 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 130 });" \
                      "document.elementFromPoint(1100, 130).dispatchEvent(evt);"
            driver.execute_script(script4)

            script5 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 140 });" \
                      "document.elementFromPoint(1100, 140).dispatchEvent(evt);"
            driver.execute_script(script5)

            script6 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 150 });" \
                      "document.elementFromPoint(1100, 150).dispatchEvent(evt);"
            driver.execute_script(script6)

            script7 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 160 });" \
                      "document.elementFromPoint(1100, 160).dispatchEvent(evt);"
            driver.execute_script(script7)

            script8 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 170 });" \
                      "document.elementFromPoint(1100, 170).dispatchEvent(evt);"
            driver.execute_script(script8)

            script9 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 180 });" \
                      "document.elementFromPoint(1100, 180).dispatchEvent(evt);"
            driver.execute_script(script9)
            script10 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 190 });" \
                       "document.elementFromPoint(1100, 190).dispatchEvent(evt);"
            driver.execute_script(script10)
            script11 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 200 });" \
                       "document.elementFromPoint(1100, 200).dispatchEvent(evt);"
            driver.execute_script(script11)

            script12 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 210 });" \
                       "document.elementFromPoint(1100, 210).dispatchEvent(evt);"
            driver.execute_script(script12)
            script13 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 220 });" \
                       "document.elementFromPoint(1100, 220).dispatchEvent(evt);"
            driver.execute_script(script13)

            script14 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 230 });" \
                       "document.elementFromPoint(1100, 230).dispatchEvent(evt);"
            driver.execute_script(script14)

            script5 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 240 });" \
                      "document.elementFromPoint(1100, 240).dispatchEvent(evt);"
            driver.execute_script(script5)

            script6 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 250 });" \
                      "document.elementFromPoint(1100, 250).dispatchEvent(evt);"
            driver.execute_script(script6)

            script17 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 260 });" \
                       "document.elementFromPoint(1100, 260).dispatchEvent(evt);"
            driver.execute_script(script17)

            script18 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 270 });" \
                       "document.elementFromPoint(1100, 270).dispatchEvent(evt);"
            driver.execute_script(script18)

            script19 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 280 });" \
                       "document.elementFromPoint(1100, 280).dispatchEvent(evt);"
            driver.execute_script(script19)
            script20 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 290 });" \
                       "document.elementFromPoint(1100, 290).dispatchEvent(evt);"
            driver.execute_script(script20)
            script21 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 300 });" \
                       "document.elementFromPoint(1100, 300).dispatchEvent(evt);"
            driver.execute_script(script21)
            script22 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 310 });" \
                       "document.elementFromPoint(1100, 310).dispatchEvent(evt);"
            driver.execute_script(script22)
            script23 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 320 });" \
                       "document.elementFromPoint(1100, 320).dispatchEvent(evt);"
            driver.execute_script(script23)

            script24 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 330 });" \
                       "document.elementFromPoint(1100, 330).dispatchEvent(evt);"
            driver.execute_script(script24)

            script25 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 340 });" \
                       "document.elementFromPoint(1100, 340).dispatchEvent(evt);"
            driver.execute_script(script25)

            script26 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 350 });" \
                       "document.elementFromPoint(1100, 350).dispatchEvent(evt);"
            driver.execute_script(script26)
            script27 = "var evt = new MouseEvent('click', { bubbles: true, cancelable: true, clientX: 1100, clientY: 360 });" \
                       "document.elementFromPoint(1100, 360).dispatchEvent(evt);"
            driver.execute_script(script27)
            print(x)
        for k in range(1):
            driver.quit()
            time.sleep(1)
            options = webdriver.ChromeOptions()
            options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            options.add_argument("--headless")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--no-sandbox")
            driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)
            driver.get(link)
            import time
            time.sleep(10)
            try:
                driver.find_element(By.XPATH,
                                    "/html/body/div[2]/div[4]/div/mat-dialog-container/div/div/app-free-round-available-dialog/app-modal-with-header/mat-dialog-actions/button[2]/span[2]").click()
                time.sleep(3)
                x_coordinate = 100
                y_coordinate = 200

                # Create an ActionChains object
                actions = ActionChains(driver)

                # Move the mouse cursor to the specified coordinates (X, Y)
                actions.move_by_offset(x_coordinate, y_coordinate).perform()

                # Perform a click at the specified coordinates
                actions.click().perform()

                time.sleep(2)
            except NoSuchElementException:
                x_coordinate = 100
                y_coordinate = 200

                # Create an ActionChains object
                actions = ActionChains(driver)

                # Move the mouse cursor to the specified coordinates (X, Y)
                actions.move_by_offset(x_coordinate, y_coordinate).perform()

                # Perform a click at the specified coordinates
                actions.click().perform()

                time.sleep(2)

            # INCLUDED
            try:

                time.sleep(1)
                # Scroll down by 200 pixels
                scroll_pixels = 200
                driver.execute_script(f"window.scrollBy(0, {scroll_pixels});")

                time.sleep(4)

                # clear
                jeje = driver.find_element(By.XPATH,
                                           "/html/body/app-root/app-crashx/div/div/div[1]/stp-crash-multi/div[2]/div[2]/div[1]/div[1]/stp-observable-input-field/stp-form-field/div/div[2]/div[2]/input")
                jeje.clear()
                random_choice = round(random.uniform(5.00, 8.00), 2)
                jeje.send_keys(str(random_choice))

                time.sleep(1)
                driver.find_element(By.XPATH,
                                    "/html/body/app-root/app-crashx/div/div/div[1]/stp-crash-multi/div[2]/div[2]/div[2]/stp-all-in-one-free-rounds/div[2]/button").click()

                time.sleep(115)


            except NoSuchElementException:
                # If the element is not found, print "none found"
                print("None found")
        driver.quit()
        end_time = time.time()
        # Calculate the elapsed time
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time:.2f} seconds")

    safi()
    print("DONE")


job()
