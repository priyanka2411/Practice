#!/usr/bin/env python3
import re
import operator
line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
st = re.search(r"ticky: INFO: ([\w ]*) ", line)
print(st)
line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
st1 = re.search(r"ticky: ERROR: ([\w ]*) ", line)
print(st1)
fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
#print(sorted(fruit.items()))
print(sorted(fruit.items(), key=operator.itemgetter(1),reverse=1))