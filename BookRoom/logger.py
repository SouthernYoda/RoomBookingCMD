import logging

class logger:

    def __init__(self, logLevel):
        FORMAT = '%(asctime)-15s %(levelname)s %(message)s'

        print(f"log level = {logLevel}")

        logging.basicConfig(
            level=logLevel
            ,format=FORMAT
            ,handlers=[
                logging.StreamHandler()
            ]
        )
