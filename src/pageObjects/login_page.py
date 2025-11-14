from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # Locators :
    link_login_with_verification_code = (By.CSS_SELECTOR, "button.text-brand-blue")
    textbox_email = (By.XPATH, "//input[@type='email']")
    button_send_code = (By.XPATH, "//button[@type='submit']")
    textbox_verification_code = (By.XPATH,"//input[@inputmode='numeric'][1]")
    button_login = (By.CSS_SELECTOR,"button.bg-brand-blue")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_login_with_verification_code(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.link_login_with_verification_code)
        )
        element.click()

    def set_email(self,email):
        self.driver.find_element(*self.textbox_email).clear()
        self.driver.find_element(*self.textbox_email).send_keys(email)

    def click_send_code(self):
        self.driver.find_element(*self.button_send_code).click()

    def set_verification_code(self,verification_code):
        self.driver.find_element(*self.textbox_verification_code).clear()
        self.driver.find_element(*self.textbox_verification_code).send_keys(verification_code)

    def click_login(self):
        self.driver.find_element(*self.button_login).click()

