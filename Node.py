import sys
import requests, json

class Node:
    def __init__(self, tier, ip, rank):
        self.ip = ip
        self.tier = tier
        self.rank = rank

    def get_benchmark_results(self):
        if self.ip.find(':') == -1:
            self.ip = self.ip + ':16127'        
        url = 'http://{0}/daemon/getbenchmarks'.format(self.ip)
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError('Node status API call failed!')
        data = response.json()
        inner_data = json.loads(data['data'])
        return inner_data['status']
    
    def set_status(self, status):
        self.status = status

    def get_values(self):
        return {'tier' : self.tier, 'ip' : self.ip, 'rank' : self.rank, 'status' : self.status}


    def get_status(self):
        return self.status          
    