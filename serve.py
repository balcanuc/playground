#!/usr/bin/env python
print('Content-type: text/html\n')
print('<title>Hello World</title>')

for num in range(2, 5000):
    prime = True
    for i in range(2,num):
        if (num%i == 0):
            prime = False
    if prime:
       print(num)
# this is the second comment from csyi06
