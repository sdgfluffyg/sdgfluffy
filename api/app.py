from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

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


criar_tabela()


@app.route("/")
def home():
    return "API SDG FLUFFY ONLINE"


@app.route("/status")
def status():
    return jsonify({
        "project": "SDG FLUFFY",
        "status": "online",
        "version": "1.0"
    })


@app.route("/fabricantes", methods=["GET"])
def fabricantes():
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome, cnpj, email
        FROM fabricantes
    """)

    dados = cursor.fetchall()
    conn.close()

    resultado = [
        {
            "id": item[0],
            "nome": item[1],
            "cnpj": item[2],
            "email": item[3]
        }
        for item in dados
    ]

    return jsonify(resultado)
@app.route("/fabricantes", methods=["POST"])
def adicionar_fabricante():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400

    nome = dados.get("nome")
    cnpj = dados.get("cnpj")
    email = dados.get("email")

    if not nome:
        return jsonify({"erro": "Campo nome é obrigatório"}), 400

    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO fabricantes (nome, cnpj, email) VALUES (?, ?, ?)",
        (nome, cnpj, email)
    )

    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()

    return jsonify({
        "mensagem": "Fabricante cadastrado com sucesso",
        "id": novo_id,
        "nome": nome,
        "cnpj": cnpj,
        "email": email
    }), 201

if __name__ == "__main__":
    app.run()
