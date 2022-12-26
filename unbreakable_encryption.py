from secrets import token_bytes


def random_key(length):
    tb = token_bytes(length)
    return int.from_bytes(tb, 'big')


def encrypt(original):
    original_bytes = original.encode()
    dummy = random_key(len(original_bytes))
    original_key = int.from_bytes(original_bytes, 'big')
    encrypted = original_key ^ dummy
    return dummy, encrypted


def decrypt(key1, key2):
    decrypted = key1 ^ key2
    temp = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, 'big')
    return temp.decode()


a = encrypt('hello world!')
print(a)
b = decrypt(a[0], a[1])
print(b)
