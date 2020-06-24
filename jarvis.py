import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from youtube_search import YoutubeSearch


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12:
        speak("Good morning !")

    elif hour >= 12 and hour < 16:
        speak("Good afternoon !")

    elif hour >= 16 and hour < 20:
        speak("Good evening !")

    else:
        speak("Good night !")

    speak(
        "i am jarvis sir ! speed 1 terahertz , memory 1 terabyte . please tell me how may i help you !"
    )


def takeCommand():
    #  it takes microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")

    except Exception as e:
        # print("e")
        print("say that again please....")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # this statement for wikipedia search
        if "wikipedia" in query:
            speak("Searching for result ....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        # this statement for youtube search
        elif "youtube" in query:
            query = query.replace("youtube", "")
            speak("Searching for result ....")
            url = "https://www.youtube.com/results?search_query="
            search_url = url + query
            webbrowser.open(search_url)

        # this statement for facebook
        elif "facebook" in query:
            webbrowser.open("https://www.facebook.com/")

        # this statement for date and time
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir the time is {strTime}")

        elif "the date" in query:
            strDate = datetime.datetime.now().strftime("%D %M %Y")
            print(strDate)
            speak(f"sir the date is {strDate}")

        # this statement for my personal choice
        elif "not in good mood" in query:
            speak("should i play music for you !")
            if "yes" in query:
                webbrowser.open("https://youtu.be/ezAtfMxqUWQ?list=RDqw1CVt43VKw")
                print("enjoy the music")
                break

        # this statement for google search
        elif "search for" in query:
            query = query.replace("search for", "")
            speak("Searching for result ....")
            url = "https://www.google.com/search?q="
            search_url = url + query
            webbrowser.open(search_url)

        elif "jarvis" in query:
            speak("i am listening sir")

        elif "quit" in query:
            speak("jarvis terminated")
            exit()
