# **Backend Scraping Flask App**

Este proyecto es una aplicación de backend desarrollada con Flask que permite analizar páginas web mediante scraping y realizar preguntas sobre su contenido utilizando la API de OpenAI.

## **Características**
- **Scraping de páginas web**: Extrae contenido textual de cualquier URL válida.
- **Procesamiento con OpenAI**: Responde preguntas basadas en el contenido extraído.
- **Modularidad**: Código organizado con controladores, servicios y rutas.
- **API RESTful**: Interfaz para interactuar con las funcionalidades mediante solicitudes HTTP.

---

## **Requisitos Previos**

1. Python 3.9 o superior
2. Clave de API de OpenAI (puedes obtenerla en [OpenAI](https://platform.openai.com/))
3. Entorno virtual de Python configurado

---

## **Instalación**

1. Clona el repositorio:
   ```bash
   git clone https://github.com/jordyvega03/backend-scraping-flask-app.git
   cd backend-scraping-flask-app
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   # o
   .venv\Scripts\activate     # Windows
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno en un archivo `.env`:
   ```plaintext
   OPENAI_API_KEY=tu_clave_openai
   SECRET_KEY=clave_secreta_para_flask
   FLASK_ENV=development
   PORT=4000
   ```

---

## **Uso**

1. Inicia el servidor Flask:
   ```bash
   python run.py
   ```

2. Accede al servidor local:
   ```
   http://127.0.0.1:4000
   ```

---

## **Rutas de la API**

### **1. Scraping de Páginas Web**
- **URL**: `/api/scrape`
- **Método**: `POST`
- **Descripción**: Extrae contenido textual de una página web.
- **Cuerpo de la Solicitud**:
  ```json
  {
    "url": "https://example.com"
  }
  ```
- **Respuesta**:
  ```json
  {
    "success": true,
    "content": "Texto extraído de la página web..."
  }
  ```

### **2. Preguntas Sobre el Contenido**
- **URL**: `/api/ask`
- **Método**: `POST`
- **Descripción**: Responde preguntas basadas en el contenido extraído.
- **Cuerpo de la Solicitud**:
  ```json
  {
    "content": "Texto extraído de la página web...",
    "question": "¿Qué significa este contenido?"
  }
  ```
- **Respuesta**:
  ```json
  {
    "success": true,
    "response": "Respuesta generada por OpenAI..."
  }
  ```

---

## **Estructura del Proyecto**

```
backend-scraping-flask-app/
├── app/
│   ├── __init__.py          # Inicialización de la aplicación Flask
│   ├── routes.py            # Rutas principales
│   ├── controllers/         # Lógica de controladores
│   │   ├── scraping_controller.py
│   │   └── openai_controller.py
│   ├── services/            # Conexión con servicios externos
│   │   └── openai_service.py
│   ├── utils/               # Funciones auxiliares (scraper)
│   │   └── scraper.py
├── .env                     # Variables de entorno (no incluido en el repositorio)
├── .gitignore               # Archivos ignorados por Git
├── config.py                # Configuración de la aplicación
├── requirements.txt         # Dependencias del proyecto
├── run.py                   # Punto de entrada de la aplicación
└── README.md                # Documentación del proyecto
```

---

## **Tecnologías Utilizadas**
- **Backend**: Flask
- **Scraping**: BeautifulSoup, Requests
- **Procesamiento**: OpenAI API
- **Gestión de Entorno**: Python Dotenv

---

## **Pruebas**

1. **Pruebas Manuales**:
   - Utiliza herramientas como Postman o cURL para probar las rutas.

2. **Ejemplo de cURL**:
   ```bash
   curl -X POST http://127.0.0.1:4000/api/scrape \
   -H "Content-Type: application/json" \
   -d '{"url": "https://kubernetes.io/es/"}'
   ```

---

## **Posibles Errores**

### **429: Too Many Requests**
- Causa: Has excedido el límite de solicitudes permitido por la API de OpenAI.
- Solución:
  - Implementa un sistema de retrasos entre solicitudes.
  - Reduce el uso de tokens ajustando `max_tokens`.

### **ModuleNotFoundError: No module named 'flask'**
- Causa: Flask no está instalado en el entorno virtual.
- Solución:
  ```bash
  pip install flask
  ```

---

## **Contribuciones**
¡Las contribuciones son bienvenidas! Si deseas colaborar, por favor sigue los pasos estándar para contribuir a proyectos de código abierto.

1. Haz un fork del repositorio.
2. Crea una rama con tu nueva funcionalidad:
   ```bash
   git checkout -b nueva-funcionalidad
   ```
3. Realiza tus cambios y haz un commit.
4. Envía un pull request.

---

## **Licencia**
Este proyecto está bajo la Licencia MIT. Puedes consultar el archivo `LICENSE` para más detalles.

---

## **Contacto**
Para dudas o sugerencias, por favor contacta a **[tu_email@example.com](mailto:jordyvega15@gmail.com)**.

--- 

¡Listo! Este archivo `README.md` debería documentar claramente tu proyecto y ayudar a otros a entender cómo usarlo o contribuir a él. 😊