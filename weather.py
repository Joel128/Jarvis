import requests
import re
from voice import speak

def get_weather():
    url = "https://wttr.in/Badalona?format=%t"
    response = requests.get(url)
    if response.status_code == 200:
        weather = response.text
        weather = re.sub(r"\n", "", weather)
        speak(f"En Badalona, la temperatura es de {weather}.")
    else:
        speak("No he podido obtener la temperatura.")