from brownie import accounts, Target_Bank  


account0 = accounts[0]
account1 = accounts[1]

def deploy_bank():
    bank = Target_Bank.deploy({"from": account0})
    return bank

def bank_interactions(bank):
    print(bank.getBalance)
    bank.deposit({"from": account0, "value": 1000000000000000000})
    print(f'Account0: {bank.getBalance({"from": account0})}')

    bank.deposit({"from": account1, "value": 2000000000000000000})
    print(f'Account1: {bank.getBalance({"from": account1})}')

def main():
    bank = deploy_bank()
    bank_interactions(bank)

