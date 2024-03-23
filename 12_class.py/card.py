from datetime import datetime

class Card:
    def __init__(self, _number, _expiry, _cvv, _holderName): # constructor
        self.number = _number
        self.expiry = datetime.strptime(_expiry, "%Y-%m-%d")
        self.cvv = _cvv
        self.holderName = _holderName

    def isExpired(self):
        now = datetime.now()
        if self.expiry > now:
            return False
        else:
            return True
        
    def expiryDays(self):
        now = datetime.now()
        diff = self.expiry - now
        return diff.days