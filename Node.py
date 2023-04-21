import requests, json

class Node:
    def __init__(self, ip):
        self.ip = ip

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