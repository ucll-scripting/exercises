import base64
import hashlib


def process(i):
    hash = hashlib.sha384(str(i).encode('ascii')).digest()
    return base64.b64encode(hash).decode('ascii')


for i in range(0, 10001):
    result = process(i)
    print(f'{i} {result}')
