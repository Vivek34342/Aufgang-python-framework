import time

from pageObjects.user_details import UserDetails
from src.pageObjects.login_page import LoginPage
from src.utilities.logger import LogGen
from src.utilities.read_config import ReadConfig


class Test_003_Login_New_User_Profile:
    baseURL = ReadConfig.getApplicationURL()
    verification_code = ReadConfig.get_verification_code()
    new_email = ReadConfig.get_new_email()
    logger = LogGen.loggen()
    new_user_email = ReadConfig.get_new_email()
    first_name = ReadConfig.get_first_name()
    last_name = ReadConfig.get_last_name()
    phone_number = ReadConfig.get_phone_number()
    location = ReadConfig.get_location()

    def test_login_new_user_profile(self,setup):
        self.logger.info("Test_003_Login_New_User_Profile")
        self.logger.info("Starting_Test_login_new_user_profile")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.click_login_with_verification_code()
        self.lp.set_email(self.new_user_email)
        self.lp.click_send_code()
        self.lp.set_verification_code(self.verification_code)
        self.lp.click_login()
        time.sleep(1)
        self.ud = UserDetails(self.driver)
        self.ud.set_first_name(self.first_name)
        self.ud.set_last_name(self.last_name)
        self.ud.set_phone_number(self.phone_number)
        self.ud.set_location(self.location)
        self.ud.click_proceed()
        time.sleep(5)