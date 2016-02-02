import random
import string
import os
import config

user = []

if config.SEC_LEVEL == 1:
    valList = list(string.ascii_letters + string.digits)
elif config.SEC_LEVEL == 2:
    valList = list(string.ascii_letters + string.digits + string.punctuation)
else:
    valList = list(string.printable)

def generate(valList, length):
    password = []
    for char in range(1, length + 1):
        password.append(str(valList[random.randint(1, 61)]))
    return "".join(password)

While True:
    if config.USE_SECURE_SEED == True:
        seed = os.urandom(config.LEN_SECURE_SEED)
        random.seed(seed)
    length = int(raw_input("How long should the password be?: "))
    count = int(raw_input("How many users would you like to generate passwords for?: "))
    for password in range(1, count+1):
        pword = generate(valList, length)
        current = {password: pword}
        user.append(current)

    with open(str(config.OUTPUT_FILE), "w") as res:
        for item in user:
            for field, field2 in item.iteritems():
                res.write(str(field) + ", " + str(field2) + "\n")
