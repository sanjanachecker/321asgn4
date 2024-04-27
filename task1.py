from hashlib import sha256
import string
import random

def sha_hash(input):
    hash = sha256(input.encode())
    hx = hash.hexdigest()[:10]
    # print('hx: ', hx)
    return hx


def hamming_dist(str1, str2):
    bins1 = ''.join(format(ord(i), '08b') for i in str1)
    bins2 = ''.join(format(ord(i), '08b') for i in str2)
    print(bins1)
    print(bins2)

    dist = 0

    length = min(len(bins1), len(bins2))
    i = 0
    while i < length:
        if bins1[i] != bins2[i]:
            dist += 1
        i += 1

    dist += max(len(bins1), len(bins2)) - i

    print("distance: ", dist)


sha_hash("hi")
hamming_dist("hello", "helln")
hamming_dist("world", "worle")

# part c

def generate_string(length):
    n = length
    res = ''.join(random.choices(string.ascii_lowercase +
                                string.digits, k=n))
    # # print result
    # print("The generated random string : " + str(res))
    return res

def generate_key_value():
    message = generate_string(8)
    hash = sha_hash(message)
    return message, hash

# print(generate_key_value())
    
messages = {}
def find_collision(messages):
    found = False
    while not found:
        message, hash = generate_key_value()
        if (hash not in messages):
            messages[hash] = message
        else:
            if(messages[hash] != message):
                found = True
                return hash, messages[hash], message

print(find_collision(messages))
# print(messages)