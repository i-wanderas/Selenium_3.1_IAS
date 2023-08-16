import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

pole_f_name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[1]')
pole_f_name.send_keys('Ivan')

pole_l_name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[2]')
pole_l_name.send_keys('Ivanov')

pole_mail = browser.find_element(By.XPATH, '/html/body/div/form/div/input[3]')
pole_mail.send_keys('Ivanov@mail.com')

import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'lesson22_step7.py')           # добавляем к этому пути имя файла
input4 = browser.find_element(By.XPATH, '//*[@id="file"]')
input4.send_keys(file_path)

submit = browser.find_element(By.XPATH, '/html/body/div/form/button')
submit.click()

time.sleep(30)
browser.quit()