class NewTransaction():
    
    def __init__(self):
        self.balances = {
            '1a':100.00,
            '2b':100.00
        }

    def TransactionValue(self, client_id_to_recive:str, client_id_to_discount:str, value_of_transaction:float):
        
        client_to_recive_current_balance = self.GetFakerBalance(client_id_to_recive)
        client_to_discount_current_balance = self.GetFakerBalance(client_id_to_discount)

        if self.ValidateTransactionAboutValueDiscount(client_to_discount_current_balance):
            self.MakeTransaction(client_id_to_recive, client_to_recive_current_balance, client_id_to_discount, client_to_discount_current_balance, value_of_transaction)
            return 'Success: The operation did normaly.'
        else:
            return 'Error: No balance to make a transaction.'


    def ValidateTransactionAboutValueDiscount(current_value:float, value_to_discount:float):

        if (current_value - value_to_discount) < 0:
            return False
        else:
            return True

    def GetFakerBalance(self, client_id):
        return self.balances[client_id]

    def MakeTransaction(self, client_id_to_recive:str, client_to_recive_current_balance:float, client_id_to_discount:str, client_to_discount_current_balance:float, value_of_transaction:float):

        new_balance_of_client_to_recive = client_to_recive_current_balance + value_of_transaction
        new_balance_of_client_to_discount = client_to_discount_current_balance - value_of_transaction

        self.UpdateFakerBalance(client_id_to_recive, new_balance_of_client_to_recive)
        self.UpdateFakerBalance(client_id_to_discount, new_balance_of_client_to_discount)
    
    def UpdateFakerBalance(self, client_id:str, new_value_of_balance:float):

        self.balances[client_id] = new_value_of_balance
        