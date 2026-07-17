from flask import Flask, jsonify

app = Flask(__name__)

import sqlite3

DB_NAME = "sdg_fluffy.db"

@app.route("/")
def home():
    return "API SDG FLUFFY ONLINE"

@app.route("/status")
def status():
    return {
        "project": "SDG FLUFFY",
        "status": "online",
        "version": "1.0"
    }

if __name__ == "__main__":
    app.run(debug=True)
