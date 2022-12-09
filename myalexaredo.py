#necessary lib. imports required for Tweety - The virtual voice assistant to work.
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import random
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import smtplib
import ctypes
import winshell
import pyjokes
import json
from twilio.rest import Client
from ecapture import ecapture as ec
from urllib.request import urlopen

#This function helps Tweety to speak
def tweety_speaks(command):
    engine.say(command)
    engine.runAndWait()

#This function helps Tweety to wish the user whenever the session starts.
def wish_me():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        tweety_speaks("Hello, Good Morning, How may I assist you?")
        print("Hello,Good Morning, How may I assist you?")
    elif hour>=12 and hour<18:
        tweety_speaks("Hello,Good Afternoon, How may I assist you?")
        print("Hello,Good Afternoon, How may I assist you?")
    else:
        tweety_speaks("Hello,Good Evening, How may I assist you?")
        print("Hello,Good Evening, How may I assist you?")
    tweety_speaks("I am your virtual voice assistant tweety")
    print("I am your virtual voice assistant tweety")

#Initialize python text to speech engine with a voice
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

#Set voice ID to '0' for Male voice, '1' for Female Voice
engine.setProperty('voice','voices[0].id') 

#This function helps Tweety to take custom commands from user
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            user_response=r.recognize_google(audio,language='en-in')
            print(f'user command:{user_response}\n')
        except Exception as e:
            tweety_speaks("Pardon me, can you please say that again")
            print("Pardon me, can you please say that again")
            return "None"
        return user_response

#This function helps Tweety to get the user information
def user_info():
    tweety_speaks("May i know your name?")
    print("May i know your name?")
    user_name = str(takeCommand())
    if(user_name):
        tweety_speaks("Hello " + user_name)
        print("Hello " + user_name)

#This function helps Tweety to send an email
def send_email(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    email_id = "use your email id"
    server.login(email_id, 'email_password')
    server.sendmail(email_id, to, content)
    server.close()
    return True

#This function helps to execute the user commands using webbrowser instance.
def execute_webbrowser(search, type):
    if type == 'website':
        webbrowser.open_new_tab(search)
        tweety_speaks(search + " is open now")
        print(search + " is open now")
        time.sleep(5)
    elif type == 'query':
        webbrowser.open_new_tab(search)
        time.sleep(5)

#This function helps to execute the user commands using webbrowser instance.
def execute_wolframalpha():
    query = takeCommand()
    app_id="your_id"
    client = wolframalpha.Client(app_id)
    res = client.query(query)
    try:
        answer = next(res.results).text
        tweety_speaks(answer)
        print(answer)
    except StopIteration:
        tweety_speaks("Sorry no results found")
        print("Sorry no results found")

#This function helps to execute the user commands using subprocess instance
def execute_subprocess(type):
    subprocess.call("shutdown / h") if type == 'h' else subprocess.call(["shutdown", type]) #if else one liner

if __name__=='__main__':
    #the below line of code clears the console
    #before tweety turns up
    clear = lambda: os.system('cls')
    clear()

    #Loading the virtual assistant
    response_load="Loading your AI Virtual Assistant - Tweety"
    print(response_load)
    tweety_speaks(response_load)

    #Wish and get the user info
    wish_me()
    user_name = user_info()

    while True:
        tweety_speaks(f"Hello {user_name} Tell me how can I help you now?")
        print(f"Hello {user_name} Tell me how can I help you now?")
        command = takeCommand().lower()

        if command == 0 or command == None:
            continue

        elif "tweety" in command:
            wish_me()
            tweety_speaks("Hey {} i am awake".format(user_name))
            print("Hey {} i am awake".format(user_name))

        elif 'wikipedia' in command:
            tweety_speaks('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=3)
            print("According to Wikipedia" + results)
            tweety_speaks("According to Wikipedia" + results)
        
        #webbrowser based actions
        elif 'open wikipedia' in command:
            execute_webbrowser("https://www.wikipedia.com","website")

        elif 'open stackoverflow' in command:
            execute_webbrowser("https://www.stackoverflow.com","website")

        elif 'open youtube' in command:
            execute_webbrowser("https://www.youtube.com","website")

        elif 'open google' or 'open google chrome' in command:
            execute_webbrowser("https://www.google.com","website")

        elif 'open gmail' in command:
            execute_webbrowser("https://www.gmail.com","website")
        
        elif 'search'  in command:
            command = command.replace("search", "")
            execute_webbrowser(command,"query")

        elif "where is " in command:
            location = command.replace("where is ","")
            tweety_speaks("Locating " + location)
            location_search_link = "https://www.google.nl / maps / place/" + location + ""
            execute_webbrowser(location_search_link, "query")

        #send mail to custom recipient
        elif 'send a mail' in command:
            try:
                tweety_speaks("whom should i send the mail?")
                print("whom should i send the mail?")
                to = input()
                tweety_speaks("what should i say?")
                print("what should i say?")
                mail_body = takeCommand()
                mail_sent_status = send_email(to, mail_body)
                if(mail_sent_status == True):
                    tweety_speaks("The email has been sent!")
                    print("The email has been sent!")
            except Exception as e:
                print(e)
                tweety_speaks("Sorry! I am unable to send the email")

        elif "send message" in command or "text message" in command:
            #create an account on Twilio to access the service
            acnt_sid = "Your account Sid key"
            auth_token = "Your auth token"
            client = Client(acnt_sid, auth_token)
            message = client.messages.create(
                                        body = takeCommand(),
                                        from_  = "Sender Number",
                                        to = "Recipient Number"
            )
            print(message.sid)
            tweety_speaks("Message sent successfully to the recipient")

        #get latest news updates
        elif 'news' in command:
            try:
                json_object = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                headlines = json.load(json_object)
                i = 1
            
                tweety_speaks('here are some top news from the times of india')
                print("=============== TIMES OF INDIA ============"+ '\n')
                 
                for item in headlines['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    tweety_speaks(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:   
                print(str(e))
                tweety_speaks("Oops! An error occured while fetching the news")

        #get latest weather updates with city name.
        elif "weather" in command:
            api_key="Your Own API key"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            tweety_speaks("what is the city name")
            print("what is the city name")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["code"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                tweety_speaks(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
            else:
                tweety_speaks("Requested City Not Found")

        #taking a note into a file - file handling case
        elif "write a note" in command or "take a note" in command:
            tweety_speaks("what do i need to jot down")
            note = takeCommand()
            note_file = open("tweety_notes.txt", "w")
            tweety_speaks("Should i include date and time")
            include_dt = takeCommand()
            if "yes" in include_dt or "yeah" in command or "sure" in command:
                noting_time = datetime.datetime.now().strftime("% H:% M:% S")
                note_list = [noting_time, " :- ", note]
                note_file.writelines(note_list)
            else:
                note_file.write(note)

        elif "show note" in command or "read notes" in command:
            tweety_speaks("Speaking out notes")
            if os.stat("tweety_notes.txt").st_size == 0:
                tweety_speaks("Oops! the notes is empty")
            else:
                with open("tweety_notes.txt") as f:
                    contents = f.read()
                    print(contents)
                    tweety_speaks(contents)

        #get answers to computational and geographical queries
        elif "what is" in command or "who is" in command:
            execute_wolframalpha()

        elif "ask" in command:
            tweety_speaks('I can answer most of your questions because i am still learning and now what question do you want to ask now')
            execute_wolframalpha()
        
        elif 'calculate' in command:
            api_id = "Wolframalpha api id"
            client = wolframalpha.Client(api_id)
            idx = query.lower().split().index('calculate')
            query = query.split()[idx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The result is " + answer)
            tweety_speaks("The result is " + answer)

        #most shooted commands/questions 
        elif 'time' in command:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            tweety_speaks(f"the current time is {strTime}")
            time.sleep(5)
        
        elif 'joke' in command or "tell me a joke" in command:
            joke = pyjokes.get_joke()
            tweety_speaks(joke)
            print(joke)

        elif 'how are you' in command or 'how are you doing' in command:
            how_are_you_responses = ["i am doing good thank you", "i am doing great indeed i feel better today", "i am feeling happy as you are with me", "i am good hope you are doing well too"]
            s = random.choice(how_are_you_responses)
            tweety_speaks(s)
            print(s)
            time.sleep(5)

        elif 'who are you' in command or 'what is your name' in command or 'what can you do' in command:
            tweety_speaks('I am Tweety version 1 point O your personal virtual vocie assistant. I am programmed to perform minor tasks like'
                  'opening youtube,google chrome,gmail, stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can also ask me computational or geographical questions too!')

        elif "who made you" in command or "who created you" in command or "who discovered you" in command or "reason for your invention" in command:
            tweety_speaks("I have been created by Polu Tharun Kumar Reddy")
            print("I have been created by Polu Tharun Kumar Reddy")

        elif "i love you" in command or "love" in command:
            tweety_speaks("It is hard to understand")

        elif "will you be my gf" in query or "will you be my bf" in query:  
            tweety_speaks("I'm not sure about, may be you should give me some time")

        elif "who i am" in command or "who am i" in command:
            tweety_speaks("If you can talk and think then definitely you are human")
        
        elif "why do you exist" in command or "why are you created" in command:
            tweety_speaks("Thanks to Polu Tharun Kumar Reddy. further details is a top secret")

        elif 'what is love' in query:
            tweety_speaks("It is 7th sense that destroy all other senses")

        elif "camera" in command or "take a photo" in command or "capture " in command:
            ec.capture(0,"Tharun camera","img.jpg")
        
        elif "empty recycle bin" in command:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, Sound = True)
            tweety_speaks("Recycle Bin in clean now")

        #turnoff commands
        elif "restart" in command:
            tweety_speaks("restarting the system")
            execute_subprocess("/r")
        
        elif "hibernate" in command or "go to sleep" in command:
            tweety_speaks("Hibernating...")
            execute_subprocess('h')

        elif "lock screen" in command or "lock window" in command:
            tweety_speaks("locking the current device")
            ctypes.windll.user32.LockWorkStation()

        elif "good bye" in command or "exit" in command or "ok bye" in command or "stop" in command:
            tweety_speaks('your personal assistant Tweety is shutting down,Good bye')
            print('your personal assistant Tweety is shutting down,Good bye')
            break

        elif "don't listen" in command or "stop listening" in command:
            tweety_speaks("How much time you want me to halt from listening to you")
            sleep_time = int(takeCommand)
            time.sleep(sleep_time)
            print("Stopped listening to your commands for" + sleep_time + "seconds")

        elif "log off" in command or "sign out" in command or "shut down" in command:
            tweety_speaks("Hold on , your pc will log off in 10 sec make sure you exit from all currently working or running applications")
            execute_subprocess("/l")

time.sleep(5)
