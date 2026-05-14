from flask import Blueprint, request, jsonify
import google.generativeai as genai
from config import GEMINI_API_KEY

chatbot_bp = Blueprint('chatbot', __name__)

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
# Updated to Gemini 2.5 Flash for better performance in 2026
model = genai.GenerativeModel('gemini-2.5-flash') 

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message')
    
    if not message:
        return jsonify({'error': 'Message required'}), 400

    try:
        # Use system_instruction in the constructor for cleaner logic
        tutor_model = genai.GenerativeModel(
            model_name='gemini-2.5-flash',
            system_instruction="You are a helpful AI tutor for students."
        )
        
        response = tutor_model.generate_content(message)
        reply = response.text

        return jsonify({'reply': reply})

    except Exception as e:
        return jsonify({'reply': str(e)})
