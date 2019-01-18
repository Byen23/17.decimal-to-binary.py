# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17, 2019

File: decimaltobinary.py
Converts a decimal integer to a string of bits.
@author: Byen23
"""
# This is to be my 17th progrm to be uploaded to github.

decimal = int(input("Enter a decimal integer: "))
if decimal == 0:
	print(0)
else:
	print("Quotient Remainder BInary")
	bitString = ""
	while decimal > 0:
		remainder = decimal % 2 
		decimal = decimal // 2
		bitString = str(remainder) + bitString
		print("%5d%8d%12s" % (decimal, remainder, bitString))
print("The binary representation is", bitString)

