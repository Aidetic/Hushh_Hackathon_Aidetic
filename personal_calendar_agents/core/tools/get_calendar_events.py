from core.settings import settings
from core.tools.base import Tool
from googleapiclient.discovery import build
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

class GetCalendarEvents(Tool):

    def __init__(self, user_id=None):

        self.creds = service_account.Credentials.from_service_account_file(
                settings.credentials_json,
                scopes= [settings.credentials_path] if settings.credentials_path else ['https://www.googleapis.com/auth/calendar']
            )
        
        self.service = build("calendar", "v3", credentials= self.creds)

        self.user_id = user_id

        self.now = datetime.datetime.now().isoformat() + 'Z'

            
    def _format_events(self, raw_events):
        """
        Internal method to format raw events into clean, structured data.
        
        Args:
            raw_events (List[Dict]): Raw event data from API
            
        Returns:
            List[Dict]: Formatted event dictionaries
        """
        formatted_events = []
        
        for event in raw_events:
            formatted_event = {
                'id': event.get('id', ''),
                'title': event.get('summary', 'No Title'),
                'time': self.now,
                'description': event.get('description', ''),
                'location': event.get('location', ''),
                'attendees': [
                    {
                        'email': attendee.get('email', ''),
                        'name': attendee.get('displayName', ''),
                        'status': attendee.get('responseStatus', '')
                    }
                    for attendee in event.get('attendees', [])
                ],
                'creator': {
                    'email': event.get('creator', {}).get('email', ''),
                    'name': event.get('creator', {}).get('displayName', '')
                },
                'organizer': {
                    'email': event.get('organizer', {}).get('email', ''),
                    'name': event.get('organizer', {}).get('displayName', '')
                },
                'status': event.get('status', ''),
                'html_link': event.get('htmlLink', ''),
                'meeting_link': event.get('hangoutLink', ''),
                'raw_start': event['start'],
                'raw_end': event['end']
            }
            formatted_events.append(formatted_event)
        
        return formatted_events

    def __call__(self, user_id = 'pandeygag78934@gmail.com'):

        """
        Fetches the next 5 upcoming calendar events for a given user.

        Args: None

        Returns:
            list: A list of event dictionaries representing the next 5 upcoming events, 
                  each containing details like summary, start time, etc.
        """
        now = datetime.datetime.now().isoformat() + 'Z'
        events_result = self.service.events().list(calendarId= user_id, timeMin= now,
                                            maxResults= 5, singleEvents=True,
                                            orderBy='startTime').execute()
        
        events = events_result.get('items', [])
        

        formatted_events = self._format_events(events)

        return formatted_events
        
    def __repr__(self):
        return self.__call__.__doc__

get_calendar_events = GetCalendarEvents()
print(get_calendar_events())