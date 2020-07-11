#!/usr/bin/env python3
import sys
#print("input two digits to calculate the sum")
#a = int(input())
#b = int(input())
input = sys.stdin.read()
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])
sum = a + b
print(sum)