from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import datetime

#execute the shuffler file to create new seats
os.system('python shuffler.py')
#group name
target = '"RoyKedem"'
# path of the pictue
path = r"C:\Users\roykc\Documents\Projects\class-shuffler\pil_text_font.png"

# Replace below path with the absolute path of the \
#chromedriver in your computer
driver = webdriver.Chrome(r'C:\Users\roykc\Documents\Projects\class-shuffler\chromedriver.exe')

driver.get("https://web.whatsapp.com/")
# time.sleep()
wait = WebDriverWait(driver, 600)

#search group and clicks
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
print (group_title)
print ("Wait for few seconds")
group_title.click()

#while not(datetime.datetime.today().weekday() == 5):
#To send attachments
#click to add
driver.find_element_by_css_selector("span[data-icon='clip']").click()
#add file to send by file path
driver.find_element_by_css_selector("input[type='file']").send_keys(path)
#click to send
time.sleep(2)
driver.find_element_by_css_selector("span[data-icon='send-light']").click()
time.sleep(2)
driver.close()