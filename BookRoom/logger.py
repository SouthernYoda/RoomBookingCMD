import logging

class logger:

    def __init__(self):
        FORMAT = '%(asctime)-15s %(levelname)s %(message)s'

        logging.basicConfig(
            level=logging.DEBUG
            ,format=FORMAT
            ,handlers=[
                logging.StreamHandler()
            ]
        )
