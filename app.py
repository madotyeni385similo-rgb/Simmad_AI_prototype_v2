from flask import Flask, render_template_string, request, jsonify
import openai
import os

app = Flask(__name__)

# Load OpenAI API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return render_template_string("""
        <h1>Welcome to Simmad AI Prototype 🚀</h1>
        <p>Your app is running successfully on Render!</p>
        <textarea id="userInput" placeholder="Type your message here..." rows="3" cols="40"></textarea><br>
        <button onclick="sendMessage()">Send</button>
        <p><strong>AI:</strong> <span id="response"></span></p>

        <script>
        async function sendMessage() {
            const userText = document.getElementById('userInput').value;
            const response = await fetch('/ask', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: userText })
            });
            const data = await response.json();
            document.getElementById('response').textContent = data.reply;
        }
        </script>
    """)

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get("message", "")
    
    if not user_message:
        return jsonify({"reply": "Please enter a message."})

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        ai_reply = completion.choices[0].message["content"]
        return jsonify({"reply": ai_reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
