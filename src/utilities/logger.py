import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        if not logger.hasHandlers():
            fileHandler = logging.FileHandler("./logs/automation.log", mode='a')
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%d-%b-%y %H:%M:%S')
            fileHandler.setFormatter(formatter)
            logger.addHandler(fileHandler)
            logger.setLevel(logging.INFO)
        return logger
