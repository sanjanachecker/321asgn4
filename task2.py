import nltk
import sys
from bcrypt import *
from nltk.corpus import words

def parse():
    filename = sys.argv[1]

    with open(filename, 'r') as file:
        for line in file:
            parts = line.split("$")
            user_info = parts[0].split(":")
            username = user_info[0]
            algo = parts[1]
            wf = parts[2]
            hash_salt = parts[3]
            print(username, " ", algo, " ", wf, " ", hash_salt, "\n")
            # return hash_salt


# hashpw(<plaintext word>, <29-char salt for bcrypt>)
# print(hashpw(b"registrationsucks", b"$2b$08$J9FW66ZdPI2nrIMcOxFYI."))

words = words.words()
for word in words:
    length = len(word)
    if length <= 10 and length >= 6:
        if checkpw(word, b'$2b$08$J9FW66ZdPI2nrIMcOxFYI.qx268uZn.ajhymLP/YHaAsfBGP3Fnmq'):
            print(word)