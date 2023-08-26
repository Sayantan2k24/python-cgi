print("Welcome to my tools")
print("Enter your requirements: ")
#ch = input()
import webbrowser
import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print('Start speaking...')
    # Listen for audio input
    audio = r.listen(source)
    print('Speech input done.')

# Recognize the audio using Google's speech recognition
ch = r.recognize_google(audio)

if ("date" in ch) and (("run" in ch) or ("execute" in ch)):
  webbrowser.open("http://192.168.0.107/cgi-bin/f.py?c=date")
elif "calender" in ch:
  webbrowser.open("http://192.168.0.107/cgi-bin/f.py?c=cal")
else:
  print("I don't know")
