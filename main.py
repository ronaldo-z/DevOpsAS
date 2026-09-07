from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "E aí, DevOps da PUCPR! Vamos conhecer um pouco do micro-framework flask?"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)