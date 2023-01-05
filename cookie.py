from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://orteil.dashnet.org/experiments/cookie/")

start_time = time.time()

while True:
    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()
    now_time = time.time()
    money = int(driver.find_element(By.CSS_SELECTOR, "#money").text)
    if now_time - start_time >= 5:
        mine = driver.find_element(By.ID, "buyMine")
        shipement = driver.find_element(By.ID, "buyShipment")
        alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab")
        portal = driver.find_element(By.ID, "buyPortal")
        time_machine = driver.find_element(By.ID, "buyTime machine")
        time_machine.click()
        portal.click()
        alchemy_lab.click()
        shipement.click()
        mine.click()
        start_time = time.time()
