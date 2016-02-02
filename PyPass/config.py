# # # # # # # # # # #
# CONFIG
# # # # # # # # # # #
# SEC_LEVEL: The range of possible characters which can be used in generating passwords. 
# 1: Only letters and digits
# 2: Letters, digits and punctuation
# 3: All printable characters
# 
# USE_SECURE_SEED: Whether or not to use a cryptographically-secure seed for each session
# True: Secure seed enabled
# False: Secure seed disabled
#
# LEN_SECURE_SEED: How large (in bytes) the secure seed should be (if USE_SECURE_SEED is set to True)
# Example: 4
#
# OUTPUT_FILE: The file which the resulting passwords will be outputted to. Include file extension. MUST BE ENCLOSED IN "'s
# Example: "C:/Users/Sample/passwords.csv"
# # # # # # # # # # #

SEC_LEVEL = 1
USE_SECURE_SEED = True
LEN_SECURE_SEED = 8
OUTPUT_FILE = "output.csv"

# # # # # # # # # # # # # # # #
# DO NOT EDIT BELOW THIS LINE
# # # # # # # # # # # # # # # #

def SEC_LEVEL():
    return SEC_LEVEL

def USE_SECURE_SEED():
    return USE_SECURE_SEED

def LEN_SECURE_SEED():
    return LEN_SECURE_SEED

def OUTPUT_FILE():
    return OUTPUT_FILE
