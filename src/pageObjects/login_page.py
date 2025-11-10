from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    #Locators :
    link_login_with_verification_code = (By.CSS_SELECTOR,"button.text-brand-blue")
    textbox_email = (By.ID,"email")
    button_send_code = (By.XPATH,"//button[@type='submit']")


    #methods
    def __init__(self, driver):
        self.driver = driver

    def click_login_with_verification_code(self,driver):
        self.wait = WebDriverWait(driver, 10)
        element = self.wait.until(EC.element_to_be_clickable(self.link_login_with_verification_code))
        element.click()



