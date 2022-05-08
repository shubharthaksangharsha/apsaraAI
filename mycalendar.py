from datetime import timedelta
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file('./google2.json', scopes=scopes)
credentials = flow.run_console()
pickle.dump(credentials, open("token.pkl", "wb")) #Save credentials
credentials = pickle.load(open("token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)
print(service)
list_calendars = service.calendarList().list().execute()
#primary=list_calendars['items'][0]['id']
#list_events = service.events().list(calendarId=primary).execute()
#print(list_events['items'][0])
