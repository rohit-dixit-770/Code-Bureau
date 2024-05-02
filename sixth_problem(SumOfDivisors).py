# method 1

# def sumOfDivisorOfNum(n):
#     sum = 0
#     for i in range(1, int(n**(1/2)) + 1):
#         if n % i == 0:
#             sum+=i
#             if i != n // i:
#                 sum+=(n // i)
#     return (sum)
# def sumOfAllDivisors(n: int) -> int:
#     sum=0
#     for i in range(1,n+1):sum+=sumOfDivisorOfNum(i)
#     return (sum)


# method 2

def sumOfAllDivisors(n: int) -> int:
    sum=0
    for i in range(1,n+1):sum+=((n//i) *i)
    return (sum)
