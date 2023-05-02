import json
import requests

class Node:
    def __init__(self, tier, ip, rank):
        self.tier = tier
        self.rank = rank
        self.status = None
        if ':' not in ip:
            self.ip = ip +':16127'
        else:
            self.ip = ip
        self.href = 'http://' + self.ip[:-1] + '6'

    #makes an api call to get the status of the node returns the status.
    def get_benchmark_results(self):
        url = f'http://{self.ip}/daemon/getbenchmarks'
        try:
            response = requests.get(url)
            data = json.loads(response.json()['data'])
            return data['status']
        except:
            return 'N/A'

    def set_status(self, status):
        self.status = status

    def to_dict(self):
        return {
            'tier': self.tier,
            'ip': self.ip,
            'rank': self.rank,
            'status': self.status,
            'href': self.href
        }
    
    