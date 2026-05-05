import os
from flask import Flask, render_template, request, redirect, session, url_for
from usuarios import USUARIOS

app = Flask(__name__)
app.secret_key = "chave_secreta_sapleno_2024"

PAINEIS = {
    "estoque": "https://app.powerbi.com/view?r=eyJrIjoiZWViYjI2NDMtNTZiZS00YmZmLWEyN2ItY2E0MjNlZWFmZjM1IiwidCI6ImRjY2U5ZTY1LWFjMGEtNDA2OS04ZWRhLTczNTQyZGYzMjNlZSJ9",
    "financeiro": "https://claude.ai/public/artifacts/ef20d868-70a7-4e8d-a0b2-102234f827f9",
    "compras": None,
}

@app.route("/", methods=["GET", "POST"])
def login():
    erro = None
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        painel = request.form["painel"]
        if usuario in USUARIOS and USUARIOS[usuario]["senha"] == senha:
            if painel in USUARIOS[usuario]["paineis"]:
                session["logado"] = True
                session["usuario"] = usuario
                session["painel"] = painel
                return redirect(url_for("dashboard"))
            else:
                erro = "Você não tem acesso a este painel."
        else:
            erro = "Usuário ou senha incorretos."
    return render_template("login.html", erro=erro)

@app.route("/dashboard")
def dashboard():
    if not session.get("logado"):
        return redirect(url_for("login"))
    painel = session.get("painel")
    url = PAINEIS.get(painel)
    return render_template("dashboard.html", url=url, painel=painel)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))
