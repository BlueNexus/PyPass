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
#
# MODE: Whether the generator is in Single or Multi mode.
# 1: Single
# 2: Multi
# # # # # # # # # # #

C_SEC_LEVEL = 1
C_USE_SECURE_SEED = True
C_LEN_SECURE_SEED = 8
C_OUTPUT_FILE = "results.csv"
C_MODE = 1

# # # # # # # # # # # # # # # #
# DO NOT EDIT BELOW THIS LINE
# # # # # # # # # # # # # # # #


def SEC_LEVEL():
    if C_SEC_LEVEL is not None and 0 < C_SEC_LEVEL < 4:
        return(C_SEC_LEVEL)
    else:
        if C_SEC_LEVEL is None:
            print("CONFIG_ERROR: NULL VALUE(SEC_LEVEL)")
        else:
            print("CONFIG_ERROR: INVALID VALUE(SEC_LEVEL)")
        exit()


def USE_SECURE_SEED():
    if C_USE_SECURE_SEED is not None and C_USE_SECURE_SEED in (True, False):
        return (C_USE_SECURE_SEED)
    else:
        if C_USE_SECURE_SEED is None:
            print("CONFIG_ERROR: NULL VALUE(USE_SECURE_SEED)")
        else:
            print("CONFIG_ERROR: INVALID VALUE(USE_SECURE_SEED)")
        exit()


def LEN_SECURE_SEED():
    if C_LEN_SECURE_SEED is not None and 0 < C_LEN_SECURE_SEED:
        return(C_LEN_SECURE_SEED)
    else:
        if C_LEN_SECURE_SEED is None:
            print("CONFIG_ERROR: NULL VALUE(LEN_SECURE_SEED)")
        else:
            print("CONFIG_ERROR: INVALID VALUE(LEN_SECURE_SEED)")
        exit()


def OUTPUT_FILE():
    if C_OUTPUT_FILE is not None:
        return(C_OUTPUT_FILE)
    else:
        print("CONFIG_ERROR: NULL VALUE(OUTPUT_FILE)")
        exit()

def MODE():
    if C_MODE in (1, 2):
        return(C_MODE)
    else:
        print("CONFIG_ERROR: INVALID VALUE(MODE)")
        exit()
