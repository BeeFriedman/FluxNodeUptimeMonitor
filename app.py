from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    wallet = request.args.get('wallet')

    if wallet == None:
        wallet = ''
    else:
        url = 'https://api.runonflux.io/daemon/validateaddress'
        params = {'zelcashaddress' : wallet}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            # API call was successful
            data = response.json()
            valid = data['data']['isvalid']
            app.logger.debug(valid)      
        
    return render_template('index.html', wallet = wallet)