from ..services.openai_service import generate_response

def ask_question(content, question):
    try:
        return generate_response(content, question)
    except Exception as e:
        if "Límite de solicitudes alcanzado" in str(e):
            return {"error": "Has alcanzado el límite de solicitudes. Intenta nuevamente más tarde."}
        else:
            return {"error": f"Error al procesar la solicitud: {str(e)}"}

