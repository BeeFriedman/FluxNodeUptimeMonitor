from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    wallet = request.args.get('wallet')

    if wallet == None:
        wallet = ''
        
    return render_template('index.html', wallet = wallet)