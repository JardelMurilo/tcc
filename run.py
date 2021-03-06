from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre.html")
def sobre():
    return render_template("sobre.html")

@app.route("/chat.html")
def chat():
    return render_template("chat.html")

@app.route("/IA.html")
def IA():
    return render_template("IA.html")

@app.route("/pesquisadores.html")
def pesquisadores():
    return render_template("pesquisadores.html")

@app.route("/personalizado.html")
def personalizado():
    return render_template("personalizado.html")

@app.route("/perfil.html")
def perfil():
    return render_template("perfil.html")

@app.route("/orientacoes.html")
def orientacoes():
    return render_template("orientacoes.html")

@app.route("/login.html")
def login():
    return render_template("login.html")

@app.route("/cadastro.html")
def cadastro():
    return render_template("cadastro.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
