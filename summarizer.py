from flask import Blueprint, request, jsonify
import google.generativeai as genai
from config import GEMINI_API_KEY

summarizer_bp = Blueprint('summarizer', __name__)

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

@summarizer_bp.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    notes = data.get('notes')

    if not notes:
        return jsonify({'error': 'Notes required'}), 400

    try:
        # Instruction and content for the model
        prompt = f"Summarize the following notes into easy bullet points:\n\n{notes}"
        response = model.generate_content(prompt)
        
        summary = response.text

        return jsonify({'summary': summary})

    except Exception as e:
        return jsonify({'summary': str(e)})
