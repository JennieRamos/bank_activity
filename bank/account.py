"""class"""
class Account(object):
    """account"""
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def test1(self):
        """test1"""
        pass
    def test3(self):
        """test3"""
        pass
class Withdraws(object):
    """withdraw"""
    def __init__(self, balance, withdraw):
        self.balance = balance-withdraw
    def test2(self):
        """test2"""
        pass
    def test4(self):
        """test4"""
        pass