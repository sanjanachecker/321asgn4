import matplotlib.pyplot as plt

data = [
    ('bits', 'inputs'),
    (8, 2988),
    (10, 12731),
    (12, 10359),
    (14, 16276),
    (16, 12112),
    (18, 11401),
    (20, 12162),
    (22, 9176),
    (24, 16309),
    (26, 10728),
    (28, 11758),
    (30, 5638),
    (32, 1216),
    (34, 12586),
    (36, 11702),
    (38, 13741),
    (40, 16423),
    (42, 17810),
    (44, 7446),
    (46, 5431),
    (48, 16399)
]

# Separate the data into x and y values
x = [d[0] for d in data[1:]]
y = [d[1] for d in data[1:]]

plt.figure(figsize=(12, 6))
plt.plot(x, y, marker='o')
plt.xlabel(data[0][0])
plt.ylabel(data[0][1])
plt.title('Inputs vs Bits')
plt.grid(axis='y')
plt.show()
