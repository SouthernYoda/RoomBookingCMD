import json
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

def get_room_data(response):
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        data = soup.find('div',{'class': 'listDiv'})['data-listdata']

        room_codes = json.loads(data)

        return room_codes

    except:
        logger.error(soup)

def get_room_id(response, room_name):

    room_codes = get_room_data(response)

    for room in room_codes['RowData']:
        if room['rowData'][2] in room_name:
            logger.info('Room entered is valid')
            return room['internalInfo'][2]['a2d188b3-8349-4f4a-8d2d-549a691864c5'][0]

def check_room_available(response, room_name):

    room_codes = get_room_data(response)

    for room in room_codes['RowData']:
        if room['rowData'][2] in room_name:
            print('INFO: Room is available')
            return

    logger.info(f'Room {room_name} is unavailable during the specified time')
    quit()

def select_available_room(response):
    room_codes = get_room_data(response)

    print('\n These are the rooms available during the timeslot:')
    for room in room_codes['RowData']:
        if room["rowData"][0] in 'TRA':
            print(f' - {room["rowData"][2]}')

    chosen_room = input('Which room would you like to book: ')

    return chosen_room
