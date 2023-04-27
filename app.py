from flask import Flask, render_template, request
from Wallet import Wallet
from Node import Node

app = Flask(__name__)

@app.route("/")
def index():
    wallet_address = request.args.get('wallet', '')
    pop_up = False
    node_output = [{'tier': '', 'ip': 'No nodes are running on this wallet address', 'rank': ''}]

    if wallet_address:
        wallet = Wallet(wallet_address)
        if not wallet.is_valid():
            pop_up = True
        else:
            node_output = []
            node_list = []
            for node in wallet.get_node_list():
                node_list.append(Node(node['tier'], node['ip'], node['rank']))

            for node in node_list:
                status = node.get_benchmark_results()
                if status == 'failed':
                    status = '/static/cancel-icon.svg'
                else:
                    status = '/static/green-checkmark-line-icon.svg'    
                node.set_status(status);  
                node_output.append(node.get_values())
        app.logger.debug(node_output)
    return render_template('index.html', wallet=wallet_address, pop_up=pop_up, node_output=node_output)