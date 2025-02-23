import chromedriver_autoinstaller as chromedriver
chromedriver.install()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
        price = WebDriverWait(browser, 12).until(
                EC.text_to_be_present_in_element((By.ID, "price"), "$100"))


        button = browser.find_element(By.ID, "book").click()

        x = browser.find_element(By.ID, "input_value").text
        result = math.log(abs(12 * math.sin(float(x))))

        field = browser.find_element(By.ID, "answer")
        field.send_keys(str(result))

        sub_button = browser.find_element(By.XPATH, "//button[text()='Submit']")
        sub_button.click()

finally:
        time.sleep(4)
        browser.quit()




