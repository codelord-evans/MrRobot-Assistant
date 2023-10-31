import datetime
import openpyxl
import phonenumbers
import requests

# Load the spreadsheet
wb = openpyxl.load_workbook('schedule.xlsx')
ws = wb.active

# Get the current time
now = datetime.datetime.now()

# Iterate over the rows in the spreadsheet
for row in ws.rows:
    # Get the task name and start time
    task_name = row[0].value
    start_time = datetime.datetime.strptime(row[1].value, '%H:%M')

    # If the start time is now, make a phone call
    if start_time == now:
        # Get your phone number
        phone_number = '+254799040632'

        # Create a Twilio request
        twilio_request = requests.Request(
            method='POST',
            url='https://api.twilio.com/2010-04-01/Accounts/YOUR_ACCOUNT_SID/Calls.json',
            data={
                'Url': 'http://twimlets.com/holdmusic?Digits=1',
                'To': phone_number,
                'From': '+15005550006'
            },
            auth=(AC47d9e058d35d2681dbe397ae12b72fe3, pk9UvfGi1gmaI4lXmtAzpF91AS635kXq)
        )

        # Make the phone call
        response = requests.send(twilio_request)

        # If the phone call was successful, print a message
        if response.status_code == 201:
            print('Phone call made to {} for task: {}'.format(phone_number, task_name))
