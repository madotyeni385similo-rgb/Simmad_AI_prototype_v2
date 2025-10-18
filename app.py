from flask import Flask, render_template, request, jsonify, send_from_directory
import openai
import os

app = Flask(__name__, static_folder='.', static_url_path='')

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    # Serve the main HTML page
    return send_from_directory('.', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")
        if not user_message:
            return jsonify({"reply": "Please enter a message."})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )

        ai_reply = response.choices[0].message["content"].strip()
        return jsonify({"reply": ai_reply})

    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
