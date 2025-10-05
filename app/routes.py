from flask import render_template, request, redirect, url_for
from app import app

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/submit", methods="POST")
def submit():
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")


