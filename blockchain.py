from time import time
import json
import hashlib

from urllib.parse import urlparse

import requests


class Blockchain:
    def __init__(self):
        self.chain = [] #normally a linked list but simplified to a list here
        self.nodes = set() #address book
        self.current_transactions = [] #transaction list that have yet to post

        #create the first block of the chain
        self.new_block(previous_hash = '1', proof = 100)


    #function to register a neighboring node (other user) in personal address book
    def register_node(self,address):
        parsed_url = urlparse(address) #parse value into url

        if parsed_url.netloc: #if there is a specific net location address
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path: #if URL doesn't have schema e.g. "192.168.1.1:3000"
            self.nodes.add(parsed_url.path)
        else: #if no url provided
            raise ValueError("Invalid address")


    #function to check for valid chain
    def valid_chain(self, chain):
        last_block = chain[0] #iterate through all blocks
        #we are chekcing the hash values lining up instead of checking proof
        current_index = 1
        while current_index < len(chain):
            block = chain[current_index] #store current block
            last_block_hash = self.hash(last_block)

            if block["previous_hash"] != last_block_hash:
                return False

            last_block = block
            current_index += 1

        #all blocks checked after this loop is gone through
        return True



    #function to resolve conflicts in between chains
    def resolve_conflicts(self):
        neighbors = self.nodes #load address book into mutable temp
        new_chain = None # temp, store for neighbor's chain

        max_length = len(self.chain)

        for node in neighbors:
            response = requests.get(f"http://{node}/chain")

            if response.status_code == 200:
                length = response.json()['length']
                chain = repsonse.json()["chain"]

                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        if new_chain:
            self.chain = new_chain
            return True
        return False

    #function to create a new block
    def new_block(self,proof,previous_hash):
        #what we need to make the block
        block = {
            "index": len(self.chain)-1,
            "timestamp": time(),
            "transactions": self.current_transactions,
            "proof": proof,
            "previous_hash": previous_hash or self.hash(self.last_block)
        }

        #reset the list of our un_tracked transactions
        self.current_transactions = []

        #append the new block of our chain
        self.chain.append(block)

        #return our block object
        return block

    #function to create a new sale/transaction of money



    #function to get the most recent block of the blockchain
    @property
    def last_block(self):
        return self.chain[-1]
    #function to create a cryptographic hash
    @staticmethod
    def hash(block):
        #put all JSON metadata into encoded string
        strBlock = json.dumps(block, sort_keys = True).encode()
        #return SHA256 has in hex
        return hashlib.sha256(strBlock).hexdigest()
    #function to check the proof of work of a block
    def proof_of_work(self, last_block):
        last_proof = last_block["proof"] #getting your proof from your last block
        last_hash = self.hash(last_block) #recalc last hash

        proof = 0
        while self.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1 #iterate

        return proof

    #function to check if a proof of work is valid
    @staticmethod
    def valid_proof(last_proof, proof, last_hash):
        #dont do this, for simplification
        #create a proof based on these encoded values
        guess = f"{last_proof}{proof}{last_hash}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        #a valid proof will have first four bits zeroes
        return guess_hash[:4] == "0000"
    