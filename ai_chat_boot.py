# Rule Based Ai Python ChatBot

import datetime
import time

name = input("Swagat Hai, Enter Your Name : ")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good Morning ",name)
elif 11 <= presentHour <= 17:
    print("Good Afternoon",name)
elif 17 <= presentHour <= 20:
    print("Good Evening",name)
else:
    print("Good Night",name)

print("Welcome To Rule Based ChatBot")
print("You Can Ask Me Basic Question, Type 'Bye' To Exit From The Bot")

#ChatBot Memory Creation [Dictionary of responses]

responses = {
    "hello": "Hi,Welcome. How Can I Help You?",
    "how are you": "I Am Very Fine. Thank You",
    "who are you": "I Am Smart Ai ChatBot",
    "motivate me": "Keep Going. Every Bug Of Your Project Makes You A Better Developer",
    "happy": "Great To Hear That",
    "what a funaction": "Funactions Is A Part Of Python"
}

#method/function to get response of chatbot

def getResponseOfBot(userquestion):
    userquestion = userquestion.lower()
    for eachKey in responses:
        if eachKey in userquestion:
            return responses[eachKey]

    return "I Am Not Able To Tell That Yet. I Am Still In Learning Mode"

#take user input

while True:
    userInput = input("Please Ask Your Question:")
    reply = getResponseOfBot(userInput)
    print("Bot Response:",reply)

    if "Bye" in userInput.lower():
        break
    
