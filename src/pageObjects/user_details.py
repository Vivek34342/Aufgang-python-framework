from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class UserDetails:
    #locators
    textbox_first_name = (By.XPATH,"//input[@name='user_name']")
    textbox_last_name = (By.XPATH,"//input[@name='user_last_name']")
    text_box_phone_number = (By.XPATH,"//input[@type='tel']")
    text_box_location = (By.XPATH,"//input[@name='user_location']")
    button_proceed = (By.CSS_SELECTOR,"button.bg-brand-blue")

    def __init__(self, driver):
        self.driver = driver

    def set_first_name(self, first_name):
        self.driver.find_element(*self.textbox_first_name).clear()
        self.driver.find_element(*self.textbox_first_name).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(*self.textbox_last_name).clear()
        self.driver.find_element(*self.textbox_last_name).send_keys(last_name)

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.text_box_phone_number).clear()
        self.driver.find_element(*self.text_box_phone_number).send_keys(phone_number)

    def set_location(self, location):
        self.driver.find_element(*self.text_box_location).clear()
        self.driver.find_element(*self.text_box_location).send_keys(location)

    def click_proceed(self):
        self.driver.find_element(*self.button_proceed).click()
