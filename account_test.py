import unittest
from account import Account
from account import Withdraws
from account import Check_balance

class TestAccount(unittest.TestCase):
  def test_account_object_can_be_created(self):
    account = Account()

class TestAccount(unittest.TestCase):
  def test_account_object_returns_current_balance(self):
    account = Account("001", 50)
    self.assertEqual(account.account_number, "001")
    self.assertEqual(account.balance, 50)
 
  def test_withdraw(self):
    account = Withdraws("001", 50, 20)
    self.assertEqual(account.balance, 30)

  def test_check_balance_if_int(self):
    account = Check_balance('None')
    self.assertRaises(typeError,"30")
    
    

if __name__ == '__main__':
  unittest.main()
