from config import Config 


class Blockchair(Config):
    def __init__(self, API=''):
        self.configuration(API)


    def transaction(self, tx_hash):
        self.url_creator(f'/dashboards/transaction/{tx_hash}')
        status, response = self.requests_and_parse('GET')
        return status, response


    def transactions(self, txs_hash):
        self.url_creator(f'/dashboards/transactions/{",".join(txs_hash)}')
        status, response = self.requests_and_parse('GET')
        return status, response
