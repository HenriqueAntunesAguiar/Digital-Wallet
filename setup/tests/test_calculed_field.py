from ..app.document import NewTransaction
import pytest 

def test_GetFakerBalance(): 

    new_transaction = NewTransaction()
    assert new_transaction.GetFakerBalance('1a') == 100.00

def test_GetFakerBalanceErrorNotFoundClientId(): 

    new_transaction = NewTransaction()

    with pytest.raises(KeyError):
        new_transaction.GetFakerBalance('999')

def test_MakeTransaction():

    new_transaction = NewTransaction()

    new_transaction.MakeTransaction('1a', 100.00, '2b', 100.00,50.00)