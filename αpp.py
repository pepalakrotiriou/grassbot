# Save this as app.py in your GitHub
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# This will control the pump (Relay Module) 
PUMP_PIN = 17 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def command():
    action = request.json.get('action')
    print(f"Robot executing: {action}")
    # When hardware arrives, add GPIO commands here
    return jsonify(status="success", message=f"Executed {action}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
