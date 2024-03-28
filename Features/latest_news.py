from Body.Speak import Speak
import requests
import json
import speech_recognition as sr


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source, 0, 5)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en")
        print(query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        print("Sorry, I'm having trouble accessing the recognition service.")

def latestnews():
    try:
        api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=5cae6364b921480cb5e8f0360f2f3f42",
                "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=5cae6364b921480cb5e8f0360f2f3f42",
                "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=5cae6364b921480cb5e8f0360f2f3f42",
                "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=5cae6364b921480cb5e8f0360f2f3f42",
                "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=5cae6364b921480cb5e8f0360f2f3f42",
                "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=5cae6364b921480cb5e8f0360f2f3f42"
    }

        counter = 0
        url = None
        Speak("Of course! What specific topics are you interested in? For example: Technology, Sports....")
        field = listen()
        for key ,value in api_dict.items():
            if key.lower() in field.lower():
                url = value
                break
            

        news = requests.get(url).text
        news = json.loads(news)
        Speak("Here are the top 5 headlines.")

        arts = news["articles"]
        for articles in arts :
            article = articles["title"]
            Speak(article)
            counter += 1
            if counter >= 5:
                break
        Speak("Is there anything else i can help you with?")
        return True
    except:
        Speak("I apologize, i was not able to find any news.")
        return True

