from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import csv
import random

PATH = "C:\Program Files (x86)\chromedriver2.exe"
driver=webdriver.Chrome(PATH)


driver.get("https://mtamn.mta.ac.il/yedion/fireflyweb.aspx")
print('Enter your kours kod (קוד הקורס):')
kod= input()
#kod=142203
#kod=50003
uname="edenbm"
password="12Phoenixmed34"
msg_box=driver.find_element_by_xpath("//input[@id='R1C1']")
msg_box.send_keys(uname)#enter username

msg_box2=driver.find_element_by_xpath("//input[@id='R1C2']")
msg_box2.send_keys(password)#enter password

loginbtn=driver.find_element_by_xpath("//button[@id='loginbtn']")
loginbtn.send_keys(Keys.ENTER)#click login

menu=driver.find_element_by_xpath("//div[@id='kt_header_menu_mobile_toggle']")
menu.click() #click on the menu

time.sleep(5)

rishum=driver.find_element_by_xpath("//span[contains(text(),'רישום לקורסים')]")
rishum.click()#click on the first רישום לקורסים

time.sleep(3)

rishum2=driver.find_element_by_xpath("//div[@class='menu-item']")
rishum2.click()#click on the second רישום לקורסים

time.sleep(2)

kod_kours=driver.find_element_by_xpath("//input[@id='SubjectCode']")
kod_kours.send_keys(kod)#enter the kod kours in the textbox

btn_search=driver.find_element_by_xpath("//input[@id='searchButton']")
btn_search.click()
#click on kours search btn
if (len(driver.find_elements_by_xpath("//button[@id='REG1']")) > 0):  # if the button exist click on it (if the length of the button is bigger than 0...)
    driver.find_element_by_xpath("//button[@id='REG1']").click()
else:
   print('error,they need to be a btn course to continue')

i=1
# driver.find_element_by_xpath("//div[@class='modal-footer']").click()
# driver.refresh()

while(True):
    if (len(driver.find_elements_by_xpath("//span[@class='MessageInScreen']")) > 0):
        # //span[@class='MessageInScreen']
        # //div[@class='modal-footer']
        # driver.find_element_by_xpath("//div[@class='modal-footer']").click()
        driver.refresh()
    elif (len(driver.find_elements_by_xpath("//span[@class='fas fa-pencil-alt']")) > 0):
        driver.find_element_by_xpath("//span[@class='fas fa-pencil-alt']").click()
    else:break

















