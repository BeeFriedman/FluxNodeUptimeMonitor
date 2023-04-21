import requests

class Wallet:
    FLUX_API_URL = 'https://api.runonflux.io/daemon/'
    VALIDATE_ADDRESS_ENDPOINT = 'validateaddress'
    LIST_ZELNODES_ENDPOINT = 'listzelnodes'

    def __init__(self, address):
        self.address = address

    def is_valid(self):
        params = {'zelcashaddress': self.address}
        response = requests.get(Wallet.FLUX_API_URL + Wallet.VALIDATE_ADDRESS_ENDPOINT, params=params)
        if response.status_code != 200:
            raise ValueError('Wallet validation API call failed!')
        data = response.json()
        return data['data']['isvalid']

    def get_node_list(self):
        params = {'filter': self.address}
        response = requests.get(Wallet.FLUX_API_URL + Wallet.LIST_ZELNODES_ENDPOINT, params=params)
        if response.status_code != 200:
            raise ValueError('Get nodes API call failed!')
        data = response.json()
        return data['data']