import smtplib
import speech_recognition as sr
from Body.Speak import Speak
import os

# Define the path to the contacts file
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_DIR = os.path.join(CURRENT_DIR, '..', 'Brain', 'Database')
CONTACTS_FILE = os.path.join(DATABASE_DIR, 'email_data.txt')

def load_contacts():
    contacts = {}
    with open(CONTACTS_FILE, "r") as file:
        for line in file:
            name, email = line.strip().split(",")
            contacts[name.strip()] = email.strip()
    return contacts

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source, 0, 20)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en")
        print(query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        print("Sorry, I'm having trouble accessing the recognition service.")

Email_FILE = os.path.join(DATABASE_DIR, 'email_id_pass.txt')
def get_credentials():
    with open(Email_FILE, 'r') as file:
        lines = file.readlines()
        email = lines[0].strip()
        password = lines[1].strip()
    return email, password

def send_email(to, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        email, password = get_credentials()
        server.login(email, password)
        server.sendmail(email, to, message)
        Speak("Message sent successfully")
        return True
    except smtplib.SMTPAuthenticationError:
        Speak("Authentication error: Please check your email credentials.")
    except smtplib.SMTPException as e:
        Speak(f"An error occurred: {e}")
    finally:
        server.quit()

def send_email_prompt():
    contacts = load_contacts()
    Speak("To whom do you want to send the email?")
    recipient = listen()
    if not recipient:
        Speak("Please try again by using the command, Send Email")
        return True
    to = ""
    for name, email in contacts.items():
        if name in recipient:
            to = email
            break

    if not to:
        Speak("Recipient not recognized. Please try again by using the command, Send Email")
        return True

    Speak("What message do you want to send?")
    message = listen()
    if not message:
        Speak("Message cannot be empty. Please try again by using the command, Send Email")
        return True

    send_email(to, message)
    return True

if __name__ == "__main__":
    send_email_prompt()
