import time

from selenium import webdriver
from selenium.webdriver.common.by import By


user_name = (By.ID, 'username')
user_password = (By.ID, 'password')
login_button = (By.CLASS_NAME, 'radius')
text_info = (By.CLASS_NAME, 'subheader')

driver_1 = webdriver.Chrome()
driver_1.get('https://the-internet.herokuapp.com/login')
driver_1.maximize_window()
print(f'Start test case invalid login')
time.sleep(2)
driver_1.find_element(*user_name).send_keys('Popescu')
time.sleep(2)
driver_1.find_element(*user_password).send_keys('asdf1234')
driver_1.find_element(*login_button).click()
time.sleep(2)

# TODO - sa validam ca logarea a esuat folosind acel banner cu wrong credentiale
print('Start case valid login')
driver_1.find_element(*user_name).send_keys('tomsmith')
time.sleep(2)
driver_1.find_element(*user_password).send_keys('SuperSecretPassword!')
driver_1.find_element(*login_button).click()
time.sleep(2)

# TODO verificam ca logarea a avut cu success

logout_button = (By.CSS_SELECTOR, '#content > div > a')
driver_1.find_element(*logout_button).click()
text = driver_1.find_element(*text_info).text
print(text)
#TODO test if text is corect/complete
#TODO sa nu mai completam noi manual (username)
