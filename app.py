import json
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas Connection
client = MongoClient("mongodb+srv://Admin:Admin%40123@cluster1.jumillq.mongodb.net/?appName=Cluster1")

db = client["studentdb"]
collection = db["students"]

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# API Route
@app.route('/api')
def api():

    try:
        with open('data.json', 'r') as file:
            data = json.load(file)

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)})

# Form Submit Route
@app.route('/submit', methods=['POST'])
def submit():

    try:
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']

        data = {
            "name": name,
            "email": email,
            "course": course
        }

        collection.insert_one(data)

        return render_template('success.html')

    except Exception as e:
        return render_template('index.html', error=str(e))

# Run Flask
if __name__ == '__main__':
    app.run(debug=True,use_reloader=False ,port=8000)        