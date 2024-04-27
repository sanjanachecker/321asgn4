from hashlib import sha256


def sha_hash(input):
    hash = sha256(input.encode())
    hx = hash.hexdigest()
    print('hx: ', hx)


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


hamming_dist("hello", "helln")
hamming_dist("world", "worle")
