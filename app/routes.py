from flask import render_template, request
from datetime import datetime
from app import app

contact_info = {
    'customer_care': {
        'name': 'Maria Ivanova',
        'position': 'Account Manager',
        'email': 'care@company.com',
        'phone': '+7 (495) 123-45-67'
    },
    'address': {
        'street': '25 Tverskaya Street',
        'city': 'Moscow',
        'postal_code': '125009',
        'country': 'Russia'
    }
}

@app.route("/")
def home():
    current_time = datetime.now()
    return render_template("index.html", current_time=current_time)

@app.route("/about")
def about():
    team_members = [
        {'name': 'Alice', 'role': 'Developer'},
        {'name': 'Bob', 'role': 'Designer'},
        {'name': 'Charlie', 'role': 'Project Manager'}
    ]
    return render_template("about.html", team_members=team_members)

@app.route("/contact")
def contact():
    return render_template("contact.html", contact_info=contact_info)

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    return render_template("contact.html", submitted=True, contact_info=contact_info)
