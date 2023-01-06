from hashlib import sha256

def update_hash(*args):
    hashing_text = ""
    h = sha256()

    for arg in args:
        hashing_text += str(arg)

    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()

class Block():
    data = None
    hash = None
    nonce = 0
    previous_hash = "0" * 64

    def __init__(self, data, number=0):
        self.data = data
        self.number = number

    def hash(self):
        return update_hash(self.data, self.previous_hash, self.nonce, self.number)

    def __str__(self):
        return f"Block#: {self.number}\nHash: {self.hash()}\nPrevious Hash: {self.previous_hash}\nData: {self.data}\nNonce: {self.nonce}\n"

class Blockchain():
    num_zeros = 7

    def __init__(self, chain=[]):
        self.chain = chain

    def add_blocks(self, block):
        self.chain.append(block)

    def mine(self, block):
        try:
            block.previous_hash = self.chain[-1].hash()
        except IndexError:
            pass

        while True:
            if block.hash()[:self.num_zeros] == '0' * self.num_zeros:
                self.add_blocks(block)
                break
            else:
                block.nonce += 1

class main():
    blockchain = Blockchain()
    database = [("Bob pays Alice 100LD", "You pay Bod 50LD", "Charlie pays You 70LD", "Alice pays Charlie 80LD"), 
    ("Bob pays Alice 110LD", "You pay Bod 70LD", "Charlie pays You 45LD", "Alice pays Charlie 100LD"),
    ("Bob pays Alice 20LD", "You pay Bod 25LD", "Charlie pays You 30LD", "Alice pays Charlie 10LD"),
    ("Bob pays Alice 45LD", "You pay Bod 100LD", "Charlie pays You 20LD", "Alice pays Charlie 20LD")]

    num = 0
    for data in database:
        num += 1
        blockchain.mine(Block(data, num))

    for block in blockchain.chain:
        print(block)


if __name__ == '__main__':
    main()