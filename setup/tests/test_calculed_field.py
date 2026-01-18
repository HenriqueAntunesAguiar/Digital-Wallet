from setup.app.document import NewTransaction
import pytest 

@pytest.fixture
def new_transaction():
    return NewTransaction()

def test_GetFakerBalance(new_transaction): 

    assert new_transaction.GetFakerBalance('1a') == 100.00

def test_GetFakerBalanceErrorNotFoundClientId(new_transaction): 

    with pytest.raises(KeyError):
        new_transaction.GetFakerBalance('999')

def test_MakeTransactionValidating(new_transaction):

    new_transaction.MakeTransaction('1a', 100.00, '2b', 100.00,50.00)

    assert new_transaction.GetFakerBalance('1a') == 150.00
    assert new_transaction.GetFakerBalance('2b') == 50.00

def test_ValidateTransactionAboutValueDiscountFalse(new_transaction):

    assert new_transaction.ValidateTransactionAboutValueDiscount(100.00, 100.01) is False
    assert new_transaction.ValidateTransactionAboutValueDiscount(100.00, 100.00) is True

def test_UpdateFakerBalance(new_transaction):

    new_transaction.UpdateFakerBalance('1a', 150.00) 

    assert new_transaction.GetFakerBalance('1a') == 150.00
    assert new_transaction.GetFakerBalance('2b') == 100.00

def test_TransactionValueSuccess(new_transaction):

    assert new_transaction.TransactionValue('1a', '2b', 50.00) == 'Success: The operation did normaly.'
    assert new_transaction.GetFakerBalance('1a') == 150.00
    assert new_transaction.GetFakerBalance('2b') == 50.00

def test_TransactionValueError(new_transaction):
   
    assert new_transaction.TransactionValue('1a', '2b', 150.00) == 'Error: No balance to make a transaction.'
    assert new_transaction.GetFakerBalance('1a') == 100.00
    assert new_transaction.GetFakerBalance('2b') == 100.00