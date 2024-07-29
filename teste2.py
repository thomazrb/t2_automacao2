from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("log-level=3")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.implicitly_wait(0.5)
title = driver.title
print(title)
text_box = driver.find_element(by=By.XPATH, value='/html/body/main/div/form/div/div[1]/label[1]/input')
text_box.send_keys("Oreia Seca")
submit_button = driver.find_element(by=By.TAG_NAME, value="button")
# ActionChains(driver).context_click(text_box).perform()
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text
print(text)
driver.implicitly_wait(0.5)
driver.back()
driver.quit()