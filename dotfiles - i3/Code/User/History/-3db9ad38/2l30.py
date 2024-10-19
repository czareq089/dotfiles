import random
s = input()
a = "abcdefghijklmnopqrstuvwxyz"


for i in s:
      s[i] == a[random.randint(0, len(a))]

print(s)