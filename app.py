from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "A mãe tá on!"

if __name__ == '__main__':
    app.run()