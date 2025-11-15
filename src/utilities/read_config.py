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

    @staticmethod
    def get_new_email():
        return config.get('common info', 'new_user_email')

    @staticmethod
    def get_first_name():
        return config.get('common info', 'first_name')

    @staticmethod
    def get_last_name():
        return config.get('common info', 'last_name')

    @staticmethod
    def get_phone_number():
        return config.get('common info', 'phone_number')

    @staticmethod
    def get_location():
        return config.get('common info', 'location')

