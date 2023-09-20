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

            for event in events:
                service.events().delete(calendarId=cid, eventId=event["id"]).execute()


    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()
    