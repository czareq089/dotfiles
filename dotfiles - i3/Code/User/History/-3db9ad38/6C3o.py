import random
s = input()
n = int(input())
a = "abcdefghijklmnopqrstuvwxyz"
ns = ""

for i in range (0, n):
    for j in range (0, len(s)):
      ns += a[random.randint(0, len(a))]
    print(ns)
    ns = ""

