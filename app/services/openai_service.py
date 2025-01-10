import requests
import time
from flask import current_app

def generate_response(content, question):
    """
    Genera una respuesta utilizando la API de OpenAI.
    Maneja errores de límite de tarifa con reintentos.
    """
    api_key = current_app.config["OPENAI_API_KEY"]
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    prompt = f"Contenido extraído de la página:\n{content}\n\nPregunta: {question}"
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    retries = 3  # Número de reintentos permitidos
    for attempt in range(retries):
        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"].strip()
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:  # Error de demasiadas solicitudes
                if attempt < retries - 1:
                    time.sleep(5)  # Espera 5 segundos antes de intentar nuevamente
                else:
                    raise Exception("Error en la solicitud a OpenAI: Límite de solicitudes alcanzado")
            else:
                raise Exception(f"Error en la solicitud a OpenAI: {str(e)}")
