from __future__ import print_function

import datetime
import os.path
import csv

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file gcal_token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    print("Beginning operation...")
    creds = None
    # The file gcal_token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('gcal_token.json'):
        creds = Credentials.from_authorized_user_file('gcal_token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('gcal_token.json', 'w') as token:
            token.write(creds.to_json())

    print("Acquired credentials")
    try:
        service = build('calendar', 'v3', credentials=creds)
 
        # Establish location to calendar mapping
        googleCalendarForLocation = {}
        with open('locationMapping.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            calendarIDs = []
            for row in csv_reader:
                if row[0] != "location":
                    googleCalendarForLocation[row[0]] = row[1]
                    calendarIDs.append(row[1])
        print(googleCalendarForLocation)

        print("Established service")


        # TODO: loop for each calendar ID
        # Call the Calendar API to acquire the existing list of events once to avoid redundancy
        allExistingEvents = []
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the existing events')
        print("Calendar IDs:", calendarIDs)
        for cid in calendarIDs:
            events_result = service.events().list(calendarId=cid, timeMin=now,
                                              maxResults=1000, singleEvents=True,
                                              orderBy='startTime').execute()
            events = events_result.get('items', [])

            if not events:
                print('No upcoming events found to have conflicts with')

            # # Prints the start and name of the next 10 events
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])
                allExistingEvents.append((start,event['summary']))


        print("All existing events", allExistingEvents)
 
        with open('schedule.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0

            eventList = []
            for row in csv_reader:
                newEvent = {}
                if line_count == 0:
                    properties = row
                    line_count+=1
                else:
                    for pair in zip(properties, row):
                        newEvent[pair[0]] = pair[1]
                    print(newEvent)
                    #     eventList.append(newEvent)
                    # line_count+=1
                    # print("Processing Event:", newEvent)
                    





                    # Refer to the Python quickstart on how to setup the environment:
                    # https://developers.google.com/calendar/quickstart/python
                    # Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
                    # stored credentials.

                    event = {
                        'summary': newEvent["name"],   # 'Misha Nelyubov',
                        'location': newEvent["location"], #'Williamsville Location',
                        # 'description': 'Volunteer 13 and Volunteer 24 are scheduled to come in for this shift',
                        'start': {
                            'dateTime': newEvent["startTime"], #'2022-11-05T09:00:00',
                            'timeZone': 'America/New_York',
                        },
                        'end': {
                            'dateTime': newEvent["endTime"], #'2022-11-05T17:00:00',
                            'timeZone': 'America/New_York',
                        },

                        # 'attendees': [    # Can only create up to 36 invites per day -- https://stackoverflow.com/questions/15473732/google-calendar-api-calendar-usage-limits-exceeded
                        #     {'email': newEvent["email"],}, #'mnelyubo@gmail.com'},
                        # ],

                        # 'reminders': {
                        #     'useDefault': False,
                        #     'overrides': [
                        #     {'method': 'email', 'minutes': 24 * 60},
                        #     {'method': 'popup', 'minutes': 10},
                        #     ],
                        # },
                    }

                    # check the set of existing events in this calendar before publishing a new event to the calendar
                    redundant = False
                    for priorEvent in allExistingEvents:
                        # print("Existing Event:", priorEvent[0])
                        # print("New Event:     ", event['start']['dateTime'])
                        if (event['start']['dateTime'] in priorEvent[0]) and priorEvent[1] == event['summary']:
                            redundant = True

                    if not redundant:
                        print("Attempting to create event", event)
                        event = service.events().insert(calendarId=googleCalendarForLocation[newEvent["location"]], body=event).execute()
                        print("Event created:", (event.get('htmlLink')))
                    else:
                        print("skipping event because it already exists: ", priorEvent)


    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()
    