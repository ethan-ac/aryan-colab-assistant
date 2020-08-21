# START OF CODE
# Written by Aryan Sahel last updated August 20, 2020.
# Virtual Assistant.py ©

# This is the code for a simple chatbot/virtual assistant. It is currently capable of:
# 1. Responding to courtesies.
# 2. Displaying the date and time.
# 3. Performing searches on wikipedia

# CURRENT PROBLEMS THAT NEED TO BE FIXED:
# 1. Right now, everytime the user says somethings to the computer, it responds and then the code stops.
# We need to find a way for it to correctly loop through.

# THINGS TO ADD:
# 1. Ability to send texts
# 2. Ability to dial a number
# 3. Ability to set a timer/alarm.

# For ETHAN: feel free to go through the code, let me know if you don't understand something.
# You might have to go through the installation steps for some of the classes I have used.
# You can look it up online on geeksforgeeks or stack overflow.
# Wikipedia: https://pypi.org/project/wikipedia/#files
# Speech Recognition: https://pypi.org/project/SpeechRecognition/#files
# Text to Speech: https://pypi.org/project/pyttsx3/#description




# This class helps to obtain the current date.
from datetime import date, datetime

# This carries out searches on wikipedia when prompted by the user.
import wikipedia

# This allows the human-computer interaction by detecting the microphone and speaker in the machine.
import speech_recognition as sr

# This converts text to speech.
import pyttsx3

# A dictionary contain common greetings as keys and their responses as values.
common_greetings = dict(hello="Hello, My name is BlueBelle and I am your virtual assistant.",
                        origin="I was hidden in the crypts of the human brain until Linwood Computers Inc. brought me to life.",
                        health="I am doing very well, how about yourself?")

# Defining a variable and assigning it today's date.
current_date = date.today()

# This assignment will give us the date in the format of "January 12, 2019"
date = current_date.strftime("%B %d, %Y")
print("\nThe date today is", date + ".")

# Same as for date, only this time it is gonna give us the time.
# Logic same as for obtaining date.
current_time = datetime.now()
time = current_time.strftime("%H:%M:%S")
print("The current time is", time + ".")

# For making it look visually appealing.

print("\nVirtual Assistant is running")

# This variable is MANDATORY for carrying out any wikipedia searches.
# Hard coded to give user lesser freedom to reduce headache.
# This will now display 4 sentences when the wikipedia library is prompted.
sentences = 4

# Function to convert text to speech.
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Loop infinitely for user to speak

while 1:

    # Exception handling to handle
    # exceptions at the runtime
    try:
        MyText = input("say something: ")
        MyText = MyText.lower()
        if MyText == "hello" or MyText == "hi" or MyText == "hey":
            print(common_greetings.get("hello"))

            # The SpeakText function makes the computer say the results out loud.
            # It is from the pyttsx3 class.
            # It has been used all throughout the code to make the interactions possible.
            SpeakText(common_greetings.get("hello"))

        elif MyText == "how are you" or MyText == "how's it going":
            print(common_greetings.get("health"))
            SpeakText(common_greetings.get("health"))

        elif MyText == "where are you from":
            print(common_greetings.get("origin"))
            SpeakText(common_greetings.get("origin"))

        elif MyText == "i want to search for something":
            print("What would you like me to search for you today?")
            SpeakText("What would you like me to search for you today?")

            # A new variable was required for the computer to wait for another response from the user.
            search = input("search: ")

            search.lower()
            print(search)

            # Variable to hold the wikipedia result in. wikipedia.summary is an in-built function.
            result = wikipedia.summary(search, sentences)
            print(result)
            SpeakText(result)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        # SpeakText("Request is unavailable.")

    except sr.UnknownValueError:
        print("I'm not sure I understand.")
        # SpeakText("I'm not sure I understand.")

# END OF CODE.