"""Bank"""
class Bank(object):
    """ bank """
    def __init__(self):
        self.accounts = {}
    def add_account(self, account):
        """ add account"""
        self.accounts[account.account_number] = account.balance
    def get_account_balance(self, account_number):
        """get_account"""
        return self.accounts.get(account_number)
    def account_exist(self, account_number):
        """account_exist"""
        self.accounts.get(account_number) != 'None'
