from flask_app import app
from flask import redirect, render_template, request, session
from ..models.dojo import Dojo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def submit():
    print(f"REQUEST FORM {request.form}")
    if not Dojo.is_valid(request.form):
        return redirect("/")
    data = {
        "name" : request.form["name"],
        "location" : request.form["location"],
        "language" : request.form["language"],
        "comment" : request.form["comment"]
    }
    new_dojo_id = Dojo.save(data)
    print(f" NEW DOJO ID: {new_dojo_id}")
    return redirect(f'/display/{new_dojo_id}',)

@app.route('/display/<int:id>')
def display(id):
    data = {
        "id": id
    }
    return render_template("results.html", dojo = Dojo.get_by_id(data))

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')