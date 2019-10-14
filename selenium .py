from selenium import webdriver
import time
browser = webdriver.Firefox(executable_path = r'C:\Users\DANIAL\Desktop\New folder\geckodriver.exe')
browser.get('https://www.google.com') 
time.sleep(10)
browser.quit()