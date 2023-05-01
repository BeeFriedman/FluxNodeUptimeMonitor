from flask import Flask, render_template, request
from Wallet import Wallet
from Node import Node
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.route('/')
def index():
    wallet_address = request.args.get('wallet', '')
    pop_up = False
    empty = False
    node_output = []

    #if user searched for a wallet address, verify if it's valid.
    #if not valid set pop_up to true to trigger the invalid wallet popup
    #else check if there are nodes on the wallet.
    #if there is check their status and display it.
    if wallet_address:
        wallet = Wallet(wallet_address)
        if not wallet.is_valid():
            pop_up = True
        else:
            node_list = [Node(n['tier'], n['ip'], n['rank']) for n in wallet.get_node_list()]
            for node in node_list:
                status = node.get_benchmark_results()
                if status == 'failed':
                    status = '/static/cancel-icon.svg'
                else:
                    status = '/static/green-checkmark-line-icon.svg'
                node.set_status(status)
            node_output = [n.to_dict() for n in node_list]
    if not len(node_output):
        empty = True
    return render_template('index.html', wallet=wallet_address, pop_up=pop_up, node_output=node_output, empty=empty)

@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        if(404):
            return render_template('404.html'), 404
        return e
    return render_template('500.html'), 500
