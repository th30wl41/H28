#!python3
from selenium import webdriver
from datetime import datetime
import os
import autoit
import time
import sys
print('google Chrome is about to start... Please unlock your whatsapp using the QR code')
time.sleep(5)
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('How many times do you want your message to be sent? : '))
file_name = input('Enter the name of your file : ')
dt = datetime
x = os.path.abspath('.')
for cdir , dirs , files in os.walk(x):
	if os.path.isfile(os.path.join(cdir , file_name )) is True :
		file_path = os.path.join(cdir , file_name)
#Grab the required whatsapp group/user		
driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)).click()
print("everything is set! when it's time , your message and file will be automatically sent! good night" )
time.sleep(3)
#scheduling using datetime
while True : 
	if dt(dt.now().year,dt.now().month, dt.now().day,9,0,0,0)< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, 9, 15, 0 ,0):
#using xpath to grab the message box  		
		msg_box = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div' )
		time.sleep(3)
		for i in range(count) :
			msg_box.send_keys(msg)
#using class name to click on the send button			
			driver.find_element_by_class_name('_3M-N-').click()
		time.sleep(5)
#here we are using xpath again to access the file sending buttons		
		driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span').click()
		time.sleep(3)
		driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button').click()
		time.sleep(3)
#using autoit once the Chrome window of	uploading appear	
		autoit.control_focus("Open", "Edit1")
		autoit.control_set_text("Open","Edit1",(file_path))
		autoit.control_click("Open", "Button1")
		time.sleep(3)
#using xpath again to send the file.		
		whatsapp_send_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')
		whatsapp_send_button.click()
		print('message and file sent! thank you for using my tool ^_^ ')
		time.sleep(6)
		sys.exit()
	else : 
	    print('on hold , please wait...')
	    time.sleep(10)	



