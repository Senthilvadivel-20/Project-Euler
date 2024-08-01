'''
Auth: Senthil
Date: 01/08/2024

How to reverse the numbers

'''

n = 10001

rev = 0

temp = n

while temp != 0:
    rev = rev * 10 + temp % 10
    # print(rev)
    temp = temp // 10

if rev == n:
    print("Number is Palindrome")
else:
    print('Number is not a Palindrome')