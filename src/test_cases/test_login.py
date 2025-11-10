import time

import pytest
from src.pageObjects.login_page import LoginPage
from src.utilities.read_config import ReadConfig
from src.utilities.logger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    #email = ReadConfig.getEmail()
    #password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.smoke
    def test_verify_page_title(self,setup):
        self.logger.info("Test_001_Login.test_verify_page_title")
        self.logger.info("Starting test_verify_page_title")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Aufgang":
            assert True
            self.driver.close()
            print("Actual_Title = ",act_title)
            self.logger.info("test_verify_page_title_PASSED")

        else :
            self.driver.save_screenshot(".\\Screenshots\\" + "test_verify_page_title.png")
            self.logger.info("test_verify_page_title_FAILED")
            assert False


    def test_login(self,setup):
        self.logger.info("Test_001_Login.test_login")
        self.logger.info("Starting test_login")
        self.driver = setup
        self.driver.get(self.baseURL)


