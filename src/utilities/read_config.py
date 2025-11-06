import configparser

config = configparser.RawConfigParser()
config.read("./config/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        return config.get('common info', 'baseURL')
