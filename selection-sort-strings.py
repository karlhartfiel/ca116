#!/usr/bin/env python3

a = []

s = input()
while s != "end":
    a.append(s)
    s = input()

i = 0
while i < len(a):
    p = i
    j = p + 1
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j = j + 1

    tmp = a[i]
    a[i] = a[p]
    a[p] = tmp
    i = i + 1

i = 0
while i < len(a):
    print(a[i])
    i = i + 1
