#!/usr/bin/python3
import random
# Same as previous challenge, but more easy because you have the seed
# If you have the seed this is more easy because you dont have to check every time


seeds = [9925, 8861, 5738, 1649, 2696, 6926, 1839, 7825, 6434, 9699, 227, 7379, 9024, 817, 4022, 7129, 1096, 4149, 6147, 2966, 1027, 4350, 4272]
a = [184, 161, 235, 97, 140, 111, 84, 182, 162, 135, 76, 10, 69, 246, 195, 152, 133, 88, 229, 104, 111, 22, 39]

for i in range(len(seeds)):
    random.seed(seeds[i])
    rands = []
    for j in range(4):
        rands.append(random.randint(0,255))
    print(chr(rands[i%4]^a[i]), end="")
