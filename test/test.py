import pytest
from ecommerce import app 

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

#Testes de Usuário
def test_cadastro_valido(client):
    response = client.post("/cadastrar_usuario", data={
        "nome": "Teste",
        "email": "teste@teste.com",
        "senha": "123"
    }, follow_redirects=True)
    assert response.status_code == 200
    assert "Login" in response.get_data(as_text=True) or "login" in response.get_data(as_text=True)

def test_cadastro_sem_senha(client):
    response = client.post("/cadastrar_usuario", data={
        "nome": "Teste",
        "email": "teste2@teste.com",
        "senha": ""
    }, follow_redirects=True)
    assert "Todos os campos" in response.get_data(as_text=True)

def test_login_valido(client):
    client.post("/cadastrar_usuario", data={
        "nome": "LoginTeste",
        "email": "login@teste.com",
        "senha": "123"
    }, follow_redirects=True)
    response = client.post("/autenticar", data={
        "email": "login@teste.com",
        "senha": "123"
    }, follow_redirects=True)
    assert "logado" in response.get_data(as_text=True) or "Loja" in response.get_data(as_text=True)

def test_login_invalido(client):
    response = client.post("/autenticar", data={
        "email": "naoexiste@teste.com",
        "senha": "errada"
    }, follow_redirects=True)
    assert "Email ou senha incorretos" in response.get_data(as_text=True)

#Testes de Carrinho
def test_add_produto_invalido(client):

    client.post("/cadastrar_usuario", data={
        "nome": "TesteCarrinho",
        "email": "teste_carrinho@teste.com",
        "senha": "123"
    }, follow_redirects=True)
    client.post("/autenticar", data={
        "email": "teste_carrinho@teste.com",
        "senha": "123"
    }, follow_redirects=True)


    response = client.post("/add-to-cart/999", data={"quantidade":1})
    assert response.status_code == 302
    assert "/loja" in response.headers["Location"]


def test_finalizar_compra_sem_login(client):
    response = client.post("/finalizar_compra", follow_redirects=True)
    assert "Você precisa estar logado" in response.get_data(as_text=True)

def test_finalizar_compra_carrinho_vazio(client):
    client.post("/cadastrar_usuario", data={
        "nome": "CarrinhoTeste",
        "email": "carrinho@teste.com",
        "senha": "123"
    }, follow_redirects=True)
    client.post("/autenticar", data={
        "email": "carrinho@teste.com",
        "senha": "123"
    }, follow_redirects=True)
    response = client.post("/finalizar_compra", follow_redirects=True)
    assert "Seu carrinho está vazio" in response.get_data(as_text=True)

def test_logout(client):
    # Primeiro cadastra e loga
    client.post("/cadastrar_usuario", data={
        "nome": "LogoutTeste",
        "email": "logout@teste.com",
        "senha": "123"
    }, follow_redirects=True)
    client.post("/autenticar", data={
        "email": "logout@teste.com",
        "senha": "123"
    }, follow_redirects=True)

    # Agora faz logout
    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    assert "Logout realizado com sucesso" in response.get_data(as_text=True)