class Blockchain:
    def __init__(self):
        self.chain = [] #normally a linked list but simplified to a list here
        self.nodes = set() #address book
        self.current_transactions = [] #transaction list that have yet to post

        #create the first block of the chain
        self.new_block(previous_hash = '1', proof = 100)
        

    #function to register a neighboring node (other user) in personal address book

    #function to check for valid chain

    #function to resolve conflicts in between chains

    #function to create a new block

    #function to create a new sale/transaction of money

    #function to get the most recent block of the blockchain

    #function to create a cryptographic hash

    #function to check the proof of work of a block

    #function to check if a proof of work is valid

    