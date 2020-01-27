import logging

class logger:

    def __init__(self):
        FORMAT = '%(asctime)-15s %(message)s'

        logging.basicConfig(
            level=logging.INFO
            ,format=FORMAT
            ,handlers=[
                logging.StreamHandler()
            ]
        )
