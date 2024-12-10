
from flask import Flask, render_template, request, jsonify, redirect, url_for
import openai
import os

from flask.cli import load_dotenv



load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

tasks = []
messages = []

conversation_history = [{"role": "system", "content": "Ai BOT"}]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            tasks.append(task)
        return redirect(url_for('index'))
    return render_template('chat.html', tasks=tasks)

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    messages.append(message)
    return jsonify({"message": message})

@app.route('/chat', methods=['POST'])
def chat():
    user_message = user_message = request.form['message']
    conversation_history.append({"role": "user", "content": user_message})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
        max_tokens=100,
        temperature=0.7
    )

    ai_reply = response['choices'][0]['message']['content']
    conversation_history.append({"role": "assistant", "content": ai_reply})

    return jsonify({"response": ai_reply})

if __name__ == '__main__':
    app.run(debug=True)