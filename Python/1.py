'''
Multiples of 3 or 5

Problem 1

If we list all the natural numbers below that are multiples of or , we get and . The sum of these multiples is


Find the sum of all the multiples of
or below .

'''

res = 0

for i in range(0, 1000):
    if (i%3)==0 or (i%5)==0:
        res+=i

print(res)