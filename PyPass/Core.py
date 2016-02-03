import random
import string
import os
import config

user = []

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
        count = int(raw_input("How many users would you like to generate passwords for?: "))
    except:
        print "ERROR: INVALID INPUT"
        continue
    for password in range(1, count+1):
        pword = generate(valList, length)
        current = {password: pword}
        user.append(current)

    try:
        with open(str(config.OUTPUT_FILE), "w") as res:
            for item in user:
                for field, field2 in item.iteritems():
                    res.write(str(field) + ", " + str(field2) + "\n")
    except:
        print "ERROR: FILE ERROR"
        continue
