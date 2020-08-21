# START OF CODE
# Written by Aryan Sahel and Ethan Clarke:) last updated August 20, 2020.
# Virtual Assistant.py ©

# This is the code for a simple chatbot/virtual assistant. It is currently capable of:
# 1. Responding to courtesies.
# 2. Displaying the date and time.
# 3. Performing searches on wikipedia

# THINGS TO ADD:
# 1. Ability to send texts
# 2. Ability to dial a number
# 3. Ability to set a timer/alarm

# Wikipedia: https://pypi.org/project/wikipedia/#files
# Speech Recognition: https://pypi.org/project/SpeechRecognition/#files
# Text to Speech: https://pypi.org/project/pyttsx3/#description




# This class helps to obtain the current date.
from datetime import date, datetime

# This carries out searches on wikipedia when prompted by the user.
import wikipedia

# This converts text to speech.
import pyttsx3

# Defining a variable and assigning it today's date.
current_date = date.today()

# This assignment will give us the date in the format of "January 12, 2019"
date = current_date.strftime("%B %d, %Y")
print("\nThe date today is", date, ".")

# Same as for date, only this time it is gonna give us the time.
# Logic same as for obtaining date.
current_time = datetime.now()
time = current_time.strftime("%H:%M:%S")
print("The current time is", time, ".")
print("\nVirtual Assistant is running...")




# A dictionary contain common greetings as keys and their responses as values.
common_greetings = dict(hello="Hello, My name is BlueBelle and I am your virtual assistant.",
                        origin="I was hidden in the crypts of the human brain until Linwood Computers Inc. brought me to life.",
                        health="I am doing very well, how about yourself?")

# Function to convert text to speech.
def speak_text(text):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to make the bot speak and write
def response(input):
    # The SpeakText function makes the computer say the results out loud.
    # It is from the pyttsx3 class.
    # It has been used all throughout the code to make the interactions possible.
    if input in common_greetings:
        print(common_greetings.get(input))
        speak_text(common_greetings.get(input))
    else:
        print(input)
        speak_text(input)

def wiki_search():
    response("What would you like me to search for you today?")

    # A new variable was required for the computer to wait for another response from the user.
    search = input("Search: ")
    search.lower()

    # Variable to hold the wikipedia result in. wikipedia.summary is an in-built function.
    # Allows wiki searches to display 4 sentences
    sentences = 4
    result = wikipedia.summary(search, sentences)
    response(result)




# Loop infinitely for user to speak
while 1:

    # Exception handling to handle
    # exceptions at the runtime
    try:
        MyText = input("\nSay something: ")
        MyText.lower()
        if MyText == "hello" or MyText == "hi" or MyText == "hey":
            response("hello")

        elif MyText == "how are you" or MyText == "how's it going":
            response("health")

        elif MyText == "where are you from":
            response("origin")

        elif MyText == "i want to search for something":
            wiki_search()

        else:
            response("Sorry I don't understand.")
    except:
        print("Goodbye.")
        speak_text("Goodbye.")

# END OF CODE.