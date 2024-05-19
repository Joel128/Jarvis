import requests

request = requests.get("https://www.eldiario.es/temas/barcelona/")
                
texto = request.text

texto.match("<a href=")

