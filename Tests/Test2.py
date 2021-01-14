from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

s=Service("C:\\Selenium\\chromedriver.exe")

#driver = webdriver.Chrome(service=s)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com")
username=driver.find_element_by_name("txtUsername")
print(type(username))
enableStatus=username.is_enabled()
displayStatus=username.is_displayed()
print(enableStatus)
print(displayStatus)
username.clear()
attrData=username.get_attribute("type")
fontvalue=username.value_of_css_property("font-size")
print(attrData)
print(fontvalue)
username.send_keys("Admin")

password=driver.find_element_by_id("txtPassword")
password.send_keys("admin123")
loginButton=driver.find_element_by_class_name("button")
loginButton.click()

driver.quit()