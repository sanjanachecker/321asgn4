import nltk
import sys
from bcrypt import *
from nltk.corpus import words
import time


def parse():
    filename = sys.argv[1]

    with open(filename, 'r') as file:
        for line in file:
            parts = line.split(":")
            start = time.time()
            # user_info = parts[0].split(":")
            # username = user_info[0]
            # algo = parts[1]
            # wf = parts[2]
            # hash_salt = parts[3]
            # print(username, " ", algo, " ", wf, " ", hash_salt, "\n")
            verify(parts[1])
            end = time.time()
            print(line, "start: ", start, " end: ", end)


# hashpw(<plaintext word>, <29-char salt for bcrypt>)
print(hashpw(b"registrationsucks", b"$2b$08$J9FW66ZdPI2nrIMcOxFYI."))


def verify(salt):
    words = words.words()
    for word in words:
        length = len(word)
        if length <= 10 and length >= 6:
            if checkpw(word.encode('utf-8'), salt.encode('utf-8')):
                print(word)
                print("true")


word = "registrationsucks"
print(hashpw(b"registrationsucks", b"$2b$08$J9FW66ZdPI2nrIMcOxFYI."))
print(checkpw(word.encode('utf-8'),
      b'$2b$08$J9FW66ZdPI2nrIMcOxFYI.zKGJsUXmWLAYWsNmIANUy5JbSjfyLFu'))
if checkpw(word.encode('utf-8'), b'$2b$08$J9FW66ZdPI2nrIMcOxFYI.zKGJsUXmWLAYWsNmIANUy5JbSjfyLFu'):
    print("True")
