from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# API route to check if server is up
@app.route('/api/status', methods=['GET'])
def server_status():
    return jsonify({"message": "Server is up and running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)

