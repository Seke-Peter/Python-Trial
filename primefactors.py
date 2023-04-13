# def findPrimeFactors(num, isPrime):
#     arr = []
#     for i in range(2, num):
#         isPrime
#         if num % i == 0:
#             isPrime = True
#
#     for j in range(2, i):
#         if i % j == 0:
#             isPrime == False
#
#             if isPrime != False:
#                 pass
#             else:
#                 arr.add(i)
#         return arr.length

count = 0
n = int(input("Enter a number "))

for i in range(1, n + 1):
    if n % 1 == 0:
        count += 1
if count == 2:
    print(n, "is a prime number")
else:
    print(n, "is not a Prime number")