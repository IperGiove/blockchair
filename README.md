# Blockchair Unofficial
Python library to manage bloackchair api

# Functions
- transaction
- transactions

### Example
```python
from blockchair import Blockchair
blockchair = Blockchair()
blockchair.blockchain('BTC') 
adresses = ['2668c2141cd939a4ae9b67f3837c97899e2ed4786b1951e36e6cb062233ea820', 
            'd7705364145822b847c21219e0fd2f27ef251ce5bbb37bfb69ec55c22988c99e']

print(blockchair.transaction(adresses[0]))

print(blockchair.transactions(adresses))
```
