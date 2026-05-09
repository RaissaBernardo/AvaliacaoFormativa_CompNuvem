from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector
import os
import time

app = Flask(__name__)

DB_HOST     = os.getenv("DB_HOST",     "mysql-service")
DB_NAME     = os.getenv("DB_NAME",     "petlove")
DB_USER     = os.getenv("DB_USER",     "aluno")
DB_PASSWORD = os.getenv("DB_PASSWORD", "senha123")


# ──────────────────────────────────────────────
# Conexão
# ──────────────────────────────────────────────

def conectar_bd():
    tentativas = 10
    while tentativas > 0:
        try:
            conexao = mysql.connector.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
            return conexao
        except mysql.connector.Error:
            tentativas -= 1
            time.sleep(1)
    return None


# ──────────────────────────────────────────────
# Página principal
# ──────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


# ──────────────────────────────────────────────
# Clientes
# ──────────────────────────────────────────────

@app.route("/clientes", methods=["GET", "POST"])
def clientes():
    conexao = conectar_bd()
    erro = None

    if request.method == "POST":
        nome     = request.form.get("nome", "").strip()
        telefone = request.form.get("telefone", "").strip()
        email    = request.form.get("email", "").strip()

        if not nome:
            erro = "O campo Nome é obrigatório."
        elif conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO clientes (nome, telefone, email) VALUES (%s, %s, %s)",
                (nome, telefone, email)
            )
            conexao.commit()
            cursor.close()
            conexao.close()
            return redirect(url_for("clientes"))

    lista = []
    if conexao:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT id, nome, telefone, email FROM clientes ORDER BY id")
        lista = cursor.fetchall()
        cursor.close()
        conexao.close()

    return jsonify(lista) if request.headers.get("X-Requested-With") == "fetch" \
        else render_template("index.html", clientes=lista, erro=erro)


# ──────────────────────────────────────────────
# Pets
# ──────────────────────────────────────────────

@app.route("/pets", methods=["GET", "POST"])
def pets():
    conexao = conectar_bd()
    erro = None

    if request.method == "POST":
        nome       = request.form.get("nome", "").strip()
        tipo       = request.form.get("tipo", "").strip()
        raca       = request.form.get("raca", "").strip()   # sem cedilha — bate com o form
        idade      = request.form.get("idade", "").strip()
        cliente_id = request.form.get("cliente_id", "").strip()

        if not nome:
            erro = "O campo Nome do pet é obrigatório."
        elif conexao:
            cursor = conexao.cursor()
            cursor.execute(
                """INSERT INTO pets (nome_pet, tipo, raca, idade, cliente_responsavel)
                   VALUES (%s, %s, %s, %s, %s)""",
                (nome, tipo, raca, idade or None, cliente_id or None)
            )
            conexao.commit()
            cursor.close()
            conexao.close()
            return redirect(url_for("pets"))

    lista = []
    clientes_lista = []
    if conexao:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(
            """SELECT p.id, p.nome_pet AS nome, p.tipo, p.raca, p.idade,
                      c.nome AS dono
               FROM pets p
               LEFT JOIN clientes c ON c.id = p.cliente_responsavel
               ORDER BY p.id"""
        )
        lista = cursor.fetchall()

        cursor.execute("SELECT id, nome FROM clientes ORDER BY nome")
        clientes_lista = cursor.fetchall()

        cursor.close()
        conexao.close()

    return render_template("index.html", pets=lista, clientes=clientes_lista, erro=erro)


# ──────────────────────────────────────────────
# Serviços  →  tabela atendimentos
# ──────────────────────────────────────────────

@app.route("/servicos", methods=["GET", "POST"])
def servicos():
    conexao = conectar_bd()
    erro = None

    if request.method == "POST":
        pet_id       = request.form.get("pet_id", "").strip()
        tipo_servico = request.form.get("tipo", "").strip()
        data         = request.form.get("data", "").strip()
        valor        = request.form.get("valor", "").strip()

        if not pet_id or not tipo_servico:
            erro = "Pet e tipo de serviço são obrigatórios."
        elif conexao:
            cursor = conexao.cursor()
            cursor.execute(
                """INSERT INTO atendimentos (pet_id, tipo_servico, data_atendimento, valor)
                   VALUES (%s, %s, %s, %s)""",
                (pet_id, tipo_servico, data or None, valor or None)
            )
            conexao.commit()
            cursor.close()
            conexao.close()
            return redirect(url_for("servicos"))

    lista = []
    pets_lista = []
    if conexao:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(
            """SELECT a.id, p.nome_pet AS pet_atendido, a.tipo_servico AS tipo,
                      a.data_atendimento AS data, a.valor
               FROM atendimentos a
               JOIN pets p ON p.id = a.pet_id
               ORDER BY a.id"""
        )
        lista = cursor.fetchall()

        cursor.execute("SELECT id, nome_pet AS nome FROM pets ORDER BY nome_pet")
        pets_lista = cursor.fetchall()

        cursor.close()
        conexao.close()

    return render_template("index.html", servicos=lista, pets=pets_lista, erro=erro)


# ──────────────────────────────────────────────
# Fornecedores  →  tabela não existe no init.sql,
#                  criamos na primeira requisição
# ──────────────────────────────────────────────

def garantir_tabela_fornecedores(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fornecedores (
            id       INT PRIMARY KEY AUTO_INCREMENT,
            nome     VARCHAR(100) NOT NULL,
            telefone VARCHAR(20),
            produto  VARCHAR(100)
        )
    """)


@app.route("/fornecedores", methods=["GET", "POST"])
def fornecedores():
    conexao = conectar_bd()
    erro = None

    if conexao:
        cursor = conexao.cursor(dictionary=True)
        garantir_tabela_fornecedores(cursor)
        conexao.commit()

        if request.method == "POST":
            nome     = request.form.get("nome", "").strip()
            telefone = request.form.get("telefone", "").strip()
            produto  = request.form.get("produto", "").strip()

            if not nome:
                erro = "O campo Nome é obrigatório."
            else:
                cursor.execute(
                    "INSERT INTO fornecedores (nome, telefone, produto) VALUES (%s, %s, %s)",
                    (nome, telefone, produto)
                )
                conexao.commit()
                cursor.close()
                conexao.close()
                return redirect(url_for("fornecedores"))

        cursor.execute("SELECT id, nome, telefone, produto FROM fornecedores ORDER BY id")
        lista = cursor.fetchall()
        cursor.close()
        conexao.close()
    else:
        lista = []

    return render_template("index.html", fornecedores=lista, erro=erro)


# ──────────────────────────────────────────────
# Vendas  →  tabela não existe no init.sql,
#            criamos na primeira requisição
# ──────────────────────────────────────────────

def garantir_tabela_vendas(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            id         INT PRIMARY KEY AUTO_INCREMENT,
            cliente    VARCHAR(100) NOT NULL,
            produto    VARCHAR(100),
            valor      DECIMAL(10,2),
            data_venda DATE
        )
    """)


@app.route("/vendas", methods=["GET", "POST"])
def vendas():
    conexao = conectar_bd()
    erro = None

    if conexao:
        cursor = conexao.cursor(dictionary=True)
        garantir_tabela_vendas(cursor)
        conexao.commit()

        if request.method == "POST":
            cliente = request.form.get("cliente", "").strip()
            produto = request.form.get("produto", "").strip()
            valor   = request.form.get("valor", "").strip()

            if not cliente:
                erro = "O campo Cliente é obrigatório."
            else:
                cursor.execute(
                    """INSERT INTO vendas (cliente, produto, valor, data_venda)
                       VALUES (%s, %s, %s, CURDATE())""",
                    (cliente, produto, valor or None)
                )
                conexao.commit()
                cursor.close()
                conexao.close()
                return redirect(url_for("vendas"))

        cursor.execute(
            "SELECT id, cliente, produto, data_venda AS data, valor FROM vendas ORDER BY id"
        )
        lista = cursor.fetchall()
        cursor.close()
        conexao.close()
    else:
        lista = []

    return render_template("index.html", vendas=lista, erro=erro)


# ──────────────────────────────────────────────
# Inicialização
# ──────────────────────────────────────────────

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)