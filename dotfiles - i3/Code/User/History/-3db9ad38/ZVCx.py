import random
s = input()
a = "abcdefghijklmnopqrstuvwxyz"
ns = ""

for i in s:
      ns += a[random.randint(0, len(a))]

print(ns)