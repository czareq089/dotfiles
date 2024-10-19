import random
s = input()
n = int(input())
a = "degklmnopqrstuvwxyz"
ns = ""

for i in range (0, n):
    for j in range (0, len(s)):
      ns += a[random.randint(0, len(a)) - 1]
    print(ns)
    ns = ""

