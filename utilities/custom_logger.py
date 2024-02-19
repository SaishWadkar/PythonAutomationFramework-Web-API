import logging

class LogGen:

    @staticmethod
    def restful_booker_api_logs():
        formatter=logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")
        handler=logging.FileHandler(filename='.\\logs\\restful_booker\\restful_booker_api_automation.log')
        handler.setFormatter(formatter)

        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        return logger

    @staticmethod
    def orange_hrm_logs():
        formatter=logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")
        handler=logging.FileHandler(filename='.\\logs\\orange_hrm\\orange_hrm_automation.log')
        handler.setFormatter(formatter)

        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        return logger