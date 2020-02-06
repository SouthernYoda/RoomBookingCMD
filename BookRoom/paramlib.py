import argparse
from datetime import datetime
import dateparser
import yaml

from BookRoom.datelib import get_timecodes

def valid_date(arg_date):
    try:
        #datetime.strptime(arg_date, '%Y/%m/%d')
        room_date = dateparser.parse(arg_date)

        print(f"The room date is : {room_date}")

        return room_date

    except ValueError:
        msg = "Not a valid date format"
        raise argparse.ArgumentTypeError(msg)

def valid_time(arg_time):
    time_codes = get_timecodes()

    if arg_time in time_codes:
        return arg_time
    else:
        raise argparse.ArgumentTypeError('Invalid time, ensure the time is bettween 7:00am and 10:00pm and it is on the hour or half hour')

def valid_config_file(arg_file):
    try:
        with open(arg_file, 'r') as yamlfile:
            cfg = yaml.load(yamlfile)

        #tests
        test = cfg['creds']['username'] # retrieve username
        test = cfg['creds']['password']

        return cfg

    except:
        msg = "Configuration is not found or invalid"
        raise argparse.ArgumentTypeError(msg)
