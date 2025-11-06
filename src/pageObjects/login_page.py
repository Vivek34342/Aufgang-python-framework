from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    #Locators :
    link_login_with_verification_code = (By.CSS_SELECTOR,"button.text-brand-blue")
    textbox_email = (By.ID,"email")
    button_send_code = (By.XPATH,"//button[@type='submit']")
