# Marsh- AI Desktop Assistant with GUI Python-OpenAI
  
This project is an AI-powered desktop assistant that can perform various tasks and uses  OpenAI API for answering. 
It uses Python as the programming language. 


## User Interface
HTML5, CSS3, Javascript, ( Python-EEL )-Backend

## API Key Generation

#### You need to generate a unique API key from  

```http
  https://platform.openai.com/api-keys
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

You have to add your own unique api key in the MarshBrain.py file.



## GUI
API Button: Before using the project, you need to add the API key here.

Email Button: The assistaant is able to send Emails based on voice command. Here You need to add the emails of receiver along with their names.

Chat Data Button: The assistant can work on custom data, Here you can Feed your custom data.

Email Credentials Button: The assistant can send emails but you need to provide your email credentials here, 

## Note:[ In the password section you dont have to enter your google account password instead you need to generate a new password(APP password) in 2 step verification in google account]

## Features

- Open any application of system.
- Search anything on Google.
- Answer queries related to any field. 
- Solve any type of logical and mathematical question.
- Remember names and details of people.
- Fetch latest weather report of a particular area.
- Able to speak time & date.
.
.
. and many more 


## Working
- This project converts a user’s query from speech to text using the Speech_Recognition module. 
- Then, it translates the text into English using the Google Translate module. 
- Next, the query is send to  OpenAI AI for response. 
- Finally, it converts the model’s response from text to speech using the Pyttsx3 module.
- It performs task i.e Open an App. using os module.
- It gets real-time weather data from google by using BeautifulSoup library.
 
## Installation:

Clone the repo to make it available on your local system by using 

```bash
  git clone <FORKED_REPO_URL>
```
Change the directory i.e: 

```bash
  cd AI-Desktop-Assistant-Python-OpenAI
```
## Requirements:

Installing all the necessary python module using 

```bash
  pip install -r requirements.txt
```
## Run

 

```bash
  python Marsh.py
```

Sure thing! Just hit the assistant with some voice commands now!


# Contribution:


- We are Open for Pull Requests.
- Please contribute and add value to the code.
- If you have some ideas for new features and you don't have time to implement them please open an issue with the tag new_feature.
- Please don't forget to comment (document) your code!

- Before creating a Pull Request please go through the above guidelines and the code!
