from requests_oauthlib import OAuth2Session
import datetime
import pytz



graph_url = 'https://graph.microsoft.com/v1.0'

def get_user(token):
  graph_client = OAuth2Session(token=token)
  # Send GET to /me
  user = graph_client.get('{0}/me'.format(graph_url))
  # Return the JSON result
  return user.json()

def get_calendar_events(token):
  graph_client = OAuth2Session(token=token)
  currentDate = datetime.datetime.now()
  week = datetime.timedelta(weeks = 1)
  nextDate = currentDate + week


  # Configure query parameters to
  # modify the results
  headers = {
    'Prefer' : 'outlook.timezone="Europe/London"'
  }
  query_params = {
    '$top': '50',
    '$select': 'subject,start,end,location,isAllDay',
    'startdatetime': currentDate.isoformat(),
    'enddatetime': nextDate.isoformat(),
    '$orderby': 'start/DateTime ASC',
  }
  # Send GET to /me/events
  events = graph_client.get('{0}/me/calendarview'.format(graph_url), headers = headers,params=query_params)
  print(currentDate.isoformat())
  # Return the JSON result
  return events.json()