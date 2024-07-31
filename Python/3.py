'''
The prime factors of 13195$ are 5, 7, 13 and 29$.


'''

n = int(input("Enter the number: "))

d = 2

prime = []

while n > 1:
    while n % d == 0:
        prime.append(d)
        n = n // d

    d = d+1

print("Total prime numbers: ",set(prime))

print("largest prime number: ",max(prime))