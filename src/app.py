from flask import Flask, render_template, request, redirect, url_for
from form import UserData
import os

#Allows to make the reference into the templates folder
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'), static_folder=os.path.join(os.path.dirname(__file__), '..', 'static'))
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def index():
    return render_template("index.html")
    #return "Prueba"

@app.route('/form', methods=['GET','POST'])
def form():
    form = UserData()
    return render_template('form.html', form=form)

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)