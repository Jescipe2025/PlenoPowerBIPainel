from flask import Flask, render_template, request, redirect, session, url_for
from usuarios import USUARIOS

app = Flask(__name__)
app.secret_key = "chave_secreta_sapleno_2024"

POWERBI_URL = "https://app.powerbi.com/view?r=eyJrIjoiZWViYjI2NDMtNTZiZS00YmZmLWEyN2ItY2E0MjNlZWFmZjM1IiwidCI6ImRjY2U5ZTY1LWFjMGEtNDA2OS04ZWRhLTczNTQyZGYzMjNlZSJ9"

@app.route("/", methods=["GET", "POST"])
def login():
    erro = None
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha   = request.form["senha"]
        if usuario in USUARIOS and USUARIOS[usuario] == senha:
            session["logado"]  = True
            session["usuario"] = usuario
            return redirect(url_for("dashboard"))
        else:
            erro = "Usuário ou senha incorretos."
    return render_template("login.html", erro=erro)

@app.route("/dashboard")
def dashboard():
    if not session.get("logado"):
        return redirect(url_for("login"))
    # Passa a URL para o template — nunca exposta ao usuário
    return render_template("dashboard.html", url=POWERBI_URL)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))