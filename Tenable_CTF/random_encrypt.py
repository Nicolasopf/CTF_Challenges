#!/usr/bin/python3
import random
# Get dict of the output and the seed, so it iterate from every one
# And then prints the correct one


a = [209, 17, 111, 78, 180, 98, 205, 186, 202, 124, 139, 37, 57, 95, 47, 136, 114, 168, 139, 204, 165]
dic = [[22, 67, 142],[57, 51, 53],[97, 114, 14],[16, 94, 107],[187, 79, 172],[138, 138, 118],[32, 41, 8],[93, 104, 248],[112, 33, 215],[22, 163, 8],[170, 21, 156],[183, 196, 255],[62, 160, 64],[93, 124, 68],[53, 227, 187],[234, 44, 74],[96, 171, 138],[161, 46, 45],[186, 114, 154],[188, 137, 120],[239, 44, 13]]
dics = [set(item) for item in dic]
print(dics)

for num in range(len(a)):
    for i in range(10000):
        random.seed(i)
        rands = []
        for j in range(4):
            rands.append(random.randint(0,255))
        if dics[num].issubset(set(rands)):
            b = set(rands) - dics[num]
            try:
                print(chr(list(b)[-1]^a[num]), end="")
            except:
                pass
