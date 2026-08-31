from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Aplicação funcionando!'

@app.route("/status")
def home():
    imprimir("Olá, mundo!")
    return "Olá Mundo"


if __name__ == '__main__':
    print('Iniciando servidor...')
    app.run(host='127.0.0.1', port=5000, debug=True)