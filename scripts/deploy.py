from brownie import Lottery, MockV3Aggregator, network, config
from scripts.helpers import get_account, deploy_mock, LOCAL_DEV_CHAINS
from web3 import Web3

def deploy_lottery():
    account = get_account()

    if network.show_active() not in LOCAL_DEV_CHAINS:
        price_feed_address = config['networks'][network.show_active()]['dai-usd-priceFeed']
    else:
        deploy_mock()
        price_feed_address = MockV3Aggregator[-1].address

    lottery = Lottery.deploy(price_feed_address, {'from': account}, publish_source=config['networks'][network.show_active()].get('verify'))
    print(f'contract deployed to {lottery.address}')

def main():
    deploy_lottery()