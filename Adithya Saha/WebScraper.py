from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed

try:
   
    driver.get("https://www.google.com")
 
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)

    results = driver.find_elements(By.XPATH, "//h3")
    for i, result in enumerate(results[:10]): 
        print(f"{i + 1}. {result.text}")

finally:
    driver.quit()
