import hashlib
m = hashlib.md5()
m.update('绝代双娇'.encode('utf-8'))
print(len(m.digest()))
print(m.hexdigest())
