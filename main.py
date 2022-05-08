#!/home/shubharthak/miniconda3/bin/python
'''
Apsara AI: Designed by Shubharthak Sangharasha

What it can do:-
1: Wishing 
2.Tell Time
3.Tell Date
4.Open Youtube 
5.Open College Site 
6:Check the Weather 
7:Read the time table
8 Tell Jokes
9.Read the News
10:Search Wikipedia 
11:Play-Pause any music From Spotify on any connected device
12.Play song on youtube too
13.Show me attendance 
14.Show me result 
15.Set Alarm/Timer
16:Search in web
17:Send Mail
18:Read Unseen/Inbox Emails
19.Ring the Phone
20:Bye Mesage
More to come...
'''
from gtts import gTTS
import speech_recognition as sr
import psutil as ps
import os
import schedule
import datefinder
from newsapi.newsapi_client import NewsApiClient
import vlc
import pytz
import datetime
import wikipedia
import webbrowser
import pyautogui
import time
import random
from email.message import EmailMessage
import smtplib
from word2number import w2n
import pyjokes
import requests
import bs4
import google
import pandas as pd
import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth
import pywhatkit
from pepper import *
import imaplib
import email
from email.header import decode_header
from datetime import date
from apiclient.discovery import build
from datetime import timedelta
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
today = date.today()
whatsapp = {'deepu': 'Shizuka', 'mummy':'Mummy', 'bro':'Bhaiya', 'papa': 'Dr Sher Singh'}
emails = {'myself': 'shubharthaksangharsha@gmail.com', 'mummy': 'usharani20jan@gmail.com', 'bro': 'siddhant3s@gmail.com', 'bhabhi':'ahuja.chaks@gmail.com' }
api_url= os.getenv("API_KEY")
base_url= os.getenv("BASE_URL")
api_news = os.environ.get('news')
base_news_url = 'https://newsapi.org/v2/top-headlines?'

#credentials = flow.run_console()
#pickle.dump(credentials, open("token.pkl", "wb")) #Save credentials
def write_file(text):
    with open('command.txt', 'w') as f:
        f.write(text)
    return True
def speak(text):    
    write_file(text)
    speech = gTTS(text=text, lang="en", slow=False)
    speech.save("text.mp3")
    os.system("mpg123 text.mp3")
    print(f'Apsara said: {text}')
    
#take command from the user
def takeCommand():
    '''
    It takes microphone input from the user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        try:
            audio = r.listen(source,timeout=1,phrase_time_limit=2)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
    return query
#for news
def takeCommand2():
    '''
    It takes microphone input from the user and returns output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('inside news')
        print("Listening...")
        r.pause_threshold = 0.6
        try:
            audio = r.listen(source,phrase_time_limit=2, timeout = 6)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please")
            return "exception"
    return query
    
def takeCommand3():
    '''
    It takes microphone input from the user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('inside news')
        print("Listening...")
        r.pause_threshold = 0.6
        try:
            audio = r.listen(source,phrase_time_limit=6, timeout = 6)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please")
            return "exception"
    return query
def takeCommand4():
    '''
    It takes microphone input from the user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('inside news')
        print("Listening...")
        r.pause_threshold = 0.6
        try:
            audio = r.listen(source,phrase_time_limit = 10,timeout = 10)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please")
            return "exception"
    return query

def authenticate_google():
    scopes = ['https://www.googleapis.com/auth/calendar']
    flow = InstalledAppFlow.from_client_secrets_file('google.json', scopes=scopes)
    credentials = pickle.load(open("token.pkl", "rb"))
    service = build("calendar", "v3", credentials=credentials)
    return service

def open_netflix():
    try:
        with pyautogui.hold('win'):
            pyautogui.press('r')
        pyautogui.write('netflix')
        pyautogui.press('return')
        time.sleep(10)
        pyautogui.click(x=60,y=122)
        pyautogui.press(['tab','tab','return'])
    except Exception as e:
        print(e)
        
def open_cloud():
    try:
        with pyautogui.hold('win'):
            pyautogui.press('r')
        pyautogui.write('alacritty')
        pyautogui.press('return')
        time.sleep(2)
        pyautogui.write('cloud')
        time.sleep(2)
        pyautogui.press('return')
        time.sleep(4)
        with pyautogui.hold('win'):
            pyautogui.press('r')
        pyautogui.write('vncviewer')
        pyautogui.press('return')
        time.sleep(1)
        with pyautogui.hold('ctrl'):
            pyautogui.press('a')
            pyautogui.press('backspace')
        pyautogui.write('localhost:5902')
        pyautogui.press('return')
        time.sleep(2)
        pyautogui.write('shubhi21')
        time.sleep(2)
        pyautogui.press('return')
    except Exception as e:
        print(e)
def get_events(day, service):
#    now = datetime.datetime.now()
#    now = now.strftime("%Y-%m-%d") + "T12:00:00-07:00"
#    print(f'Getting the upcoming {n} events')
    date = datetime.datetime.combine(day, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
    ist = pytz.timezone("Asia/Kolkata")
    date = date.astimezone(ist)
    end_date = end_date.astimezone(ist)
    event_result = service.events().list(calendarId = 'primary', timeMin=date.isoformat(),timeMax = end_date.isoformat(),singleEvents = True, orderBy='startTime').execute()# maxResults = n, 
    events = event_result.get('items', [])
    if not events:
        print('No upcoming events found')
        speak('No upcoming meetings found')
    else:
        speak(f'You have {len(events)} events on this day.')        
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
            start_time = str(start.split("T")[1].split("-")[0])
            if int(start_time.split(":")[0]) < 12:
                start_time = start_time.split(":")[0] + "am"
            else:
                start_time = str(int(start_time.split(":")[0])- 12 + "pm")
            speak(event['summary'] + 'at' + start_time)           
def get_date(text):
    MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    DAY_EXTENTIONS= ["nd", "rd", "th", "st"]
    text = text.lower()
    today = datetime.date.today()

    if text.count("today") > 0:
        return today
    if text.count("tomorrow") > 0:
        return today + timedelta(1)
    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

    # THE NEW PART STARTS HERE
    if month < today.month and month != -1:  # if the month mentioned is before the current month set the year to the next
        year = year+1

    # This is slighlty different from the video but the correct version
    if month == -1 and day != -1:  # if we didn't find a month, but we have a day
        if day < today.day:
            month = today.month + 1
        else:
            month = today.month

    # if we only found a dta of the week
    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week

        if dif < 0:
            dif += 7
            if text.count("next") >= 1:
                dif += 7

        return today + datetime.timedelta(dif)

    if day != -1:  
        return datetime.date(month=month, day=day, year=year)
    
def create_event(day, service, mail, summary):
    try:
        speak('Tell me the time')
        meeting_time = takeCommand2().lower()
        if 'a' in meeting_time:
            meeting_time =  int(meeting_time.split('a')[0].split(':')[0])
        elif 'p' in meeting_time:
            meeting_time =  int(meeting_time.split('p')[0].split(':')[0]) + 12
        start_time = datetime.datetime.combine(day, datetime.time(meeting_time))    
        end_time = start_time + timedelta(minutes=59)
        timezone = 'Asia/Kolkata'
        event = {
            'summary': summary,
            'location': 'Delhi',
            'description': summary,
            'start': {
                'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': timezone,
            },
            'end': {
                'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': timezone,
            },
            'attendees': [
                {'email': mail }                    
            ],
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
        event = service.events().insert(calendarId=emails['myself'],sendUpdates='all', body=event).execute()
        print ('Event created: %s' % (event.get('htmlLink')))
        speak('Event has been created')
    except Exception as e:
        print(e)
        speak('Unable to create the event')       

def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)
#reading email
def read_unseen():
    flag = 0
    host = 'imap.gmail.com'
    username = os.environ.get('mymail')
    password = os.environ.get('mypass')
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(username, password)
    #status, messages = imap.select("INBOX")
    imap.select('INBOX')
    _, messages = imap.search(None, 'UNSEEN')
    speak('reading 2 emails')
    # number of top emails to fetch
    N = 3
    mail_ids = []
    # total number of emails
    for block in messages:
        mail_ids += block.split()
        start_messages = int(mail_ids[0])
        end_messages = int(mail_ids[-1])
    for index, i in enumerate(range(end_messages, start_messages, -1)):
        # fetch the email message by ID
        if index == 2:
            break
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                # if it's a bytes, decode to str
                    subject = subject.decode(encoding)
                # decode email sender
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    From = From.decode(encoding)
                print("Subject:", subject)
                print("From:", From)
                speak(str(index+1) + 'mail from : ' + From)
                speak('subject is ' + subject)
                speak('Do you want me to continue reading')
                answer = takeCommand3().lower()
                if 'nope' in answer or 'no' in answer:
                    speak('Okay')
                    flag = 1
                    break                    
                # if the email message is multipart
                if msg.is_multipart():
                    # iterate over email parts
                    for part in msg.walk():
                        # extract content type of email
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            # get the email body
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            pass
                        elif "attachment" in content_disposition:
                            # download attachment
                            print('Contains attachment')
                            filename = part.get_filename()
                            if filename:
                                folder_name = clean(subject)
                                if not os.path.isdir(folder_name):
                                    # make a folder for this email (named after the subject)
                                    os.mkdir(folder_name)
                                filepath = os.path.join(folder_name, filename)
                                # download attachment and save it
                                open(filepath, "wb").write(part.get_payload(decode=True))
                else:
                    # extract content type of email
                    content_type = msg.get_content_type()
                    # get the email body
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        # print only text email parts
                        print(body)
                        speak(body)
                    if content_type == "text/html":
                        # if it's HTML, create a new HTML file and open it in browser
                        folder_name = clean(subject)
                        if not os.path.isdir(folder_name):
                        # make a folder for this email (named after the subject)
                            os.mkdir(folder_name)
                        filename = "index.html"
                        filepath = os.path.join(folder_name, filename)
                        # write the file
                        open(filepath, "w").write(body)
                        # open in the default browser
                        webbrowser.open(filepath)
                        time.sleep(2)
                        os.system(f'rm -rf {filepath}')
                        os.system(f'rmdir {folder_name}')
                    print("="*100)
        if flag == 1:
            break
                
    # close the connection and logout
    imap.close()
    imap.logout()



#spotify play
def spotify():
    """
    To run this script, you must have a file in this directory called 'setup.txt'
    In this file, enter all of the values of the required variables in the following format:

    client_id=XXXXXXXX
    client_secret=XXXXXXX
    device_name=Jake's iMac
    redirect_uri=https://example.com/callback/
    username=jakeg135
    scope=user-read-private user-read-playback-state user-modify-playback-state

    """
    # variables from setup.txt
    setup = pd.read_csv('./setup.txt', sep='=', index_col=0, squeeze=True, header=None)
    client_id = setup['client_id']
    client_secret = setup['client_secret']
    device_name = setup['device_name']
    device_name3 = 'Web Player (Firefox)'
    device_name2 = 'OPPO F17 Pro'
    redirect_uri = setup['redirect_uri']
    scope = setup['scope']
    username = setup['username']
    # Connecting to the Spotify account
    auth_manager = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope,
        username=username)
    print(f'Auth manager = {auth_manager}')
    spotify = sp.Spotify(auth_manager=auth_manager)
    try:
        # Selecting device to play from
        devices = spotify.devices()
        print(devices)
        deviceID = {}
        
        for d in devices['devices']:
            d['name'] = d['name'].replace('’', '\'')
            if d['name'] == device_name:
                deviceID[d['name']] = d['id']
                continue
            if d['name'] == device_name2:
                deviceID[d['name']] = d['id']
                continue
            if d['name'] == device_name3:
                deviceID[d['name']] = d['id']
                continue
    except:
        speak('Cant do it')
    return spotify,deviceID


#greeting function
def wishMe():
    '''
    It wishes the User according the time and return the file which played using os.system()
    '''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! ")
    else:
        speak("Good Evening!")


#for searching from google
def search_me(message):
    url = "https://google.com/search?q=" + message
    # Sending HTTP request
    request_result = requests.get( url )
    # Pulling HTTP data from internet
    soup = bs4.BeautifulSoup( request_result.text, "html.parser" )
    answer = soup.find( "div" , class_='BNeawe' ).text	
    return answer

#for setting alarm 
def set_alarm(seconds):
    i=100
    count = 0
    print(f'Set for {seconds} seconds')
    time.sleep(seconds)
    while True:
        i+=100
        os.system("mpg123 /home/shubharthak/Desktop/alarm.mp3")
        os.system('pactl set-sink-volume 0 '+str(i)+'%')
        count+=1
        if count == 5:
            break
    os.system('pactl set-sink-volume 0 100%')
#getting weather reports
def get_weather(API_URL=f'{api_url}', BASE_URL=f'{base_url}', city='delhi'):
    request_url = f"{BASE_URL}?appid={API_URL}&q={city}"
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = round(data['main']['temp'] - 273.15, 2)
        print(temperature)
        print(weather)
        result = (f'{weather}',
                  f'and Temperature is {temperature} celsius')
        return result
    else:
        return None
#getting news reports
def get_news(API_URL=f'{api_news}', BASE_URL=f'{base_news_url}'):
    request_url = f"{BASE_URL}country=in&apiKey={API_URL}"
    response = requests.get(request_url)
    data = response.json()
    if response.status_code == 200:
        for new in data['articles']:
            print(str(new['title']), "\n\n")
            title = str(new['title'])
            speak(title)
            speak('you want me to keep reading for you ?')
            try:
                answer = takeCommand2().lower()
                print(answer)
            except:
                speak('Sorry I am unable to read more')
            if 'yes' in answer or 'okay' in answer or 'alright' in answer:
                speak('Okay Reading')
                print(str(new['description']), "\n\n")
                description = str(new['description'])
                speak(description)
            elif 'no' in answer:
                speak('Okay!')
                break
            else:
                speak('You did not said yes so I am not reading')
                break
    else:
        speak('Unable to get news')
        return None
 
#sending mail 
def sendEmail(to, content):
    username = os.environ.get('mymail')
    password = os.environ.get('mypass')
    msg = EmailMessage()
    msg['Subject'] = 'Mail From Apsara AI'
    msg['From'] = username
    #msg['To'] = username
    msg['To'] = to
    msg.set_content(content)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(username, password)
        smtp.send_message(msg)

def read():
    with open('command.txt', 'r') as f:
        query = f.read()
    with open('command.txt', 'w') as f:
        pass
    return query

def open_daily_schedule():
    speak('opening daily schedule')
    webbrowser.open('leetcode.com')
    webbrowser.open_new_tab('https://github.com/shubharthaksangharsha/shubhi-prep')
    webbrowser.open_new_tab('youtube.com')
    speak('Getting Weather Reports')
    try:
        weather, temperature = get_weather()
        speak(f'Weather of delhi is ' + weather + temperature)
    except:
        speak('Sorry Unable to get weather reports at this moment')
    try:
        speak('Reading News')
        get_news()
    except:
        speak('Sorry Unable to read news at this moment')
def wake_up_shubh():
    speak('Sir wake up, its morning')
    i=100
    count = 0
    while True:
        i+=100
        os.system("mpg123 /home/shubharthak/Desktop/alarm.mp3")
        os.system('pactl set-sink-volume 0 '+str(i)+'%')
        count+=1
        if count == 5:
            break
    os.system('pactl set-sink-volume 0 150%')
def run(query):
    spotify2, deviceID = spotify()    
    schedule.every().day.at('08:00').do(wake_up_shubh)
    MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    DAY_EXTENSIONS = ["nd", "rd", "th", "st"]
    device_name2 = 'CPH2119'
    device_name = 'shubharthak'
    device_name3 = 'Web Player (Firefox)'
    say = ['Haan ji boliye?', 'ji boliye?', 'Yes sir?', 'ji boliye sir?']
    greet = ['I am Apsara designed by Shubharthak Sir. Please tell me how may I help you','Mera naam Apsara hai. Mujhe Shubharthak Sir nei design kiya hai, Please Bataayein Maii Aapki kya Sevaa Karoon?']
    try:               
        if (not ps.sensors_battery().power_plugged and int(ps.sensors_battery().percent) < 50):
            speak('Sir Please charge me')
        #query = takeCommand()
        #if query == 'None' or query =='exception':
        #    query = read()
        schedule.run_pending()
        # logic for executing tasks based on query
        query = query.replace('apsara','').replace('Apsara','').replace('Akshara','').replace('akshara','').replace('ab Sar', '')
        query = query.lower()
        if 'battery' in query:
            if (ps.sensors_battery().power_plugged == True):
                speak(f'{int(ps.sensors_battery().percent)} percent and Laptop is Charging')
            else:
                    speak(f'{int(ps.sensors_battery().percent)} percent and Laptop is not Charging')
        if 'on youtube' in query or 'On Youtube' in query or 'on Youtube' in query or 'On youtube' in query:
                query = query.replace('play', '').replace('open','').replace('on youtube', '').replace('On youtube', '').replace('on Youtube', '').replace('On Youtube', '')
                pywhatkit.playonyt(query)
                speak(f'Playing {query}')
                time.sleep(3)
                pyautogui.press('space')
            #open leetcode:
        if 'leetcode' in query:
                webbrowser.open('www.leetcode.com')
                speak('Opened leetcode Sir')
                #set spotify again
        if 'set spotify' in query or 'Set Spotify' in query or 'sad spotify' in query or 'sed spotify' in query:
                devices = spotify2.devices()
                print(devices)
                for d in devices['devices']:
                    d['name'] = d['name'].replace('’', '\'')
                    if d['name'] == device_name:                                      
                        deviceID[d['name']] = d['id']
                        continue
                    if d['name'] == device_name2:
                        deviceID[d['name']] = d['id']
                        continue
                    if d['name'] == device_name3:
                        deviceID[d['name']] = d['id']
                        continue
                print(f'DeviceID: {deviceID}')
                speak('Set Spotify')
            #open spotify
        if 'open spotify web' in query:
            webbrowser.open('https://open.spotify.com/')
            time.sleep(5)
            print(devices)
            for d in devices['devices']:
                d['name'] = d['name'].replace('’', '\'')
                if d['name'] == device_name:                                      
                    deviceID[d['name']] = d['id']
                    continue
                if d['name'] == device_name2:
                    deviceID[d['name']] = d['id']
                    continue
                if d['name'] == device_name3:
                    deviceID[d['name']] = d['id']
                    continue
            print(f'DeviceID: {deviceID}')         
                
            
        if 'open spotify' in query or 'Open Spotify' in query or 'open Spotify' in query:
                os.system('spotify &' )
                speak('opening spotify')
                time.sleep(10)
                devices = spotify2.devices()
                time.sleep(2)
                speak('opened spotify')
                print(devices)
                for d in devices['devices']:
                    d['name'] = d['name'].replace('’', '\'')
                    if d['name'] == device_name:                                      
                        deviceID[d['name']] = d['id']
                        continue
                    if d['name'] == device_name2:
                        deviceID[d['name']] = d['id']
                        continue
                    if d['name'] == device_name3:
                        deviceID[d['name']] = d['id']
                        continue
                print(f'DeviceID: {deviceID}')
                #device1:Spotifydesktop app
        if 'on device one' in query or 'on device 1' in query or 'ondevice one' in query or 'ondevice 1' in query:
                    query = query.replace('on device one', '').replace('play', '').replace('Play', '').replace('1', '').replace('on device', '')
                    print(f'query is : {query}')
                    uri = get_track_uri(spotify=spotify2, name=query)
                    print(f'Track: {uri}')
                    play_track(spotify=spotify2, device_id=deviceID[device_name], uri=uri)
                
                #device2:SpotifyMobileapp
        if 'on device to' in query or 'on device 2' in query or 'ondevice to' in query or 'ondevice 2' in query or 'device two' in query:
                query = query.replace('play', '').replace('on device two','').replace('on device 2', '').replace('on device too','').replace('on device tu','').replace('on device to','').replace('Play', '')
                print(f'query is : {query}')
                try:
                    uri = get_track_uri(spotify=spotify2, name=query)
                    print(f'Track: {uri}')
                    play_track(spotify=spotify2, uri=uri)                 
                except Exception as e:
                    print(e)
                    speak('Unable to play on device 2')
            #device3:SpotifyFirefox
        if 'on device three' in query or 'on device 3' in query or 'on device tree' in query or 'on device tee' in query:
                query = query.replace('play', '').replace('on device three','').replace('on device 3', '').replace('Play', '')
                print(f'query is : {query}')
                try:
                    uri = get_track_uri(spotify=spotify2, name=query)
                    print(f'Track: {uri}')
                    play_track(spotify=spotify2, device_id=deviceID[device_name3], uri=uri)                 
                except:
                    speak('Unable to play on device 3')
                                            
                #Search for wikipedia          
        if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                try:
                    query = query.replace('wikipedia', '')
                    result = wikipedia.summary(query, sentences=1)
                    print(result)
                    speak("According to wikipedia")
                    speak(result)
                except:
                    speak('Sorry Unable  to stop')                
        elif "open youtube" in query:
                webbrowser.open("youtube.com")
                speak('Opened Youtube')
        elif "open college site" in query:
                os.system("python college.py")
                speak('Opened College Site')
        elif "my music" in query or 'mi music' in query :
                music_dir = "/home/shubharthak/Desktop/shubhi/shubhi_songs/"
                songs = os.listdir(music_dir)
                media = vlc.MediaPlayer(os.path.join(
                music_dir, songs[random.randint(0, len(songs)-1)]))
                media.play()
                os.system("python /home/shubharthak/Desktop/shubhi_handmodule/hand_detector_shubh/volumehandcontrol/try.py &")                
                #stop the music
        elif 'stop' in query:
                try:
                    with pyautogui.hold('ctrl'):
                        pyautogui.press('w')                   
                    if device_name in deviceID:
                        spotify2.pause_playback(device_id=deviceID[device_name])
                    if device_name3 in deviceID:
                        spotify2.pause_playback(device_id=deviceID[device_name3])

                    media.stop()
                    spotify2.pause_playback(device_id='98b2d7ffaca52ec038471f30532f2fc35ed76332')
                except Exception as e:
                    print(e)

        elif  'pause' in query or 'pose' in query or 'start' in query:
                try:
                    pyautogui.press('space')                    
                    if device_name in deviceID:
                        spotify2.pause_playback(device_id=deviceID[device_name])
                    if device_name3 in deviceID:
                        spotify2.pause_playback(device_id=deviceID[device_name3])

                    media.stop()
                    spotify2.pause_playback(device_id='98b2d7ffaca52ec038471f30532f2fc35ed76332')
                except Exception as e:
                    print(e)
                    
        elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"Sir, the time is {strTime}")
                #Play Friends episode
        elif 'play friends' in query or 'play friend' in query:
                speak("Which episode sir.")
                ask = takeCommand2().lower()
                friends_dir = "/home/shubharthak/friends/season9/"
                episodes = os.listdir(friends_dir)
                try:
                    print(episodes)
                    i = str(w2n.word_to_num(ask))
                    os.system("ffplay /home/shubharthak/friends/season9/"+i+".mkv")
                except:
                    speak("Cant Understand")
                    print("Cant Understand")
                        
        elif 'attendance' in query or 'attandance' in query:
                speak('Getting Attendance Sir')
                try:
                    y = datetime.datetime.now().year
                    m=datetime.datetime.now().month
                    d=datetime.datetime.now().day
                    os.system("rm /home/shubharthak/AttendanceSummary-"+str(m)+"_"+str(d)+"_"+str(y)+".pdf")
                    os.system(
                        "python /home/shubharthak/Desktop/get_attendance.py && xdg-open /home/shubharthak/AttendanceSummary-"+str(m)+"_"+str(d)+"_"+str(y)+".pdf")
                    time.sleep(4)
                    os.system("rm /home/shubharthak/AttendanceSummary-"+str(m)+"_"+str(d)+"_"+str(y)+".pdf")    
                except:
                    speak('Unable to get Attendance Sir')
        elif 'copy' in query:
            query = query.replace('copy', '')
            print(f'saying: {query}')
            speak(query)
        elif 'bye' in query or 'buy' in query or 'bhai' in query or 'Bai' in query:
                print(query)
                speak(f'Good Bye Shubharthak Sir, Take care')                
        elif 'joke' in query or 'jokes' in query:
                My_joke = pyjokes.get_joke(language="en", category="all")
                speak(My_joke)
        elif 'Hi Apsara' in query or 'hello apsara' in query or 'hey apasara' in query or 'what is your name' in query or 'your name' in query:
                speak(greet[random.randint(0, len(greet)-1)])
                    
                    #send mail to anyone
        elif "send mail" in query or 'sendmail' in query:
                try:
                    speak('To Who I should send this mail')
                    answer = takeCommand2().lower()
                    if answer == 'None' or answer =='exception':
                        answer = read()
                    if 'mummy' in answer:
                        speak("What should I say")
                        content = takeCommand2().lower()
                        to = emails['mummy']
                        speak('Confirm me yes or no')
                        answer = takeCommand2().lower()
                    if answer == 'None' or answer =='exception':
                        answer = read()
                        if 'yes' in answer:
                            sendEmail(to, content)
                            speak('Email has been sent!')
                        elif 'no' in answer:
                            speak('Okay')
                        else:
                            speak('No response going back')
                    elif 'bro' in answer:
                            speak("What should I say")
                            content = takeCommand2()
                            to = emails['bro']
                            speak('Confirm me yes or no')
                            answer = takeCommand2().lower()
                            if 'yes' in answer:
                                sendEmail(to, content)
                                speak('Email has been sent!')
                            elif 'no' in answer:
                                speak('Okay')
                            else:
                                speak('No response going back')
                    elif 'myself' in answer:
                            speak("What should I say")
                            content = takeCommand2()
                            to = emails['myself']
                            speak('Confirm me yes or no')
                            answer = takeCommand2().lower()
                            if 'yes' in answer:
                                sendEmail(to, content)
                                speak('Email has been sent!')
                            elif 'no' in answer:
                                speak('Okay')
                            else:
                                speak('No response going back')
                except:
                        speak('Sorry my friend. I am not able to send this email at this moment')            

        elif 'weather in my state' in query:
                try:
                    speak('Getting Weather Reports')
                    weather, temperature = get_weather()
                    speak(f'Weather of delhi is ' + weather + temperature)
                except:
                    speak(
                        'Sorry my friend. I am not able to get weather reports at this moment')
        elif 'what is the weather' in query:
                try:
                    speak('Please tell me weather of which state')
                    city = takeCommand()
                    speak('Getting Weather Reports')
                    weather, temperature = get_weather(city=city)
                    speak(f'Weather of {city} is ' + weather + temperature)
                except:
                        speak(
                            'Sorry my friend. I am not able to get weather reports at this moment')
                        #search from google
        elif 'search' in query:
                    try:
                        query = query.replace('search', '')
                        result = search_me(query)
                        speak(result)
                    except:
                        speak('Sorry my friend. I am not able to search your query')
        elif "my result" in query:
                    try:
                        speak('Opening result from Chandigarh University Site')
                        os.system(
                            "python /home/shubharthak/Desktop/myresult/main.py && xdg-open /home/shubharthak/Desktop/apsaraAI/result.png")
                    except:
                        speak('Unable to get your Result Sir')
        elif 'news' in query or 'News' in query or 'neus' in query:
                    speak('Getting today news')
                    get_news(API_URL=f'{api_news}', BASE_URL=f'{base_news_url}')

        elif 'read email' in query  or 'read mail' in query:
                    speak('Connecting to mail server')
                    read_unseen()
                    
        elif 'date' in query:
                    date = today.strftime("%d %B, %Y")
                    speak(date)
                    
        elif 'day today' in query:
                    day = datetime.datetime.today().strftime('%A')
                    speak(day)
        elif 'ring' in query:
                    speak('Ringing the phone in one minute')
                    os.system('python find.py &')
                    speak('Your Phone must be ringing')
        elif 'class' in query:
                    speak("You're classes will start from 8 feburary. Your first lecture will be of Design and Analysis of Algorithms at 9:40 AM")
        elif 'open scheduler' in query:
                    open_daily_schedule()

        elif 'minutes' in query or 'minute' in query:
                    query = query.replace('minutes' , '').replace('minute', '').replace('for', '').replace('alarm', '').replace('set', '').replace('Set', '').replace('Alarm', '').replace('Minutes', '').replace('Minute', '')
                    print(query)
                    speak(f'Setting alarm for {query} minutes')
                    try:
                        i = int(query) * 60                
                        set_alarm(i)
                    except:
                        speak("Can't set alarm right now")
                    
        elif 'alarm' in query or 'timer' in query:
                    speak('Okay for how many seconds')
                    answer = takeCommand2().lower()
                    try:
                        i = int(w2n.word_to_num(answer))
                        set_alarm(i)
                    except:
                        speak('cant set alarm please try again ')
        elif "love" in query:
                    speak('I love you tooo shubharthak sir')
        elif 'check' in query or 'Check' in query or 'plans' in query or 'plan' in query:
                    try:
                        speak('Checking upcoming meetings')
                        service = authenticate_google()
                        day = get_date(query)
                        get_events(get_date(query), service)
                    except:
                        speak('Unable to find meeting right now')
        elif 'open google' in query:
                    webbrowser.open('www.google.com')
                    speak('Opened Google')
        elif 'time table' in query:
                    speak('opening time table')
                    os.system('xdg-open /home/shubharthak/Desktop/timetable.png')
        elif 'set meeting' in query and 'bro' in query:
                    speak('Please specify the day or the date')
                    date = takeCommand2().lower()
                    speak('Creating event with Bhayiya')
                    service = authenticate_google()
                    print(get_date(date))
                    create_event(get_date(date), service, emails['bro'], summary='Meeting with Bhayiya')
        elif 'set meeting' in query and 'bhabhi' in query or 'set meeting' in query and 'bhaabhi' in query:
                    speak('Please specify the day or the date')
                    date = takeCommand2().lower()
                    speak('Creating event with Bhaabhi')
                    service = authenticate_google()
                    print(get_date(date))
                    create_event(get_date(date), service, emails['bhabhi'], summary='Meeting with Bhabhi')
        elif 'mute' in query or 'unmute' in query:
            os.system('pactl set-sink-mute @DEFAULT_SINK@ toggle')
        elif 'increase' in query:
            query = query.replace('increase', '')
            query = int(query)
            os.system(f'pactl set-sink-volume 0 +{query}%')
        elif 'decrease' in query:
            query = query.replace('decrease', '')
            query = int(query)
            print(query)
            os.system(f'pactl set-sink-volume 0 -{query}%')

        elif 'open cloud' in query or 'open oracle' in query:
                    open_cloud()
        elif 'open netflix' in query:
                    open_netflix()
        elif 'send message' in query or 'message' in query:
                    speak('To whom you want to send message')
                    user = takeCommand3()
                    speak('Tell me your message')
                    message = takeCommand4()
                    message += ' Send By ApsaraAI'
                    speak(f'your message is {message} to {user}')
                    speak('Confirm me yes or no')
                    confirm = takeCommand3().lower()
                    if 'yes' in confirm:
                        speak('Sending Message')
                        os.system(f'python whatsapp.py {user} {message}')
                        speak('Message sent successfully')
                    if 'no' in confirm:
                        speak('okay')            
    except Exception as e:
        print(e)
        print('unable to say right now!!')
        

#Driver Code
if __name__ == "__main__":
    schedule.every().day.at('08:00').do(wake_up_shubh)
    MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    DAY_EXTENSIONS = ["nd", "rd", "th", "st"]
    device_name2 = 'OPPO F17 Pro'
    device_name = 'shubharthak'
    device_name3 = 'Web Player (Firefox)'
    say = ['Haan ji boliye?', 'ji boliye?', 'Yes sir?', 'ji boliye sir?']
    greet = ['I am Apsara designed by Shubharthak Sir. Please tell me how may I help you','Mera naam Apsara hai. Mujhe Shubharthak Sir nei design kiya hai, Please Bataayein Maii Aapki kya Sevaa Karoon?']
    wishMe()
    speak(random.choice(greet))
    spotify, deviceID = spotify()    
    print(spotify.current_user())
    run('apsara what is your name')
    
