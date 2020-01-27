import requests
import yaml
import logging

session_cookie = None
config_file = None
logger = logging.getLogger(__name__)

def request_set_config_file(cfg):
    global config_file

    config_file = cfg

# log into room booking
def login():

    global session_cookie


    print(f"print statement {logger.name}")

    logger.info('Login request triggered')

    url = "https://roombooking.sheridancollege.ca/Portal/Services/Login.php"

    payload = {
        'txtUsername': config_file['creds']['username'],
        'txtPassword': config_file['creds']['password']
    }

    response = requests.request("POST", url, data=payload)

    #response.headers['Set-Cookie']
    session_cookie = response.cookies

    return

def form_request(url, payload):

    if session_cookie is None:
        login()

    response = requests.request("POST", url, data=payload, cookies=session_cookie)

    logger.info('info message in request lib')
    logger.debug('HTTP {response.status_code} {response.url}')

    return response
