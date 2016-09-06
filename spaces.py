#!/usr/local/bin/python

import os

string = str(input("String: "))
multiplier = input("Multiplier:")
iter_string = range(len(string))
new_string = ""

if string == "":
	"Empty string given"

for i in iter_string:
	new_string += string[i]
	if i != iter_string[-1]:
		if string[i] != " ":
			if string[i+1] != " ":
				new_string += (" "  * multiplier)
		else: 
			new_string += ("  " * multiplier)

os.system("echo '%s' | pbcopy" % new_string)


		