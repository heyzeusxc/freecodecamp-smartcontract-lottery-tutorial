from brownie import Lottery, accounts, config, network
from scripts.helpers import get_account

def test_get_entrance_fee():
    account = get_account()
    lottery = Lottery.deploy(config['networks'][network.show_active()]['dai-usd-priceFeed'], {'from' : account})
    assert lottery.getEntranceFee() > 0
    assert lottery.getEntranceFee() < 101 * (10**18)
