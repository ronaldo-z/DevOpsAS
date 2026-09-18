from flask import Flask, render_template, request, redirect, url_for

app: Flask = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/escolher', methods=['POST'])
def escolher():
    time = request.form.get('time')
    return redirect(url_for('pagina_time', nome_time=time))

@app.route('/time/<nome_time>')
def pagina_time(nome_time):
    times_capital = ['coritiba', 'athletico', 'parana']
    if nome_time in times_capital:
        return f"<h1>Bem-vindo, torcedor do {nome_time.capitalize()}!</h1>"
    return "<h1>Time não encontrado na capital!</h1>", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)