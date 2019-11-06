from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = "Hello World"
    # To run Flask i "debugger mode": $ export FLASK_DEBUG=1
    #return f'Hello, {greeting}!'
    return render_template('index.html', greeting=greeting)

if __name__ == "__main__":
    app.run()
    # debug mode: 
    #app.run(debug=True)

