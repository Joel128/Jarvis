import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voice_id = "Microsoft Helena Desktop - Spanish (Spain)"
engine.setProperty("voice", voice_id)
engine.setProperty("rate", 140)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Reconociendo tu voz")
        query = r.recognize_google(audio, language="es-es")
        print(query)
    except Exception as e:
        print(e)
        speak("No te he entendido, quitate lade la boca y hablame otra vez")
        return "None"
    return query
