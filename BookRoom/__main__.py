import argparse

from BookRoom.requestlib import login, form_request, request_set_config_file
from BookRoom.datelib import get_unixdate, get_timecode, get_endtime_code
from BookRoom.roomlib import get_room_id, check_room_available
from BookRoom.paramlib import valid_date, valid_time, valid_config_file

resource_id = 'a2d188b3-8349-4f4a-8d2d-549a691864c5'

####################################################################################
#
#
#
####################################################################################

parser = argparse.ArgumentParser(description='This program will book a specified study room at Sheridan college')
parser.add_argument('--room', '-r', help='The room you want to book.', default='C138A', required=False)
parser.add_argument('--date','-d', help='The date is in format YYYY/MM/DD', type=valid_date, required=True)
parser.add_argument('--starttime', '-t', help='start time of room book. valid format is hh:mm[am,pm]', type=valid_time, required=True)
parser.add_argument('--duration', '-period', '-p', help='How long to reserve the room.', choices=[ '30', '60', '90', '120'], required=True)
parser.add_argument('--config', '-c', help='path to load conifiguration file. default is .config.yaml', default='config.yml', type=valid_config_file)
args = parser.parse_args()

room_name = args.room
room_booking_date = args.date
room_booking_start_time = args.starttime
room_booking_duration = args.duration
config_file = args.config

request_set_config_file(config_file)

# Get available rooms
response = form_request(
    url = 'https://roombooking.sheridancollege.ca/Portal/Services/SelfServiceFindRoomList.php'
    ,payload = {
        'cboRequestType': resource_id,
        'startDate': get_unixdate(room_booking_date), # unix datestamp, date of request
        'isSelfService': '1',
        'startTime': get_timecode(room_booking_start_time),
        'duration': room_booking_duration,
        'endTime': get_endtime_code(room_booking_start_time, room_booking_duration),
        'originalRequestID': '00000000-0000-0000-0000-000000000000'
    }
)

check_room_available(response, room_name)

# Make request to book room
form_request(
    url = "https://roombooking.sheridancollege.ca/index.php?p=ConfirmBooking"
    ,payload = {
        'txtOriginalRequestId': '00000000-0000-0000-0000-000000000000',
        'txtRequestTypeId': resource_id,
        'txtRoomId': resource_id,
        'txtRoomConfigId': resource_id,
        'txtStartDate': 'get_unixdate(room_booking_date)',  # unix datestamp, date of request
        'txtDuration': room_booking_duration,
        'AvailableRoomConfigIdentIDs': get_room_id(room_name),
        'dpStartDate3_stamp': get_unixdate(room_booking_date),
        'dpStartDate3': room_booking_date,
        'dpEndByDate_stamp': get_unixdate(room_booking_date),
        'dpEndByDate': room_booking_date,
        'numOccurrences': '10', 'radRecRange': '1', 'txtEndDate': '', 'txtStartTime': '', 'txtEndTime': '',
        'txtCapacity': '0', 'txtMinArea': '0', 'txtLocationId': '', 'RoomTypes': '', 'FloorLevels': '',
        'Pavilions': '', 'Characteristics': '', 'ConfigurationTypes': '', 'everyDay': '1', 'everyWeek': '1',
        'radMonthlyRankType': '1', 'everyMonthDay': '1', 'everyMonth': '1', 'monthlyRank': '0', 'monthlyDayOfWeek': '0',
        'everyMonthRank': '0', 'radYearlyRankType': '1', 'yearlyEveryMonth': '1', 'yearlyMonthDay': '1',
        'yearlyRank': '0', 'yearlyDayOfWeek': '0', 'yearlyMonth': '1',
    }
)

# Confirm Room Booking Request

form_request(
    url = "https://roombooking.sheridancollege.ca/Portal/Services/CreateBookingRequest.php"
    ,payload = {
        'selfService': '1',
        'txtRequestDisclaimer': 'Select OK to submit this request.',
        'txtRoomConfigId': get_room_id(room_name),
        'txtOriginalRequestId': '00000000-0000-0000-0000-000000000000',
        'cboRequestType': resource_id,
        'txtNumberOfAttendees': '',
        'dpStartDate_stamp': get_unixdate(room_booking_date),  # unix datestamp, date of request
        'cboStartTime': get_timecode(room_booking_start_time),
        'cboDuration': room_booking_duration,
        'txtNbOfPeople': '0',
        'txtMinArea': '0',
        'txtRoomId': resource_id,
        'cboRoomConfiguration': get_room_id(room_name),
        'btnConfirm': 'Confirm'
    }
)
