from blockChain import SimpleBlockchain

block_one_transactions = {"from":"Sokrates", "to": "Plato", "amount":"1"}
block_two_transactions = {"from": "Plato", "to":"Aristo", "amount":"125"}
block_three_transactions = {"from":"Descartes", "to":"Spinoza", "amount":"250"}
fake_transactions = {"from": "Descartes", "to":"Spinoza", "amount":"555"}

local_blockchain = SimpleBlockchain() 

local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.chain[2].trx = fake_transactions
x=local_blockchain.validate_chain()