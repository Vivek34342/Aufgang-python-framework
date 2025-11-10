import configparser

config = configparser.RawConfigParser()
config.read("./config/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        return config.get('common info', 'baseURL')

    def getEmail(self):
        return config.get('common info', 'Email')

    def getPassword(self):
        return config.get('common info', 'password')