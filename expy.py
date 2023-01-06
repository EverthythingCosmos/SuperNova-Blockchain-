from hashlib import sha256

def update_hash(*args):
    hashing_text = ""
    h = sha256()

    for arg in args:
        hashing_text += str(arg)

    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()

data = 'hello'
nonce = 0

def hash(string, number):
    return update_hash(string, number)

while True:
    if update_hash(data, nonce)[:3] == '0' * 3:
        print(nonce)
        break
    else:
        nonce += 1