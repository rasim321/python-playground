#!/usr/bin/env python
with open('name.txt') as f:
	my_name = f.read()

print(my_name)

with open('hello.txt', 'w') as f:
	f.write('Hello, my name is ' + str(my_name))

#Working with Inayat and Mia

