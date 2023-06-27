from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from math import *
browser=webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button0=browser.find_element(By.TAG_NAME, "button")
    h5=browser.find_element(By.CSS_SELECTOR, "h5#price")
    while h5.text!="$100":
        h5=browser.find_element(By.ID, "price")
    button0.click()
    x=browser.find_element(By.CSS_SELECTOR, "#input_value")
    input_=browser.find_element(By.TAG_NAME, "input")
    input_.send_keys(str(log(abs(12*sin(int(x.text))))))
    button=browser.find_element(By.CSS_SELECTOR, "button#solve")
    button.click()
finally:
    time.sleep(20)
    browser.quit()
