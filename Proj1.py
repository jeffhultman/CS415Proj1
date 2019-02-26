import math


def fibGen(maxIndex):
    fibSeq = [0, 1]
    for i in range(2, maxIndex + 1):
        fibSeq.append(fibSeq[i - 1] + fibSeq[i - 2])
    return fibSeq


def sieveOfEra(k):
    A = [True for i in range(k)]
    # print (A)
    p = 2
    while p * p <= k:
        if A[p]:
            for i in range(p * p, k, p):
                A[i] = False
        p += 1
    # print(A)
    prime = []
    for i in range(2, len(A)):
        if A[i]:
            prime.append(i)
    # print(prime)
    return prime


def gcdEuclid(m, n, count):
    if m == 0:
        return [n, count - 1]
    return gcdEuclid(n % m, m, count + 1)

def avgConsecutive(m):
    sum = 0
    n = 1
    while n <= m:
        sum += gcdConsecInter(m,n)[1]
        n += 1
    return sum/m

def avgEuclid(m):
    sum = 0
    n = 1
    while n <= m:
        sum += gcdEuclidITER(m,n)[1]
        n += 1
    return sum/m

def gcdEuclidITER(m, n):
    if m > 1:
        count = 1
    else:
        count = 0
    if n == 0:
        return m
    while m % n != 0:
        temp = n
        n = m % n
        m = temp
        count += 1
    return [n, count]


def gcdConsecInter(m, n):
    divisor = n
    count = 0
    while divisor > 0:
        count += 1
        if (m % divisor == 0):
            count += 1
            if (n % divisor == 0):
                return [divisor, count]
        divisor -= 1


def main():
    print(avgConsecutive(23))
    #  print("Please enter index for Fibonacci Sequence: (At least 2)")
    # val = int(input())
    # while val < 3:
    #     print("Please enter index for Fibonacci Sequence: (At least 2)")
    #     val = int(input())
    # # fib = sieveOfEra(val)
    # fib = fibGen(val + 1)
    # print("gdc(", fib[val], ",", fib[val - 1], ")")
    # div = gcdEuclidITER(fib[val], fib[val - 1])
    # print("Iterative Euclid: ", div)
    # div2 = gcdEuclid(fib[val], fib[val - 1], 0)
    # print("Recursive Euclid: ", div2)
    # div3 = gcdConsecInter(fib[val], fib[val - 1])
    # print("Consecutive Integer: ", div3)


# main()
print(fibGen(6))
