from selenium import webdriver

driver = webdriver.Chrome()
# tarefa...
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
# driver.implicitly_wait(0.5)
title = driver.title
print(title)


input()