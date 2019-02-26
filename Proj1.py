import math


def fibGen(maxIndex):
    fibSeq = [0, 1]

    for i in range(2, maxIndex):
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


def gcdEuclidITER(m, n):
    if m > 1:
        count = 1
    else:
        count = 0
    if n == 0:
        return [m, count]
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
        if (m % divisor == 0) & (n % divisor == 0):
            count += 1
            return [divisor, count]
        divisor -= 1
        count += 1

def promptForMode():
    print("Please choose a mode:")
    print("0: User testing mode")
    print("1: Scatter plot mode")
    print("2: Exit")
    val = int(input())
    return val

def promptForTask():
    print("Plase choose task 1, 2, or 3 (4 to quit):")
    val = int(input())
    return val

def main():
    modeChoice = -1
    taskChoice = -1
    while (modeChoice < 0) | (modeChoice > 2):
        modeChoice = promptForMode()
    if (modeChoice == 2):
        return 0
    # User test mode
    elif (modeChoice == 0):
        taskChoice = 0
        while (taskChoice < 1) | (taskChoice > 4):
            taskChoice = promptForTask()
        if (taskChoice == 4):
            return 0
        # TODO
        elif (taskChoice == 1):
            print("User enters a single value of n; program outputs values of MDavg(n) and Davg(n).")
        # DONE
        elif (taskChoice == 2):
            k = int(input("Please enter a value for k: "))
            fib = fibGen(k + 2)
            m = fib[k + 1]
            n = fib[k]
            result = gcdEuclidITER(m, n)
            print("\nGCD(", m, ",", n, "):", result[0], "\n")
        # DONE
        elif (taskChoice == 3):
            m = int(input("Please enter a value for m: "))
            n = int(input("Please enter a value for n: "))
            result = gcdEuclidITER(m, n)
            print("\nGCD(", m, ",", n, "):", result[0], "\n")
        else:
            return 1
    # Scatter plot mode
    elif (modeChoice == 1):
        print("scatter")
    else:
        return 1

main()
