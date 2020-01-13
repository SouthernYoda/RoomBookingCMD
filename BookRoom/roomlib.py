import json
from bs4 import BeautifulSoup

def get_room_id(room_name):

    with open('BookRoom//RoomList_codes.json') as json_file:
        room_codes = json.load(json_file)

    for room in room_codes['RowData']:
        if room['rowData'][2] in room_name:
            print('Found Match')
            return room['internalInfo'][2]['a2d188b3-8349-4f4a-8d2d-549a691864c5'][0]

    #room_codes['RowData'][21]['rowData'][2] = 'C142A'
    #room_codes['RowData'][21]['internalInfo'][2]['a2d188b3-8349-4f4a-8d2d-549a691864c5'][0] = {'a2d188b3-8349-4f4a-8d2d-549a691864c5': ['2726467f-c4a2-a10e-e053-4a0f378e0de8']}

def check_room_available(response, room_name):

    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        data = soup.find('div',{'class': 'listDiv'})['data-listdata']

        room_codes = json.loads(data)

        for room in room_codes['RowData']:
            if room['rowData'][2] in room_name:
                print('INFO: Room is available')
                return

    except:
        print(soup)

    print()
    print(f'Room {room_name} is unavailable during the specified time')
    quit()
