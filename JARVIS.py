import pyttsx3
import speech_recognition as sr
import os
import datetime
import wikipedia
import webbrowser
import random
import subprocess

# Initialize pyttsx3 engine with 'sapi5', set default voice.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# list of random responses
responses = ["Hello! I'm JARVIS. How can I assist you today?",
    "Greetings! What can I do for you?",
    "Hi there! Ready to tackle some tasks?",
    "Good day! How may I be of service?",
    "Hey! What's on your mind?",
    "Welcome back! What do you need help with?",
    "Hiya! How can I help you today?",
    "Hello there! What's the plan for today?",
    "Hey! Need a hand with something?",
    "Good to see you! What's new?",
    "Hi! How's your day going?",
    "Hey there! Let's get productive!",
    "Hi! What can I do to make your day better?",
    "Hello! Ready for another adventure?",
    "Hey! Need assistance with anything specific?",
    "Hiya! How can I make your day easier?",
    "Hello there! Let's make today awesome!",
    "Hey! What's the word?",
    "Hi! How can I make your life easier today?",
    "Greetings! How can I assist you?",
    "Hey! Need a little JARVIS magic?",
    "Hi there! Let's make today a great day!",
    "Hey! What's the buzz?",
    "Good morning! How can I help you today?",
    "Hey there! Need a little pick-me-up?",
    "Hello! Ready to conquer the day?",
    "Greetings! How can I lend a hand?",
    "Hey! Let's make today a productive one!",
    "Hi! How's it going?",
    "Hey there! What's the latest?",
    "Hello! Let's make today a great day!",
    "Hey! What can I do to assist you?",
    "Hiya! How's everything going?",
    "Hello! How can I make your day better?",
    "Greetings! Ready for action?",
    "Hey! Need some JARVIS magic?",
    "Hi there! Let's tackle today's challenges!",
    "Hey! What's on your agenda today?",
    "Hi! How can I assist you today?",
    "Hello! Let's make today amazing!",
    "Hey there! Need a helping hand?",
    "Hiya! What's the plan for today?",
    "Greetings! How can I make your day better?",
    "Hey! Need some assistance?",
    "Hi! How can I make your life easier?",
    "Hello! Let's get started!",
    "Hey! What can I do for you today?",
    "Hi there! How can I assist you?",
    "Hello! Ready to make today awesome?",
    "Hey! Need some JARVIS magic today?",]


#say function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# wishme function 
def wishme():
    current_time = datetime.datetime.now()
    current_hours = current_time.hour
    current_minutes = current_time.minute
    current_seconds = current_time.second
    time = (f"current_time : {current_hours}:{current_minutes}:{current_seconds}")
    print(time)
    if 5<= current_hours <12:
        print("Good Morning")
    elif 12<= current_hours <16:
        print("Good Afternoon")
    elif 16<= current_hours <21:
        print("Good Evening")
    else:
        print("Good NIght")
    
    random_responses = random.choices(responses)
    print(random_responses)
    speak(random_responses)


# command function for speech recognition
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("JARVIS is listening....")
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language = "en-in")
        print(f"User said: {query}")

    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"
    return query

if __name__ ==  "__main__":
    name = input("enter your name")
    speak(f"{name}, Welcome to Jarvis !")
    wishme()

# for execution of instructions
    if True:
        query = command().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        if 'open google' in query:
            webbrowser.open("google.com")

        if 'date and time' in query:
            date_time = datetime.datetime.now()
            print(f"time is : {date_time.hour}:{date_time.minute}:{date_time.second}")

        if 'open vscode' in query:
            os.startfile("C:\\Users\\91885\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code")

        if 'open gta5' in query:
            try:
                subprocess.Popen("D:\\Launcher\\LauncherPatcher.exe")
            except Exception as e:
                print(e)
                print("An error occured. Try again")