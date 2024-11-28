from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# import class for searching something in input box
from selenium.webdriver.common.by import By
# import libries for pressing or entering input
from selenium.webdriver.common.keys import Keys
import time
# providing webdriver
s = Service('C:/Users/Yogesh/Desktop/chromedriver.exe')
# stop automatic closing of crome
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
# calling crome 
driver = webdriver.Chrome(service=s,options=options)

driver.get('https://www.smartprix.com/')
# # find path of input box
# user_input = driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
# # writing input
# user_input.send_keys('smartprix')
# # pressing enter 
# user_input.send_keys(Keys.ENTER)

time.sleep(2)
# # selecting an link and click them

link1 = driver.find_element(by=By.XPATH,value="/html/body/div[1]/nav/ul/li[1]/a")
link1.click()
time.sleep(2)

link2 = driver.find_element(by=By.XPATH,value="/html/body/div[1]/main/aside/div/div[6]/div[2]/label[1]/input")
link2.click()
time.sleep(2)

link3 = driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/aside/div/div[5]/div[2]/label[1]/input')
link3.click()
time.sleep(2)

link4 = driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/aside/div/div[5]/div[2]/label[2]/input')
link4.click()
time.sleep(2)

old_height = driver.execute_script('return document.body.scrollHeight')
while True:
    next_page = driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/div[1]/div[2]/div[3]')
    next_page.click()
    time.sleep(1)
   
    new_height = driver.execute_script('return document.body.scrollHeight')
    print(old_height)
    print(new_height)
    if new_height==old_height:
        break

    old_height=new_height

html = driver.page_source

with open('smartprix.html','w',encoding='utf-8') as f:
    f.write(html)