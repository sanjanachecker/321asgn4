import nltk
import sys
from bcrypt import *
from nltk.corpus import words
import time

def main():
    filename = sys.argv[1]

    with open(filename, 'r') as file:
        for line_num,line in enumerate(file):
            parts = line.strip().split(":")
            start = time.asctime(time.localtime())
            print(parts)
            # user_info = parts[0].split(":")
            # username = user_info[0]
            # algo = parts[1]
            # wf = parts[2]
            # hash_salt = parts[3]
            # print(username, " ", algo, " ", wf, " ", hash_salt, "\n")
            print(parts[0], "start time:", start)
            print(parts[0], "password:", find_password(parts[1]))
            end = time.asctime(time.localtime())
            print(parts[0], "end time:", end)


def find_password(hash):
    possible_words = words.words()
    for word in possible_words:
        length = len(word)
        if length <= 10 and length >= 6:
            if checkpw(word.encode('utf-8'), hash.encode('utf-8')):
                return word

# word = "registrationsucks"
# print(hashpw(b"registrationsucks", b"$2b$08$J9FW66ZdPI2nrIMcOxFYI."))
# print(checkpw(word.encode('utf-8'),
#       b'$2b$08$J9FW66ZdPI2nrIMcOxFYI.zKGJsUXmWLAYWsNmIANUy5JbSjfyLFu'))
# if checkpw(word.encode('utf-8'), b'$2b$08$J9FW66ZdPI2nrIMcOxFYI.zKGJsUXmWLAYWsNmIANUy5JbSjfyLFu'):
#     print("True")

if __name__ == "__main__":
    main()