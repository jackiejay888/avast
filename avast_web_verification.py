# -*- coding: utf-8 -*-
'''
Created on 2021/06/01

@author: ZL Chen
@Task: Automate a sign up form

1.	Use form at https://demoqa.com/automation-practice-form
2.	Using Java or Python and Selenium, create at least 5 automated tests that will test the form’s functionality (you can include more scenarios you’d like to test, but don’t have to implement them)
3.	Send us a link to your Git repository with sources on a publicly accessible service (GitHub, GitLab, Bitbucket).

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from time import sleep
from os import system
import re, unittest, configparser, datetime

config = configparser.ConfigParser()
config.read('avast_web_verification.ini')
date_current_time = str(datetime.date.today())

class avast_web_verification(unittest.TestCase):
	def setUp(self):
		options = webdriver.ChromeOptions() 
		options.add_argument("--incognito") # incognito
		options.add_argument("start-maximized") # Maximization of Chrome browser
		self.driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
		self.driver.implicitly_wait(30)
		self.base_url = "https://www.google.com/"
		self.verificationErrors = []
		self.accept_next_alert = True
		self.driver.get("https://demoqa.com/automation-practice-form")
	
	def test_01_feature(self):
		driver = self.driver
		self.is_element_present(By.XPATH, "//div[@id='app']/div/div/div[2]/div[2]/div/h5")
		self.is_element_present(By.ID, "userName-label")
		self.is_element_present(By.ID, "userEmail-label")
		self.is_element_present(By.XPATH, "//div[@id='genterWrapper']/div")
		self.is_element_present(By.ID, "userNumber-label")
		self.is_element_present(By.ID, "dateOfBirth-label")
		self.is_element_present(By.ID, "subjects-label")
		self.is_element_present(By.XPATH, "(//label[@id='subjects-label'])[2]")
		self.is_element_present(By.XPATH, "(//label[@id='subjects-label'])[3]")
		self.is_element_present(By.ID, "currentAddress-label")
		self.is_element_present(By.ID, "stateCity-label")
		self.is_element_present(By.ID, "firstName")
		self.is_element_present(By.ID, "lastName")
		self.is_element_present(By.ID, "userEmail")
		self.is_element_present(By.XPATH, "//div[@id='genterWrapper']/div[2]/div/label")
		self.is_element_present(By.XPATH, "//div[@id='genterWrapper']/div[2]/div[2]/label")
		self.is_element_present(By.XPATH, "//div[@id='genterWrapper']/div[2]/div[3]/label")
		self.is_element_present(By.ID, "userNumber")
		self.is_element_present(By.ID, "dateOfBirthInput")
		self.is_element_present(By.XPATH, "//div[@id='subjectsContainer']/div/div")
		self.is_element_present(By.XPATH, "//div[@id='hobbiesWrapper']/div[2]/div/label")
		self.is_element_present(By.XPATH, "//div[@id='hobbiesWrapper']/div[2]/div[2]/label")
		self.is_element_present(By.XPATH, "//div[@id='hobbiesWrapper']/div[2]/div[3]/label")
		self.is_element_present(By.ID, "currentAddress")
		self.is_element_present(By.XPATH, "//div[@id='app']/div/div/div[2]/div[3]")
		self.is_element_present(By.ID, "submit")
		self.click(By.ID, "submit")
		sleep(0.2)
		driver.save_screenshot('test_01_' + date_current_time + '.png')

	def test_02_functional_sendkey(self):
		driver = self.driver
		self.functional_precondition_action()
		self.click(By.CSS_SELECTOR, "svg.css-19bqh2r > path")
		self.click(By.ID, "react-select-3-option-0")
		self.click(By.XPATH, "//div[@id='city']/div/div[2]/div")
		self.click(By.ID, "react-select-4-option-0")		
		self.click(By.ID, "submit")
		sleep(0.2)
		driver.save_screenshot('test_02_' + date_current_time + '.png')
		self.click(By.ID, "closeLargeModal")

	def test_03_functional_gender_filed(self):
		self.functional_precondition_action()
		for gender in range(1, 4):
			self.click(By.XPATH, "//div[@id='genterWrapper']/div[2]/div[" + str(gender) + "]/label")
		self.click(By.ID, "submit")
		sleep(0.2)
		self.driver.save_screenshot('test_03_' + date_current_time + '.png')
		self.click(By.ID, "closeLargeModal")

	def test_04_functional_hobbies_filed(self):
		self.functional_precondition_action()
		self.click(By.XPATH, "//div[@id='hobbiesWrapper']/div[2]/div[1]/label")
		for hobbies in range(1, 4):
			for loop in range(2):
				self.click(By.XPATH, "//div[@id='hobbiesWrapper']/div[2]/div[" + str(hobbies) + "]/label")
				sleep(0.1)
		self.click(By.XPATH, "//div[@id='hobbiesWrapper']/div[2]/div[3]/label")
		self.click(By.ID, "submit")
		sleep(0.2)
		self.driver.save_screenshot('test_04_' + date_current_time + '.png')
		self.click(By.ID, "closeLargeModal")

	def test_05_functional_state_city_filed(self):
		self.functional_precondition_action()
		for state in range(4):
			self.click(By.CSS_SELECTOR, "svg.css-19bqh2r > path")
			self.click(By.ID, "react-select-3-option-" + str(state))
			for city in range(2):
				self.click(By.XPATH, "//div[@id='city']/div/div[2]/div")
				self.click(By.ID, "react-select-4-option-" + str(city))
		self.click(By.ID, "submit")
		sleep(0.2)
		self.driver.save_screenshot('test_05_' + date_current_time + '.png')
		self.click(By.ID, "closeLargeModal")

	def functional_precondition_action(self):
		driver = self.driver
		driver.find_element_by_id("firstName").clear()
		driver.find_element_by_id("firstName").send_keys(config.get('functional', 'firstname'))
		driver.find_element_by_id("lastName").clear()
		driver.find_element_by_id("lastName").send_keys(config.get('functional', 'lastname'))
		driver.find_element_by_id("userEmail").clear()
		driver.find_element_by_id("userEmail").send_keys(config.get('functional', 'useremail'))
		self.click(By.XPATH, "//div[@id='genterWrapper']/div[2]/div/label")
		driver.find_element_by_id("userNumber").clear()
		driver.find_element_by_id("userNumber").send_keys(config.get('functional', 'usernumber'))
		self.click(By.XPATH, "//div[@id='subjectsContainer']/div/div")
		driver.find_element_by_id("subjectsInput").clear()
		driver.find_element_by_id("subjectsInput").send_keys(config.get('functional', 'subjectsinput'))
		self.click(By.XPATH, "//div[@id='hobbiesWrapper']/div[2]/div/label")
		driver.find_element_by_id("currentAddress").clear()
		driver.find_element_by_id("currentAddress").send_keys(config.get('functional', 'currentaddress'))

	def click(self, by, parameter_list):
		try:
			driver = self.driver
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, parameter_list))).click()
			sleep(0.5)
		except Exception as e:
			return False
		return True

	def is_element_present(self, how, what):
		try: 
			self.driver.find_element(by=how, value=what)
		except NoSuchElementException as e: 
			return False
		return True
	
	def is_alert_present(self):
		try: 
			self.driver.switch_to_alert()
		except NoAlertPresentException as e: 
			return False
		return True
	
	def close_alert_and_get_its_text(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally: 
			self.accept_next_alert = True
	
	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	system('del *.png')
	unittest.main()
