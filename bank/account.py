class Account(object):
    """account"""
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

class Withdraws(object):
    """withdraw"""
    def __init__( self, acount_number, balance, withdraw):
        self.balance = balance-withdraw