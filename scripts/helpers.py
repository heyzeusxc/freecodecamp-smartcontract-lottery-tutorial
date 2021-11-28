from brownie import MockV3Aggregator, network, config, accounts
from web3 import Web3

LOCAL_DEV_CHAINS = ['development', 'ganache-local']

decimals = 18
startingPrice = 2000

def get_account():
    if network.show_active() in LOCAL_DEV_CHAINS:
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])

def deploy_mock():
    print(f'Active network is {network.show_active()}')
    print('Deploying Mock Aggregator')
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(decimals, Web3.toWei(startingPrice,'ether'), {'from': get_account()})
    price_feed_address = MockV3Aggregator[-1].address
    print('Mock Aggregator Deployed')