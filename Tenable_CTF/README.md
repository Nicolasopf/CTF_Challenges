# Tenable CTF - February 21 - Just one day of the CTF doing challenges


## Random encryption file:

```c
import random
flag = "flag{n0t_that_r4ndom}"
seeds = []
for i in range(0,len(flag)):
    seeds.append(random.randint(0,10000))

res = []
for i in range(0, len(flag)):
    random.seed(seeds[i])
    rands = []
    for j in range(0,4):
        rands.append(random.randint(0,255))

    res.append(ord(flag[i]) ^ rands[i%4])
    del rands[i%4]
    print(str(rands))

print(res)
print(seeds)
```

Example execution:
```c
[22, 67, 142]
[57, 51, 53]
[97, 114, 14]
[16, 94, 107]
[187, 79, 172]
[138, 138, 118]
[32, 41, 8]
[93, 104, 248]
[112, 33, 215]
[22, 163, 8]
[170, 21, 156]
[183, 196, 255]
[62, 160, 64]
[93, 124, 68]
[53, 227, 187]
[234, 44, 74]
[96, 171, 138]
[161, 46, 45]
[186, 114, 154]
[188, 137, 120]
[239, 44, 13]
[209, 17, 111, 78, 180, 98, 205, 186, 202, 124, 139, 37, 57, 95, 47, 136, 114, 168, 139, 204, 165]
```


## Random encryption fix file
We found the following file on a hacked terminal:

```c
import random
flag = "flag{not_the_flag}"
seeds = []
for i in range(0,len(flag)):
    seeds.append(random.randint(0,10000))

res = []
for i in range(0, len(flag)):
    random.seed(seeds[i])
    rands = []
    for j in range(0,4):
        rands.append(random.randint(0,255))

    res.append(ord(flag[i]) ^ rands[i%4])
    del rands[i%4]
    print(str(rands))

print(res)
print(seeds)
```
We also found sample output from a previous run:
```c
[249, 182, 79]
[136, 198, 95]
[159, 167, 6]
[223, 136, 101]
[66, 27, 77]
[213, 234, 239]
[25, 36, 53]
[89, 113, 149]
[65, 127, 119]
[50, 63, 147]
[204, 189, 228]
[228, 229, 4]
[64, 12, 191]
[65, 176, 96]
[185, 52, 207]
[37, 24, 110]
[62, 213, 244]
[141, 59, 81]
[166, 50, 189]
[228, 5, 16]
[59, 42, 251]
[180, 239, 144]
[13, 209, 132]
[184, 161, 235, 97, 140, 111, 84, 182, 162, 135, 76, 10, 69, 246, 195, 152, 133, 88, 229, 104, 111, 22, 39]
[9925, 8861, 5738, 1649, 2696, 6926, 1839, 7825, 6434, 9699, 227, 7379, 9024, 817, 4022, 7129, 1096, 4149, 6147, 2966, 1027, 4350, 4272]
```
