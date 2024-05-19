import time
from voice import speak
import re

def set_timer(minutes):
    seconds = minutes * 60
    speak(f"Temporizador establecido para {minutes} minutos.")
    time.sleep(seconds)
    speak("El tiempo ha terminado.")

def extract_minutes(query):
    match = re.search(r'temporizador de (\d+) minutos', query)
    if match:
        return int(match.group(1))
    else:
        return None
