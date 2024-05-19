import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')

for voice in voices:
    print(f"ID: {voice.id}\nName: {voice.name}\n")
