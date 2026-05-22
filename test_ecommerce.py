import sqlite3
import pytest


# ======================================================
# FIXTURE DE PRODUTOS
# ======================================================

@pytest.fixture
def db_produtos():

    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
        )
    """)

    conn.commit()

    yield conn

    conn.close()


# ======================================================
# FIXTURE DE LOGS
# ======================================================

@pytest.fixture(scope='session')
def db_logs():

    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE auditoria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            evento TEXT NOT NULL
        )
    """)

    conn.commit()

    yield conn

    conn.close()


# ======================================================
# TESTE 1
# ======================================================

def test_inserir_produto(db_produtos):

    cursor = db_produtos.cursor()

    cursor.execute(
        "INSERT INTO produtos (nome, preco) VALUES (?, ?)",
        ("Caneca", 29.90)
    )

    db_produtos.commit()

    cursor.execute("SELECT * FROM produtos")

    resultado = cursor.fetchall()

    assert len(resultado) == 1
    assert resultado[0][1] == "Caneca"
    assert resultado[0][2] == 29.90


# ======================================================
# TESTE 2
# ======================================================

def test_banco_produtos_vazio(db_produtos):

    cursor = db_produtos.cursor()

    cursor.execute("SELECT * FROM produtos")

    resultado = cursor.fetchall()

    assert resultado == []


# ======================================================
# TESTE 3
# ======================================================

def test_registrar_log(db_logs):

    cursor = db_logs.cursor()

    cursor.execute(
        "INSERT INTO auditoria (evento) VALUES (?)",
        ("usuario_logado",)
    )

    db_logs.commit()

    cursor.execute("SELECT * FROM auditoria")

    resultado = cursor.fetchall()

    assert len(resultado) >= 1
    assert resultado[0][1] == "usuario_logado"


# ======================================================
# TESTE 4
# ======================================================

def test_logs_compartilhados(db_logs):

    cursor = db_logs.cursor()

    cursor.execute(
        "INSERT INTO auditoria (evento) VALUES (?)",
        ("pagamento_realizado",)
    )

    db_logs.commit()

    cursor.execute("SELECT evento FROM auditoria")

    resultados = cursor.fetchall()

    eventos = [evento[0] for evento in resultados]

    assert "usuario_logado" in eventos
    assert "pagamento_realizado" in eventos