#prob 1 - sum of all multiples of 3 or 5 below 1000
"""
numbers = []
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        numbers.append(i)
print sum(numbers)
"""
#prob 2 - sum of even fibonacci numbers under 4mil starting at 1 & 2

"""
def fib_function(a, b):
    fibonacci = [a, b]
    while fibonacci[-1] <= 2000000:
        a = a + b
        fibonacci.append(a)
        b = b + a
        fibonacci.append(b)
    to_sum = []
    for item in fibonacci:
        if item % 2 == 0:
            to_sum.append(item)
    return sum(to_sum)
    
print fib_function(1, 2)
"""

#prob 6 - find the difference between the sum of the squares of 1-100
# and the square of the sums of 1-100
"""
square_of_sum = sum(range(1, 101)) ** 2
squares = []
for i in range(1, 101):
    i = i ** 2
    squares.append(i)
sum_of_squares = sum(squares)
print square_of_sum - sum_of_squares
"""

#problem 5 - find the smallest number that is evenly divisible by all
#numbers between 1 and 20
"""
def prob_five():
    number = 2520
    to_divide = [11, 13, 14, 16, 17, 18, 19]
    while True:
        if all(number % i == 0 for i in to_divide):
            return number
            break
        else:
            number = number + 20

print prob_five()
"""
#problem 3 - what is the largest prime factor of the number 600851475143? 
"""def is_it_prime(x):
    if x < 2:
        return False
    else:
        for num in range (2, x):
            if x % num == 0:
                return False
                break
        else:
            return True

def prime_list():
    primes = []
    for i in range(50000, 100000):
        if is_it_prime(i) and 600851475143 % i == 0:
            primes.append(i)
    return primes
            

print prime_list()
"""
#problem 4 - Find the largest palindrome made from the product of two 3-digit numbers.
def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False


def prob_four():
    x = 999
    y = 999
    if 
    return x, y, x*y



