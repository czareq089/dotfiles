import random
s = input()
a = "abcdefghijklmnopqrstuvwxyz"


for i in s:
      s[i] == a[random.random(len(a))]

print(s)