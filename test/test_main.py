from src.main import app

# Teste 1: Página inicial carrega com status 200 e traz o formulário
def test_index_carrega_formulario():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Qual" in response.data

# Teste 2: Redirecionamento correto ao escolher um time
def test_redirecionamento_time():
    client = app.test_client()
    response = client.post('/escolher', data={'time': 'coritiba'})
    assert response.status_code == 302
    assert '/time/coritiba' in response.headers['Location']

# Teste 3: Página do Athletico renderiza comstatus 200
def test_pagina_time_athletico():
    client = app.test_client()
    response = client.get('/time/athletico')
    assert response.status_code == 200
    assert b"Athletico" in response.data

# Teste 4: Página do Coritiba renderiza com status 200
def test_pagina_time_coritiba():
    client = app.test_client()
    response = client.get('/time/coritiba')
    assert response.status_code == 200
    assert b"Coritiba" in response.data

# Teste 5: Rota inexistente retorna código 404
def test_rota_inexistente():
    client = app.test_client()
    response = client.get('/rota-inexistente')
    assert response.status_code == 404