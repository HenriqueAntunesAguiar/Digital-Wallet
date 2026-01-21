from app.scripts.wallet import Wallet
import pytest

def test_debit_success():
    test_debit_wallet = Wallet('1',100.00, '2')
    test_debit_wallet.debit(10)

    assert test_debit_wallet.balance == 90
    assert test_debit_wallet._events[0]['type'] == 'WalletDebited'

def test_debit_fail():
    test_debit_wallet = Wallet('1',100.00, '2')
    
    with pytest.raises(Exception) as Error:
        test_debit_wallet.debit(101)
    
    assert str(Error.value) == 'Insufficient funds'
    assert test_debit_wallet._events == []

def test_credit_success():
    test_credit_wallet = Wallet('1',100.00, '2')
    test_credit_wallet.credit(10)

    assert test_credit_wallet.balance == 110.00
    assert test_credit_wallet._events[0]['type'] == 'WalletCredited'
