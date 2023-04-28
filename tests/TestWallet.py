import unittest
from Wallet import Wallet

class TestWallet(unittest.TestCase):
    def test_is_valid(self):
        wallet = Wallet('t1NGCodd8fdGfbxyENtmHQ4yrVYqQ2Rbf98')
        self.assertTrue(wallet.is_valid())

        wallet = Wallet('invalid_address')
        self.assertFalse(wallet.is_valid())

    def test_get_node_list(self):
        wallet = Wallet('t1NGCodd8fdGfbxyENtmHQ4yrVYqQ2Rbf98')
        node_list = wallet.get_node_list()
        self.assertIsInstance(node_list, list)

if __name__ == '__main__':
    unittest.main()  