class DataModel():
    
    def __init__(self):
        self.balances = {
            '1a':100.00,
            '2b':100.00
        }

        self.log = []

    def GetFakerBalance(self, wallet_id):
        return self.balances[wallet_id]
    
    def UpdateFakerBalance(self, wallet_id:str, new_value_of_balance:float):
        self.balances[wallet_id] = new_value_of_balance

        
class Wallet:

    def __init__(self, wallet_id, balance):
       self.wallet_id = wallet_id
       self.balance = balance

    def debit(self, amount):
        if self.balance - amount < 0:
            raise Exception('Invalid amount')
        
        self.balance -= amount

    def credit(self, amount):
        self.balance += amount

class Controller:
    
    def __init__(self):
        self.model = DataModel()

    def MakeTransaction(self):

        client_1_balance = self.model.GetFakerBalance('1a')
        client_1_wallet = Wallet('1a', client_1_balance)
        client_1_wallet.debit(50.00)

        client_2_balance = self.model.GetFakerBalance('2b')
        client_2_wallet = Wallet('2b', client_2_balance)
        client_2_wallet.credit(50.00)

        self.model.UpdateFakerBalance(client_1_wallet.wallet_id, client_1_wallet.balance)
        self.model.UpdateFakerBalance(client_2_wallet.wallet_id, client_2_wallet.balance)