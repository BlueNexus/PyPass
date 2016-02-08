import random
import string
import os
import config

if config.SEC_LEVEL == 1:
    valList = list(string.ascii_letters + string.digits)
elif config.SEC_LEVEL == 2:
    valList = list(string.ascii_letters + string.digits + string.punctuation)
elif config.SEC_LEVEL == 3:
    valList = list(string.printable)
else:
    print "ERROR: INVALID VALUE(SEC_LEVEL)"
    exit()


def generate(valList, length):
    password = []
    for char in range(1, length + 1):
        password.append(str(valList[random.randint(1, len(valList))]))
    return "".join(password)

While True:
    if config.USE_SECURE_SEED is True:
        seed = os.urandom(config.LEN_SECURE_SEED)
        random.seed(seed)
    try:
        length = int(raw_input("How long should the password be?: "))
    except:
        print "ERROR: INVALID INPUT"
        continue
    for password in range(1, count+1):
        pword = generate(valList, length)
        current = {password: pword}
        print current
