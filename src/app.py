from flask import Flask, render_template
import os

#Allows to make the reference into the templates folder
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'))

@app.route('/')
def form():
    return render_template("index.html")
    #return "Prueba"

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)