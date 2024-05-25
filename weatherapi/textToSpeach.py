#pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
#pip install pyttsx3
import pyttsx3
engine = pyttsx3.init()
# engine.say("I will speak this text")
text = input("what u want to speak : ")
engine.say(text)
engine.runAndWait()