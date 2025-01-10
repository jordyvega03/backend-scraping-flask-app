from flask import Blueprint, request, jsonify
from .controllers.scraping_controller import scrape_content
from .controllers.openai_controller import ask_question

api_routes = Blueprint("api", __name__)

@api_routes.route("/scrape", methods=["POST"])
def scrape():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL es requerida"}), 400

    try:
        content = scrape_content(url)
        return jsonify({"success": True, "content": content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_routes.route("/ask", methods=["POST"])
def ask():
    """
    Maneja las solicitudes para generar una respuesta basada en el contenido y la pregunta.
    """
    data = request.get_json()
    content = data.get("content")
    question = data.get("question")

    if not content or not question:
        return jsonify({"error": "El contenido y la pregunta son requeridos"}), 400

    try:
        response = ask_question(content, question)
        return jsonify({"success": True, "response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
