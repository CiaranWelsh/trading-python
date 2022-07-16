from trade.wallet import Wallet
import pytest

@pytest.fixture
def wallet1000():
    return Wallet(1000)


@pytest.fixture
def wallet800():
    return Wallet(800)

def test_wallet_add(wallet1000):
    wallet = wallet1000 + 5
    assert wallet == 1005

def test_wallet_add2(wallet1000, wallet800):
    wallet = wallet1000 + wallet800
    assert wallet == 1800

def test_wallet_sub(wallet1000):
    wallet = wallet1000 - 5
    assert wallet == 995

def test_wallet_sub2(wallet1000, wallet800):
    wallet = wallet1000 - wallet800
    assert wallet == 200

def test_wallet_div(wallet1000):
    wallet = wallet1000 / 5
    assert wallet == 200.0

def test_wallet_div2(wallet1000, wallet800):
    wallet = wallet1000 / wallet800
    assert wallet == 1.25

def test_wallet_mul(wallet1000):
    wallet = wallet1000 * 5
    assert wallet == 5000

def test_wallet_mul2(wallet1000, wallet800):
    wallet = wallet1000 * wallet800
    assert wallet == 800000

def test_wallet_eq(wallet1000):
    wallet = Wallet(1000)
    assert wallet == wallet1000

def test_wallet_eq2(wallet1000):
    assert 1000 == wallet1000

def test_almost_equal():
    w1 = Wallet(1.2345)
    assert w1.almost_equal(1.23453, 1e-4)













