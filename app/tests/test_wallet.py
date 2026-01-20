import pytest 
from app.scripts.wallet import Wallet, ApplicationService

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

def test_execute_generates_debit_and_credit_events():
    service = ApplicationService(
        debit_wallet="wallet-debit",
        debit_wallet_balance=100,
        credit_wallet="wallet-credit",
        credit_wallet_balance=50
    )

    events = service.execute(30)

    assert len(events) == 2

    debit_event = events[0]
    credit_event = events[1]

    assert debit_event["type"] == "WalletDebited"
    assert debit_event["wallet_id"] == "wallet-debit"
    assert debit_event["amount"] == 30

    assert credit_event["type"] == "WalletCredited"
    assert credit_event["wallet_id"] == "wallet-credit"
    assert credit_event["amount"] == 30