# -*- coding: utf-8 -*-
"""Euler004
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

palindrome = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        number = i * j
        if str(number) == str(number)[::-1]:
            if number > palindrome:
                palindrome = number
                a = i
                b = j
            break
print(f'Palindromic number is {palindrome}')
print(f'number one = {a}; number two = {b}')
