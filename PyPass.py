import random
import string


user = []
valList = list(string.ascii_letters + string.digits)

def generate(valList, length):
    password = []
    for char in range(1, length + 1):
        password.append(str(valList[random.randint(1, 61)]))
    return "".join(password)


length = int(raw_input("How long should the password be?: "))
count = int(raw_input("How many users would you like to generate passwords for?: "))
for password in range(1, count+1):
    pword = generate(valList, length)
    current = {password: pword}
    user.append(current)

with open("results.txt", "w") as res:
    for item in user:
        res.write(str(item) + "\n")
