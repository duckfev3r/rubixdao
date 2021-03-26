import unittest

from contracting.client import ContractingClient


class TokenTests(unittest.TestCase):
    def setUp(self):
        self.client = ContractingClient()
        self.client.flush()
        with open('dai_token.py') as file:
            code = file.read()
        self.client.submit(code, name='dai_token', constructor_args={'vk': 'me', 'owner': 'default_owner'})

    def tearDown(self):
        pass

    def test(self):
        pass

if __name__ == "__main__":
    unittest.main()
