import pyttsx3
import eel
def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[2].id)
    engine.setProperty('rate',160)
    print("")
    print(f"Marsh : {Text}.")
    print("")
    engine.say(Text)
    eel.DisplayMessage(Text)
    engine.runAndWait()

