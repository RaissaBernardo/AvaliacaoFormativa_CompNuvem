from flask import Flask, request, jsonify
from db import get_connection

app = Flask(__name__)

# cadastrar cliente
@app.route('/clientes', methods=['POST'])
def criar_cliente():
    data = request.json

    conexao = get_connection()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO clientes (nome, telefone, email)
        VALUES (%s, %s, %s)
    """

    valores = (
        data['nome'],
        data.get('telefone'),
        data.get('email')
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

    return jsonify({"msg": "Cliente criado com sucesso"}), 201


# listar clientes
@app.route('/clientes', methods=['GET'])
def listar_clientes():
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    cursor.close()
    conexao.close()

    return jsonify(clientes)


# cadastrar pets
@app.route('/pets', methods=['POST'])
def criar_pet():
    data = request.json

    conexao = get_connection()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO pets (nome, tipo, raca, idade, cliente_id)
        VALUES (%s, %s, %s, %s, %s)
    """

    valores = (
        data['nome'],
        data.get('tipo'),
        data.get('raca'),
        data.get('idade'),
        data['cliente_id']
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

    return jsonify({"msg": "Pet cadastrado com sucesso"}), 201


# listar pets
@app.route('/pets', methods=['GET'])
def listar_pets():
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT * FROM pets")
    pets = cursor.fetchall()

    cursor.close()
    conexao.close()

    return jsonify(pets)


# teste
@app.route('/teste')
def teste():
    return "ok"


if __name__ == '__main__':
    app.run(debug=True)