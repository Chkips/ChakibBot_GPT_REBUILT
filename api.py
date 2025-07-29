from flask import Flask, render_template, request
from agent_gpt import Agent

app = Flask(__name__)
agent = Agent()

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        user = request.form.get("username")
        message = request.form.get("message")
        response = agent.respond(message)
    return render_template("index.html", response=response)
