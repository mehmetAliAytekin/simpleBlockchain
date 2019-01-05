from datetime import datetime
from hashlib import sha256


class SimpleBlock:
  def __init__(self, trx, previousHash, nonce = 0):
    self.timestamp = datetime.now()
    self.trx = trx
    self.previousHash = previousHash
    self.nonce = nonce
    self.currentHash = self.generate_block_hash()
    
  def print_block(self): 
    print("timestamp : {0} ; current hash : {1} ;  transactions :  {2}" .format( self.timestamp,self.currentHash,self.trx)) 
    
  def generate_block_hash(self): 
    content = self.get_block_contents_in_str()
    currentHash = self.to_hash(content)
    return currentHash.hexdigest()

  def to_hash(self,content):
    return sha256(content.encode())

  def get_block_contents_in_str(self):
    return str(self.timestamp) + str(self.trx) + str(self.previousHash) + str(self.nonce)



class SimpleBlockchain:
  def __init__(self):
    self.chain = []
    self.allTrx = []
    self.genesis_block()

  def genesis_block(self):
    trx = {}
    genesisBlock = SimpleBlock(trx, "0")
    self.chain.append(genesisBlock)
    return self.chain
  
  def add_block(self, transactions):
    previousHash = self.chain[len(self.chain)-1].currentHash
    newBlock = SimpleBlock(transactions, previousHash)
    newBlock.generate_block_hash()
    proof = self.proof_of_work(newBlock)
    self.chain.append(newBlock)
    return proof, newBlock

  def validate_chain(self):
    for i in range(1, len(self.chain)):
      current = self.chain[i]
      previous = self.chain[i-1] 
      if(current.currentHash != current.generate_block_hash()):
        current.print_block();
        print("it is broken")
        return False
      if(current.previousHash != previous.generate_block_hash()):
        current.print_block();
        return False
    return True
  
  def proof_of_work(self,block, difficulty=2):
    proof = block.generate_block_hash()
    while proof[:difficulty] != '0'*difficulty:
      block.nonce += 1
      proof = block.generate_block_hash()
    block.nonce = 0
    return proof