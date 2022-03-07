import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from pymongo import *
mongo_client = MongoClient('mongodb://localhost:27017')
users=mongo_client["covidassess"]["users"]

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

for user in users.find():
    driver.get('https://covid-assessment.publicboard.ca/?NoLogin=1')
    driver.implicitly_wait(1)
    print(driver.title)
    nameBox=driver.find_element(By.ID,"NoLoginID")
    nameBox.send_keys(user["studentID"])
    dobBox=driver.find_element(By.ID,"NoLoginDOB")
    dobBox.send_keys(user["dob"])
    driver.find_element(By.ID,"ContinueButton").click()
    driver.implicitly_wait(1)
    #driver.find_element(By.XPATH,"//input[@value='yes']").click()
    driver.execute_script("arguments[0].click();", driver.find_element(By.ID,"AdditionalQuestion1Yes"))