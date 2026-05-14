from flask import Flask, render_template
from flask_cors import CORS
from routes.chatbot import chatbot_bp
from routes.summarizer import summarizer_bp
from routes.leaderboard import leaderboard_bp
from routes.parental import parental_bp
from routes.users import users_bp

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(chatbot_bp)
app.register_blueprint(summarizer_bp)
app.register_blueprint(leaderboard_bp)
app.register_blueprint(parental_bp)
app.register_blueprint(users_bp)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/parent')
def parent_page():
    return render_template('parent.html')

if __name__ == '__main__':
    app.run(debug=True)