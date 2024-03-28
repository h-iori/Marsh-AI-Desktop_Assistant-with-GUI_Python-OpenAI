import eel
import sys
import os
import subprocess
from Brain.MarshBrain import ReplyBrain
from Body.Speak import Speak
from Body.Listen import MicExecution
from Main import MainTaskExecution

# Initialize Eel
eel.init('web')
os.system('start msedge.exe --start-maximized --app="http://localhost:8000/index.html"')
# Expose Python functions to JavaScript
@eel.expose
def start_assistant():
    Speak("Hello Sir")
    Speak("What can I do for you?")

    while True:
        data = MicExecution()
        data = str(data)
        value_return = MainTaskExecution(data)

        if value_return:
            pass
        elif len(data) < 3:
            pass
        else:
            reply = ReplyBrain(data)
            Speak(reply)

@eel.expose
def exit_program():
    Speak("Ok, I'll see you later")
    sys.exit()


script_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(script_dir, 'Brain', 'Database', 'API.txt')

@eel.expose
def saveTextToFile(data):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, 'Brain', 'Database', 'API.txt')
    with open(file_path, 'w') as file:
        file.write(data)

@eel.expose
def openapi():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, 'Brain', 'Database', 'API.txt')
    subprocess.Popen(['notepad.exe', file_path])


@eel.expose
def savecredToFile(email, password):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, 'Brain', 'Database', 'email_id_pass.txt')
    formatted_cred = f"{email}\n{password}\n"
    with open(file_path, 'w') as file:
        file.write(formatted_cred)

@eel.expose
def opencred():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, 'Brain', 'Database', 'email_id_pass.txt')
    subprocess.Popen(['notepad.exe', file_path])

@eel.expose
def saveemailToFile(data):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, 'Brain', 'Database', 'email_data.txt')
    with open(file_path, 'a') as file:
        file.write(data + '\n')

@eel.expose
def openemail():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, 'Brain', 'Database', 'email_data.txt')
    subprocess.Popen(['notepad.exe', file_path])

@eel.expose
def savechatToFile(question, answer):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, 'Brain', 'Database', 'chat_log.txt')
    formatted_log = f"You: {question}\nMarsh: {answer}\n"
    with open(file_path, 'a') as file:
        file.write(formatted_log)

@eel.expose
def openchat():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, 'Brain', 'Database', 'chat_log.txt')
    subprocess.Popen(['notepad.exe', file_path])

eel.start('index.html',mode=None, host='localhost', block=True)

