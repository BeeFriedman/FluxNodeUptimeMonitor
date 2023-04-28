import json
import requests

class Node:
    def __init__(self, tier, ip, rank):
        self.ip = ip
        self.tier = tier
        self.rank = rank
        self.status = None

    #makes an api call to get the status of the node returns the status.
    def get_benchmark_results(self):
        if ':' not in self.ip:
            self.ip += ':16127'
        
        url = f'http://{self.ip}/daemon/getbenchmarks'
        response = requests.get(url)
        response.raise_for_status()

        data = json.loads(response.json()['data'])
        return data['status']

    def set_status(self, status):
        self.status = status

    def to_dict(self):
        return {
            'tier': self.tier,
            'ip': self.ip,
            'rank': self.rank,
            'status': self.status
        }
    
    