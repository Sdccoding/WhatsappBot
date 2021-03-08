#Copyright@Souhardya & Amartya.
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time
from datetime import datetime

driver = webdriver.Chrome() 

driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 
string = input("Type the common message that you want to send to people:")
no=int(input("Enter number of persons whom you want to send:"))
for i in range(no):
	targetprim=input("Put ur target name(Name of the person whom you want to send the message):")
	target='"'+targetprim+'"'
	x_arg = '//span[contains(@title,' + target + ')]'
	print(x_arg)
	group_title = wait.until(EC.presence_of_element_located(( 
		By.XPATH, x_arg))) 
	group_title.click() 
	inp_xpath='//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
	input_box = wait.until(EC.presence_of_element_located(( 
		By.XPATH, inp_xpath))) 
	#50 means 50 times
	for i in range(1):
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		strs = "Hi "+targetprim+" "+string
		input_box.send_keys(strs + Keys.ENTER)
		time.sleep(1) 
