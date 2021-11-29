"""
The sum of the squares of the first ten natural numbers is 1 ** 2 + 2 ** 2 + ... 10 ** 2 = 385.
The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10) ** 2 = 55 ** 2 = 3025.
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

n = 100
sum_sq = 0
for i in range(1, n+1):
    sum_sq += i ** 2

sq_sum = ((n + 1) * n / 2) ** 2

diff_sum = int(sq_sum - sum_sq)

print(f'Difference sum = {diff_sum}')
