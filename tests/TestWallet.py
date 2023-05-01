import unittest
from Wallet import Wallet

class TestWallet(unittest.TestCase):
    #tests that a valid wallet returns the right true
    #and that an invalid wallet returns false.
    def test_is_valid(self):
        wallet = Wallet('t1NGCodd8fdGfbxyENtmHQ4yrVYqQ2Rbf98')
        self.assertTrue(wallet.is_valid())

        wallet = Wallet('invalid_address')
        self.assertFalse(wallet.is_valid())

    #tests that we are getting back a list of data from the api.
    def test_get_node_list(self):
        wallet = Wallet('t1NGCodd8fdGfbxyENtmHQ4yrVYqQ2Rbf98')
        node_list = wallet.get_node_list()
        self.assertIsInstance(node_list, list)