import hashlib

key = "yzbqklnj"
# key = "abcdef"

def eval(s):
    hash = hashlib.md5(s.encode('utf8')).hexdigest()
    return hash[:5] == "00000"

test = 1 # 609043
while True:
    if eval(key + str(test)):
        break

    test += 1

print(test)