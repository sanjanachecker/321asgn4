import nltk
import sys

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
