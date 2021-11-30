"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

for i in range(1, 1000):
    for j in range(i+1, 1000):
        k = 1000 - i - j
        if i ** 2 + j ** 2 == k ** 2:
            break
    if i ** 2 + j ** 2 == k ** 2:
        break

print(f'product is {i * j * k}')
print(f'a = {i}, b = {j}, c = {k}')
