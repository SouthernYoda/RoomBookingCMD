import json
from bs4 import BeautifulSoup

def get_room_data(response):
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        data = soup.find('div',{'class': 'listDiv'})['data-listdata']

        room_codes = json.loads(data)

        return room_codes

    except:
        print(soup)

def get_room_id(response, room_name):

    room_codes = get_room_data(response)

    for room in room_codes['RowData']:
        if room['rowData'][2] in room_name:
            print('Found Match')
            return room['internalInfo'][2]['a2d188b3-8349-4f4a-8d2d-549a691864c5'][0]

    #room_codes['RowData'][21]['rowData'][2] = 'C142A'
    #room_codes['RowData'][21]['internalInfo'][2]['a2d188b3-8349-4f4a-8d2d-549a691864c5'][0] = {'a2d188b3-8349-4f4a-8d2d-549a691864c5': ['2726467f-c4a2-a10e-e053-4a0f378e0de8']}

def check_room_available(response, room_name):

    room_codes = get_room_data(response)

    for room in room_codes['RowData']:
        if room['rowData'][2] in room_name:
            print('INFO: Room is available')
            return

    print()
    print(f'Room {room_name} is unavailable during the specified time')
    quit()

def select_available_room(response):
    room_codes = get_room_data(response)

    print('These are the rooms available during the timeslot:')
    for room in room_codes['RowData']:
        if room["rowData"][0] in 'TRA':
            print(f' - {room["rowData"][2]}')

    chosen_room = input('Which room would you like to book: ')

    return chosen_room

    print()
    print(f'Room {room_name} is unavailable during the specified time')
