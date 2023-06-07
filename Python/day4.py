import hashlib


def checkSoln(soln):
    return soln[:6] == "000000"


input = "ckczppom"
# input = "pqrstuv"

i = 0
while True:
    result = hashlib.md5((input + str(i)).encode())
    if checkSoln(result.hexdigest()):
        print(i)
        break
    else:
        i += 1
