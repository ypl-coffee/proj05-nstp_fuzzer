#!/usr/bin/env python3

import sys, crypt
import nacl.pwhash

if (len(sys.argv) != 3):
    print("usage: python3 %s <username> <password>" % sys.argv[0])
    exit(1)
    
username = sys.argv[1]
password = sys.argv[2]
print("username: %s" % username)
print("password: %s\n" % password)

# md5
print(username + ":" + crypt.crypt(password, crypt.mksalt(method=crypt.METHOD_MD5)))

# sha256
rounds_sha256 = 535000
prefix_sha256 = "$5$rounds={0}$".format(rounds_sha256)
print(username + ":" + crypt.crypt(password, prefix_sha256 + crypt.mksalt(method=crypt.METHOD_SHA256)))

# sha512
rounds_sha512 = 656000
prefix_sha512 = "$6$rounds={0}$".format(rounds_sha512)
print(username + ":" + crypt.crypt(password, prefix_sha512 + crypt.mksalt(method=crypt.METHOD_SHA512)))

# argon2id
print(username + ":" + nacl.pwhash.argon2id.str(password.encode()).decode())