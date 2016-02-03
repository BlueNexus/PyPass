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
    if SEC_LEVEL is not None:
        return SEC_LEVEL
    else:
        print "ERROR: NULL VALUE(SEC_LEVEL)"
        exit()

def USE_SECURE_SEED():
    if USE_SECURE_SEED is not None:
        return USE_SECURE_SEED
    else:
        print "ERROR: NULL VALUE(USE_SECURE_SEED)"
        exit()

def LEN_SECURE_SEED():
    if LEN_SECURE_SEED is not None:
        return LEN_SECURE_SEED
    else:
        print "ERROR: NULL VALUE(LEN_SECURE_SEED"
        exit()

def OUTPUT_FILE():
    if OUTPUT_FILE is not None:
        return OUTPUT_FILE
    else:
        print "ERROR: NULL VALUE(OUTPUT_FILE)"
        exit()
