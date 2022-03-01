from urllib.parse import urlencode
import httpx

class Config:        
    def configuration(self, API):
        self.__api(API)
        self.__url_base_creator()
        self.__client = httpx.Client(limits=httpx.Limits(max_connections=30), timeout=None)

    def __exit__(self):
        self.__client.close()
                
    def __api(self, API):
        self.API = API

    def __url_base_creator(self):
        self.url_base = 'https://api.blockchair.com/'

    def __unzip_params(self, params):
        if params:
            return params['params']
        else:
            return ''

    def blockchain(self, chain):
        if chain =='BTC':
            self.chain = 'bitcoin'
        elif chain == 'BCH':
            self.chain = 'bitcoin-cash'
        elif chain == 'BSV':
            self.chain = 'bitcoin-sv'
        elif chain == 'LTC':
            self.chain = 'litecoin'
        elif chain == 'ETH':
            self.chain = 'ethereum'
        elif chain == 'DOGE':
            self.chain = 'dogecoin'
        elif chain == 'ZEC':
            self.chain = 'zcash'


    def url_creator(self, url_final, **params):
        params = self.__unzip_params(params)
        self.url = self.url_base + self.chain + url_final 

        if self.API:
            self.url += '?key=' + self.API + urlencode(params)
        else:
            self.url += urlencode(params)

    def requests_and_parse(self, method):
        response = self.__client.send(self.__client.build_request(method, self.url))
        status = response.status_code
        
        if self.check_status(status):
            return status, response.json()
        else:
            print('warning, status code:', status)
            print(response.text)
            return status, None
    
    def check_status(self, status):
        if status in range(200,299):
            return True
        else:
            return False
