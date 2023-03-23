import pyttsx3 
import speech_recognition as sr             
import datetime                #import date and time
import wikipedia
import webbrowser
from termcolor import colored

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():  
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir. ")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir. ")

    else:
        speak("Good Evenning Sir") 

    
    speak(" I am Jarvis. How can i help You..! ")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
           print(colored("Listening...\n","green"))
           r.pause_threshold = 1
           audio = r.listen(source)

    try:
          print("<--- Recognizing --->")
          query = r.recognize_google(audio,language = 'en-in')
          print(colored("\nUser Command : ", "blue"),f"{query}\n")

    except Exception as e:
        #   print(e)
          speak("Please Say that Again.")
          print("Please Say that Again.")
          return "None"
          
    return query
     
if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
        if "wikipedia" in query:
              speak("Searching in Wikipedia ...")
              query = query.replace("wikipedia","")
              results = wikipedia.summary(query, sentences = 1)
              speak("According To wikipedia")
              print(results)
              speak(results)
        elif "open youtube" in query:
             webbrowser.open("youtube.com")
        elif "open chrome" in query:
             webbrowser.open("Chrome")
        elif "open google" in query:
             webbrowser.open("google.com")
        elif "time" in query:
             strtime = datetime.datetime.now().strftime("%H : %M : %S")
             print(f"The Time is {colored(strtime,'green')}\n")
        elif "shutdown jarvis" or "shutdown system" in query:
             speak("Ok sir, Shutting down system.")
             exit()
        