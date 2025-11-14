import configparser

config = configparser.RawConfigParser()
config.read("./config/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        return config.get('common info', 'baseURL')

    @staticmethod
    def getEmail():
        return config.get('common info', 'email')

    @staticmethod
    def get_verification_code():
        return config.get('common info', 'verification_code')