'''
app.py
practice on flask
'''

from flask import Flask

app = Flask(__name__)
@app.route("/")

def run() :
    return "hello world"