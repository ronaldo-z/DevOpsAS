from main import app

def test_index_carrega_formulario():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Qual" in response.data

def test_redirecionamento_time():
    response = app.test_client().post('/escolher', data={'time': 'coritiba'})
    assert response.status_code == 302
    assert '/time/coritiba' in response.headers['Location']

def test_pagina_time_valido():
    response = app.test_client().get('/time/athletico')
    assert response.status_code == 200
    assert b"Athletico" in response.data