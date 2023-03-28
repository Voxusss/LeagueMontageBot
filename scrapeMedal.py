import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from dotenv import load_dotenv
import os

load_dotenv()

driver = webdriver.Chrome()
driver.get("https://medal.tv/login")
driver.find_element("xpath","/html/body/div[1]/div/div/div/div[2]/div/button[2]").click()
time.sleep(2)
driver.find_element("xpath","/html/body/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/form/div[1]/div/input").send_keys(os.getenv("MEDAL_USERNAME"))
driver.find_element("xpath","/html/body/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/form/div[2]/div/input").send_keys(os.getenv("MEDAL_PASSWORD"))
driver.find_element("xpath","/html/body/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/form/button").click()
driver.get("https://medal.tv/tags/annie")

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "div[class='sc-kLLXSd gXatEm']").click()
time.sleep(2)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
time.sleep(2)
scroll_amount = 200
for i in range(100):

    driver.execute_script(f"window.scrollBy(0, {scroll_amount})")
    JS_get_network_requests = "var performance = window.performance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;"
    network_requests = driver.execute_script(JS_get_network_requests)
    for n in network_requests:
        if ".m3u8" in n["name"]: 
            print(n["name"])
    time.sleep(2)

