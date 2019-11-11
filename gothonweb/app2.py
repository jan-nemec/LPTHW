from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = "Hello World"
    # To run Flask i "debugger mode": $ export FLASK_DEBUG=1
    #return f'Hello, {greeting}!'
    return render_template('index.html', greeting=greeting)

"""
@app.route('/hello')
def index():
    name = request.args.get('name', 'Nobody') 
    greet = request.args.get('greet', 'Hola')
    # request.args to get data from the browser. This is simple dict that
    # contains the form values as a key=value pairs.

    if name:
        greeting = f"{greet}, {name}"
    else:
        greeting = "Hello World"

    return render_template("index.html", greeting=greeting)
"""

@app.route('/hello', methods=['POST', 'GET'])
def index():
    greeting = "Hello World"

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)
    else:
        return render_template("hello_form.html")


if __name__ == "__main__":
    app.run()
    # debug mode: 
    #app.run(debug=True)