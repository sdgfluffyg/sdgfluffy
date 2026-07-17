from flask import Flask, jsonify

app = Flask(__name__)

import sqlite3

DB_NAME = "sdg_fluffy.db"
def conectar_db():

    return sqlite3.connect(DB_NAME)



def criar_tabela():

    conn = conectar_db()

    cursor = conn.cursor()



    cursor.execute("""

    CREATE TABLE IF NOT EXISTS fabricantes (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        nome TEXT NOT NULL,

        cnpj TEXT,

        email TEXT

    )

    """)



    conn.commit()

    conn.close()
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

@app.route("/fabricantes")

def fabricantes():

    conn = conectar_db()

    cursor = conn.cursor()



    cursor.execute("SELECT * FROM fabricantes")

    dados = cursor.fetchall()



    conn.close()



    return jsonify(dados)
if __name__ == "__main__":
    criar_tabela()
    app.run(debug=True)
