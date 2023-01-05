# import libraries required from tweety_lib_imports.py file
from tweety_lib_imports import *

# Initialize python text to speech engine with a voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# Set voice ID to '0' for Male voice, '1' for Female Voice
engine.setProperty('voice', voices[1].id)


# utility functions
# This function helps Tweety to speak
def tweety_speaks(command):
    engine.say(command)
    engine.runAndWait()


# Loading the virtual assistant
def load_tweety():
    response_load = "Loading your Virtual Voice Assistant..."
    print(response_load)
    tweety_speaks(response_load)


# This function helps Tweety to wish the user whenever the session starts.
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        tweety_speaks("Hello, Good Morning, I am your virtual voice assistant tweety")
        print("Hello,Good Morning, I am your virtual voice assistant tweety")
    elif 12 <= hour < 18:
        tweety_speaks("Hello,Good Afternoon, I am your virtual voice assistant tweety")
        print("Hello,Good Afternoon, I am your virtual voice assistant tweety")
    else:
        tweety_speaks("Hello,Good Evening, I am your virtual voice assistant tweety")
        print("Hello,Good Evening, I am your virtual voice assistant tweety")


# This function helps Tweety to take custom commands from user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

        try:
            print("Recognizing...")
            user_response = r.recognize_google(audio, language='en-us')
            print(f'user command:{user_response}\n')
        except Exception as e:
            tweety_speaks("Pardon me, can you please say that again")
            print("Pardon me, can you please say that again")
            takeCommand()
    return user_response


# This function helps Tweety to get the user information
def user_info():
    tweety_speaks("May i know your name?")
    print("May i know your name?")
    try:
        user_name = str(takeCommand())
        if user_name:
            tweety_speaks("Hello " + user_name)
            print("Hello " + user_name)
    except Exception as e:
        tweety_speaks("Pardon me")
        print("Pardon me")
        user_info()
    return user_name


# This function helps Tweety to send an email
def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    email_id = "use your email id"
    server.login(email_id, 'email_password')
    server.sendmail(email_id, to, content)
    server.close()
    return True


# This function helps to execute the user commands using webbrowser instance.
def execute_webbrowser(user_search, type):
    print("your search: " + user_search)
    if type == 'website':
        webbrowser.open(user_search)
        first_dot_idx = user_search.index('.')
        second_dot_idx = user_search.rindex('.')
        website_name = user_search[first_dot_idx + 1:second_dot_idx]
        tweety_speaks(website_name + " is open now")
        print(website_name + " is open now")
        time.sleep(5)
    elif type == 'query':
        webbrowser.open(user_search)
        time.sleep(5)


# This function helps to execute the user commands using webbrowser instance.
def execute_wolframalpha():
    query = takeCommand()
    app_id = "your_id"
    client = wolframalpha.Client(app_id)
    res = client.query(query)
    try:
        answer = next(res.results).text
        tweety_speaks(answer)
        print(answer)
    except StopIteration:
        tweety_speaks("Sorry no results found")
        print("Sorry no results found")


# This function helps to execute the user commands using subprocess instance
def execute_subprocess(type):
    subprocess.call("shutdown / h") if type == 'h' else subprocess.call(["shutdown", type])  # if else one-liner
