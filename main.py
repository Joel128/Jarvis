from voice import speak, takeCommand
from weather import get_weather
from timer import set_timer, extract_minutes
from ml_model import train_model, retrain_model, classify_query, collect_data
import webbrowser
import datetime
import subprocess
from jokes import get_jokes

if __name__ == "__main__":
    speak("¿Qué quieres?")
    train_model()
    while True:
        query = takeCommand().lower()
        if query != "none":
            collect_data(query)  # Recolectar datos para mejorar
            label = classify_query(query)
            if label == "open_youtube":
                webbrowser.open("https://youtube.com")
            elif label == "open_vs":
                print(query)
                proyecto = query.split(" ")[-1]
                ruta = f"/home/joel/proyects/{proyecto}"
                print(ruta)
                try:
                    subprocess.Popen(
                        ["code", "--remote", "wsl+Ubuntu", ruta], shell=True
                    )
                except FileNotFoundError:
                    speak("No he podido encontrar el editor de código.")
            elif label == "weather_query":
                get_weather()
            elif label == "news_query":
                print("No hay noticias en Badalona")
                
            elif label == "greeting":
                speak("Hola, ¿cómo puedo ayudarte?")
            elif label == "time_query":
                speak(datetime.datetime.now().strftime("%H:%M"))
            elif "temporizador de" in query:
                minutes = extract_minutes(query)
                if minutes is not None:
                    set_timer(minutes)
                else:
                    speak("No he entendido la duración del temporizador.")
            elif "buscar" in query:
                query = query.replace("buscar", "")
                webbrowser.open("https://google.com/search?q=" + query)
            elif label == "tell_joke":
                get_jokes()
            elif "duerme" in query:
                speak("¿Pa eso me despiertas?")
                exit()
