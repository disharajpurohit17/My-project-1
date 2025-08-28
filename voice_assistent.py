import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

# Initialize engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        listener.pause_threshold = 1
        audio = listener.listen(source)

    try:
        print("✅ Recognizing...")
        command = listener.recognize_google(audio, language='en-in')
        print(f"You said: {command}\n")
    except:
        print("❌ Could not understand. Please say again...")
        return "None"
    return command.lower()

def run_assistant():
    command = take_command()

    if "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The time is {time}")

    elif "date" in command:
        date = datetime.datetime.now().strftime('%d %B %Y')
        speak(f"Today's date is {date}")

    elif "who is" in command or "what is" in command:
        person = command.replace("who is", "").replace("what is", "")
        info = wikipedia.summary(person, sentences=2)
        speak(info)

    elif "play" in command:
        song = command.replace("play", "")
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif "search" in command:
        query = command.replace("search", "")
        speak(f"Searching {query} on Google")
        pywhatkit.search(query)

    elif "exit" in command or "stop" in command:
        speak("Goodbye! Have a great day.")
        exit()

    else:
        speak("Sorry, I didn't understand. Please say again.")

if Lokir == "main":
    speak("Hello! I am your voice assistant. How can I help you?")
    while True:
        run_assistant()
