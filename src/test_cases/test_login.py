import time

import pytest
from src.pageObjects.login_page import LoginPage
from src.utilities.read_config import ReadConfig
from src.utilities.logger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.smoke
    def test_login_valid(self,setup):
        self.logger.info("Starting Login Test")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)




