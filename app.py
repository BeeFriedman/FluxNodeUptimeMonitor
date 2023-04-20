from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    wallet = request.args.get('wallet')
    popUp = False
    nodeList = [{'tier': '', 'ip': 'No nodes are running on this wallet address', 'rank': ''}]

    if wallet == None or wallet == '':
        wallet = ''
    else:
        url = 'https://api.runonflux.io/daemon/validateaddress'
        params = {'zelcashaddress' : wallet}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            # API call was successful
            data = response.json()
            valid = data['data']['isvalid']
            if valid == False:
                popUp = True 
            elif valid == True:
                nodeList = getNodeList(wallet)

        for node in nodeList:
            ip = node['ip']

            if ip.find(':') == -1:
                ip = ip + ':16127'
            status = getBenchmarkResults(ip)     
        #app.logger.debug(nodeList)
    return render_template('index.html', wallet = wallet, popUp = popUp, nodeList = nodeList)

def getNodeList(wallet):
    url = 'https://api.runonflux.io/daemon/listzelnodes'
    params = {'filter': wallet}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        # API call was successful
        data = response.json()
        nodeList = data['data']
        return nodeList
    
def getBenchmarkResults(ip):
    url = 'http://{0}/daemon/getbenchmarks'.format(ip)
    response = requests.get(url)
    data = response.json()
    status = json.loads(data['data'])
    app.logger.debug(status['status'])
    return status