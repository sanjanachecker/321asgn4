from hashlib import sha256
import string
import random
import time


def sha_hash(input, n):
    hash = sha256(input.encode())
    hx = hash.hexdigest()[:n]
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


# sha_hash("hi")
# hamming_dist("hello", "helln")
# hamming_dist("world", "worle")

# part c


def generate_string(length):
    n = length
    res = ''.join(random.choices(string.ascii_lowercase +
                                 string.digits, k=n))
    # # print result
    # print("The generated random string : " + str(res))
    return res


def generate_key_value(digest_size):
    message = generate_string(8)
    hash = sha_hash(message, digest_size)
    return message, hash

# print(generate_key_value())


def find_collision(digest_size):
    messages = {}
    found = False
    inputs = 0
    while not found:
        message, hash = generate_key_value(digest_size)
        if (hash not in messages):
            messages[hash] = message
            inputs += 1
        else:
            if (messages[hash] != message):
                found = True
                return inputs


def increment_by_2():
    time_list = [("bits", "secs")]
    input_list = [("bits", "inputs")]

    for i in range(14, 18, 2):
        start = time.time()
        inputs = find_collision(i)
        end = time.time()
        total_time = end - start
        time_list.append((i, total_time))
        input_list.append((i, inputs))

    return time_list, input_list


time_list, input_list = increment_by_2()
print(time_list)
print(input_list)
# print(find_collision(messages))
# print(messages)
