#necessary lib. imports required for Tweety - The virtual voice assistant to work.
import ctypes
import datetime
import json
import os
import random
import smtplib
import subprocess
import time
import webbrowser
from urllib import request
from urllib.request import urlopen
import pyjokes
import pyttsx3
import speech_recognition as sr
import wikipedia
import winshell
import wolframalpha
from ecapture import ecapture as ec
from twilio.rest import Client

#Initialize python text to speech engine with a voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#Set voice ID to '0' for Male voice, '1' for Female Voice
engine.setProperty('voice', voices[1].id) 

#utility functions
#This function helps Tweety to speak
def tweety_speaks(command):
    engine.say(command)
    engine.runAndWait()

#Loading the virtual assistant
def load_tweety():
    response_load = "Loading your Virtual Voice Assistant..."
    print(response_load)
    tweety_speaks(response_load)

#This function helps Tweety to wish the user whenever the session starts.
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        tweety_speaks("Hello, Good Morning, I am your virtual voice assistant tweety")
        print("Hello,Good Morning, I am your virtual voice assistant tweety")
    elif hour >= 12 and hour < 18:
        tweety_speaks("Hello,Good Afternoon, I am your virtual voice assistant tweety")
        print("Hello,Good Afternoon, I am your virtual voice assistant tweety")
    else:
        tweety_speaks("Hello,Good Evening, I am your virtual voice assistant tweety")
        print("Hello,Good Evening, I am your virtual voice assistant tweety")

#This function helps Tweety to take custom commands from user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

        try:
            print("Recognizing...")
            user_response = r.recognize_google(audio,language='en-us')
            print(f'user command:{user_response}\n')
        except Exception as e:
            tweety_speaks("Pardon me, can you please say that again")
            print("Pardon me, can you please say that again")
            takeCommand()
    return user_response

#This function helps Tweety to get the user information
def user_info():
    tweety_speaks("May i know your name?")
    print("May i know your name?")
    try:
        user_name = str(takeCommand())
        if(user_name):
            tweety_speaks("Hello " + user_name)
            print("Hello " + user_name)
    except Exception as e:
        tweety_speaks("Pardon me")
        print("Pardon me")
        user_info()
    return user_name

#This function helps Tweety to send an email
def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    email_id = "use your email id"
    server.login(email_id, 'email_password')
    server.sendmail(email_id, to, content)
    server.close()
    return True

#This function helps to execute the user commands using webbrowser instance.
def execute_webbrowser(user_search, type):
    print("your search: " + user_search)
    if type == 'website':
        webbrowser.open(user_search)
        first_dot_idx = user_search.index('.')
        second_dot_idx = user_search.rindex('.')
        website_name = user_search[first_dot_idx+1:second_dot_idx]
        tweety_speaks(website_name + " is open now")
        print(website_name + " is open now")
        time.sleep(5)
    elif type == 'query':
        webbrowser.open(user_search)
        time.sleep(5)

#This function helps to execute the user commands using webbrowser instance.
def execute_wolframalpha():
    query = takeCommand()
    app_id ="your_id"
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

    #loading the assistant, starts with a Wish and gets the user info
    load_tweety()
    wish_me()
    #user_name = user_info()
    user_name = "tharun"
    tweety_speaks(f"Hope you are doing great Tell me how can I help you now?")
    print(f"{user_name},Hope you are doing great. Tell me how can I help you now?")

    repeat_intro = ["Do you have any other questions", "Do i have any further questions if not i can take a short nap just kidding", "How can i help you furthermore please say yes if you have any queries"]

    # Below variable keeps track of tweety voice assistant usage
    usage_count = 1
    while True:
        #check if tweety is ready to ans the second question
        if usage_count >= 2:
            ask_next_query = random.choice(repeat_intro)
            tweety_speaks(ask_next_query)
            print(ask_next_query)
            next_command = takeCommand().lower()
            if next_command == "yes":
                usage_count = 1
                continue
            else:
                #print("in else") for debugging purpose
                break

        command = str(takeCommand().lower())
        print(command)

        if command == '':
            break
        else:
            if "tweety" in command:
                wish_me()
                tweety_speaks("Hey {} i am awake".format(user_name))
                print("Hey {} i am awake".format(user_name))

            if 'wikipedia' in command:
                tweety_speaks('Searching Wikipedia...')
                command = command.replace("wikipedia", "")
                if(command != ''):
                    results = wikipedia.summary(command, sentences=3)
                    print("According to Wikipedia" + results)
                    tweety_speaks("According to Wikipedia" + results)
                else:
                    tweety_speaks("please try again")
            
            #webbrowser based actions
            if 'stack overflow' in command:
                execute_webbrowser("https://www.stackoverflow.com","website")
                
            if 'google' in command:
                execute_webbrowser("https://www.google.com", "website")

            if 'youtube' in command:
                execute_webbrowser("https://www.youtube.com","website")

            if 'gmail' in command:
                execute_webbrowser("https://www.gmail.com","website")
            
            if 'search'  in command:
                command = command.replace("search ", "")
                if(command != ''):
                    parsed_command = "https://www.google.com/search?q=" + command
                    execute_webbrowser(parsed_command,"query")
                else:
                    tweety_speaks("Please check there is nothing to search")
                    print("Please check there is nothing to search")

            if "where is " in command:
                location = command.replace("where is ","")
                tweety_speaks("Locating " + location)
                location_search_link = "https://www.google.nl / maps / place/" + location + ""
                execute_webbrowser(location_search_link, "query")

            #send mail to custom recipient
            if 'send a mail' in command:
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

            if "send message" in command or "text message" in command:
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

            #get latest news updates using news api - Third Party API case
            if 'news' in command:
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

            #get latest weather updates with city name using openweathermap - Third Party API case
            if "weather" in command:
                api_key="Your Own API key"
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                tweety_speaks("what is the city name")
                print("what is the city name")
                city_name = takeCommand()
                complete_url = base_url+"appid="+api_key+"&q="+city_name
                response = request.get(complete_url)
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
            if "write a note" in command or "take a note" in command:
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

            #reading the taken note in file - file handling case
            if "show note" in command or "read notes" in command:
                tweety_speaks("Speaking out notes")
                if os.stat("tweety_notes.txt").st_size == 0:
                    tweety_speaks("Oops! the notes is empty")
                else:
                    with open("tweety_notes.txt") as f:
                        contents = f.read()
                        print(contents)
                        tweety_speaks(contents)

            #get answers to computational and geographical queries
            if "what is" in command or "who is" in command:
                execute_wolframalpha()

            if "ask" in command:
                tweety_speaks('I can answer most of your questions because i am still learning and now what question do you want to ask now')
                execute_wolframalpha()
            
            if 'calculate' in command:
                api_id = "Wolframalpha api id"
                client = wolframalpha.Client(api_id)
                idx = query.lower().split().index('calculate')
                query = query.split()[idx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The result is " + answer)
                tweety_speaks("The result is " + answer)

            #most shooted commands/questions 
            if 'time' in command:
                str_time = datetime.datetime.now().strftime("%H:%M:%S")
                tweety_speaks(f"the current time is {str_time}")
                time.sleep(5)
            
            if 'joke' in command or "tell me a joke" in command:
                joke = pyjokes.get_joke()
                tweety_speaks(joke)
                print(joke)

            if 'how are you' in command or 'how are you doing' in command:
                how_are_you_responses = ["i am doing good thank you", "i am doing great indeed i feel better today", "i am feeling happy as you are with me", "i am good hope you are doing well too"]
                s = random.choice(how_are_you_responses)
                tweety_speaks(s)
                print(s)
                time.sleep(5)

            if 'who are you' in command or 'what is your name' in command or 'what can you do' in command:
                tweety_speaks('I am Tweety version 1 point O your personal virtual vocie assistant. I am programmed to perform minor tasks like'
                    'opening youtube,google chrome,gmail, stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                    'in different cities , get top headline news from times of india and you can also ask me computational or geographical questions too!')

            if "who made you" in command or "who created you" in command or "who discovered you" in command or "reason for your invention" in command:
                tweety_speaks("I have been created by Polu Tharun Kumar Reddy")
                print("I have been created by Polu Tharun Kumar Reddy")

            if "i love you" in command or "love" in command:
                tweety_speaks("It is hard to understand")

            if "will you be my gf" in command or "will you be my bf" in command:  
                tweety_speaks("I'm not sure about, may be you should give me some time")

            if "who i am" in command or "who am i" in command:
                tweety_speaks("If you can talk and think then definitely you are human")
            
            if "why do you exist" in command or "why are you created" in command:
                tweety_speaks("Thanks to Polu Tharun Kumar Reddy. further details is a top secret")

            if 'what is love' in command:
                tweety_speaks("It is 7th sense that destroy all other senses")

            if "camera" in command or "take a photo" in command or "capture " in command:
                ec.capture(0,"Tharun camera","img.jpg")
            
            if "empty recycle bin" in command:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, Sound = True)
                tweety_speaks("Recycle Bin in clean now")

            #turnoff commands
            if "restart" in command:
                tweety_speaks("restarting the system")
                execute_subprocess("/r")
            
            if "hibernate" in command or "go to sleep" in command:
                tweety_speaks("Hibernating...")
                execute_subprocess('h')

            if "lock screen" in command or "lock window" in command:
                tweety_speaks("locking the current device")
                ctypes.windll.user32.LockWorkStation()

            if "good bye" in command or "exit" in command or "ok bye" in command or "stop" in command:
                tweety_speaks('your personal assistant Tweety is shutting down,Good bye')
                print('your personal assistant Tweety is shutting down,Good bye')
                break

            if "don't listen" in command or "stop listening" in command:
                tweety_speaks("How much time you want me to halt from listening to you")
                sleep_time = int(takeCommand)
                time.sleep(sleep_time)
                print("Stopped listening to your commands for" + sleep_time + "seconds")

            if "log off" in command or "sign out" in command or "shut down" in command:
                tweety_speaks("Hold on , your pc will log off in 10 sec make sure you exit from all currently working or running applications")
                execute_subprocess("/l")

        #increment tweety usage count by 1 after every usage
        usage_count += 1

#standard 5 seconds sleep time before next run
time.sleep(5)
