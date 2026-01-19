import pytest 
from app.scripts.wallet import Wallet

def test_credit_adds_balance_and_event():
    wallet = Wallet("wallet-1", 100)

    wallet.credit(50)

    assert wallet.balance == 150

    events = wallet.pull_events()
    assert len(events) == 1
    assert events[0]["type"] == "WalletCredited"
    assert events[0]["amount"] == 50

def test_debit_adds_balance_and_event():
    wallet = Wallet("wallet-1", 100)

    wallet.debit(50)

    assert wallet.balance == 50

    events = wallet.pull_events()
    assert len(events) == 1
    assert events[0]["type"] == "WalletDebited"
    assert events[0]["amount"] == 50

def test_debit_raises_exception_when_insufficient_funds():
    wallet = Wallet("wallet-1", 30)

    with pytest.raises(Exception, match="Insufficient funds"):
        wallet.debit(50)

def test_pull_events_clears_event_list():
    wallet = Wallet("wallet-1", 100)

    wallet.credit(10)
    events = wallet.pull_events()

    assert len(events) == 1
    assert wallet.pull_events() == []