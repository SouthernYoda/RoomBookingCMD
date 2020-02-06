import datetime as dt
import time
from datetime import datetime, timedelta

time_codes = {
    '7:00am': '420'
    ,'7:30am': '450'
    ,'8:00am': '480'
    ,'8:30am': '510'
    ,'9:00am': '540'
    ,'9:30am': '570'
    ,'10:00am': '600'
    ,'10:30am': '630'
    ,'11:00am': '660'
    ,'11:30am': '690'
    ,'12:00pm': '720'
    ,'12:30pm': '750'
    ,'1:00pm': '780'
    ,'1:30pm': '810'
    ,'2:00pm': '840'
    ,'2:30pm': '870'
    ,'3:00pm': '900'
    ,'3:30pm': '930'
    ,'4:00pm': '960'
    ,'4:30pm': '990'
    ,'5:00pm': '1020'
    ,'5:30pm': '1050'
    ,'6:00pm': '1080'
    ,'6:30pm': '1110'
    ,'7:00pm': '1140'
    ,'7:30pm': '1170'
    ,'8:00pm': '1200'
    ,'8:30pm': '1230'
    ,'9:00pm': '1260'
    ,'9:30pm': '1290'
    ,'10:30pm': '1350'
    ,'10:00pm': '1320'
}

def get_timecodes():
    return time_codes

def get_unixdate(room_booking_date):

    date_obj = dt.date(room_booking_date.year,room_booking_date.month,room_booking_date.day)

    unix_roombooking_date = int(time.mktime(date_obj.timetuple()))

    return unix_roombooking_date

def get_timecode(room_booking_start_time):

    time_code = time_codes[room_booking_start_time]

    return time_code

def get_endtime_code(room_booking_start_time, room_booking_duration):
    format = '%I:%M%p'
    dt_end_time = datetime.strptime(room_booking_start_time, format)

    dt_end_time = dt_end_time + timedelta(minutes=int(room_booking_duration))

    room_booking_end_time = dt_end_time.strftime(format).replace('PM','pm').replace('AM','am').lstrip('0')

    room_booking_end_time_code = get_timecode(room_booking_end_time)

    return room_booking_end_time_code
