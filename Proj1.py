import math
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import random



def fibGen(maxIndex):
    fibSeq = [0, 1]
    for i in range(2, maxIndex + 1):
        fibSeq.append(fibSeq[i - 1] + fibSeq[i - 2])
    return fibSeq


def sieveOfEra(k):
    A = [True for i in range(k + 1)]
    # print (A)
    p = 2
    while p * p <= k:
        if A[p]:
            for i in range(p * p, k + 1, p):
                A[i] = False
        p += 1
    prime = []
    for i in range(2, len(A)):
        if A[i]:
            prime.append(i)
    return prime

def gcdByMiddleSchool(m, n):
    mf = middleSchoolPrimeFactors(m)
    nf = middleSchoolPrimeFactors(n)
    if len(mf) > len(nf):
        leastFactors = nf
        mostFactors = mf
    else:
        leastFactors = mf
        mostFactors = nf
    commonPrimeFactors = []
    i = j = 0
    operations = 0
    sum = 1
    while (i < len(leastFactors)) & (j < len(mostFactors)):
        operations += 1
        if leastFactors[i] == mostFactors[j]:
            sum *= leastFactors[i]
            i += 1
            j += 1
        else:
            j += 1
        
    return [sum, operations, len(mostFactors)]

def middleSchoolPrimeFactors(m):
    primeNums = sieveOfEra(m)
    primeFactors = []
    primeIndex = 0
    while m > 1:
        if m % primeNums[primeIndex] == 0:
            m = m / primeNums[primeIndex]
            primeFactors.append(primeNums[primeIndex])
        else:
            primeIndex += 1
    return primeFactors

def gcdEuclid(m, n, count):
    if m == 0:
        return [n, count - 1]
    return gcdEuclid(n % m, m, count + 1)

def timeAvgConc(n):
    sum = 0
    m = 1
    while m <= n:
        start = timer()
        gcdConsecInter(n,m)
        end = timer()
        sum += (end - start)
        m += 1
    return sum/n

def avgConsecutive(n):
    sum = 0
    m = 1
    while m <= n:
        sum += gcdConsecInter(n,m)[1]
        m += 1
    return sum/n

def worstConsectutive(k):
    sum = 0
    fibSeq = fibGen(k)
    for i in range(1, k):
        sum += gcdConsecInter(fibSeq[i+1], fibSeq[i])[1]
    return sum/k

def worstEuclid(k):
    sum = 0
    fibSeq = fibGen(k)
    for i in range(1, k):
        sum += gcdEuclidITER(fibSeq[i+1], fibSeq[i])[1]
    return sum/k

def timeAvgEuclid(n):
    start = timer()
    avgEuclid(n)
    end = timer()
    return end-start

def avgEuclid(n):
    sum = 0
    m = 1
    while m <= n:
        sum += gcdEuclidITER(n,m)[1]
        m += 1
    return sum/n

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
        count += 1
        if (m % divisor == 0):
            count += 1
            if (n % divisor == 0):
                return [divisor, count]
        divisor -= 1

def promptForMode():
    print("Please choose a mode:")
    print("0: User testing mode")
    print("1: Scatter plot mode")
    print("2: Exit")
    val = int(input())
    return val

def promptForTask():
    print("Plase choose a task:")
    print("1: average-case efficiency of Euclid's algorithm and Consecutive integer checking algorithm")
    print("2: worst-case efficiency of Euclid's algorithm")
    print("3: 'Middle-school procedure' for computing the GCD")
    print("4: exit")
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
        # DONE
        elif (taskChoice == 1):
            n = int(input("Please enter a value for n: "))
            md = avgEuclid(n)
            d = avgConsecutive(n)
            print("\nMD:", md)
            print("D:", d)
        # DONE
        elif (taskChoice == 2):
            k = int(input("Please enter a value for k: "))
            md = worstEuclid(k)
            d = worstConsectutive(k)
            print("\nMD:", md)
            print("\nD:", d)

            
            #  fib = fibGen(k + 2)
            # m = fib[k + 1]
            # n = fib[k]
            # result = gcdEuclidITER(m, n)
        # TODO: Middle school division
        elif (taskChoice == 3):
            m = int(input("Please enter a value for m: "))
            n = int(input("Please enter a value for n: "))
            result = gcdByMiddleSchool(m, n)[0]
            print("\nGCD(", m, ",", n, "):", result, "\n")
        else:
            return 1
    # Scatter plot mode
    elif (modeChoice == 1):
        taskChoice = 0
        while (taskChoice < 1) | (taskChoice > 4):
            taskChoice = promptForTask()
        if (taskChoice == 4):
            return 0
        # TODO
        elif (taskChoice == 1):
            mdvalues = []
            mdresults = []
            for i in range(0, 50):
                n = random.randint(1,51)
                result = avgEuclid(n)
                mdvalues.append(n)
                mdresults.append(result)
            dvalues = []
            dresults = []
            for i in range(0, 50):
                n = random.randint(1,51)
                result = avgConsecutive(n)
                dvalues.append(n)
                dresults.append(result)
            mdmatrix = (mdvalues, mdresults)
            dmatrix = (dvalues, dresults)
            data = (mdmatrix, dmatrix)
            colors = ('blue', 'green')
            groups = ('euclid', 'consecutive')
            # fig = plt.figure()
            for data, color, group in zip(data, colors, groups):
                x, y = data
                plt.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
            plt.title('Euclid\'s vs Consecutive')
            plt.legend(loc=2)
            plt.show()
        elif (taskChoice == 2):
            # fibs = fibGen(200)
            values = []
            results = []
            for i in range(0, 199):
                n = random.randint(1,200)
                result = worstEuclid(n)
                values.append(n)
                results.append(result)
            plt.scatter(values, results, alpha=0.5)
            plt.title('Euclid\'s (Worst Case)')
            plt.show()
        elif (taskChoice == 3):
            # Complexity of middlechool gcd
            values = []
            results = []
            for i in range(0, 999):
                m = random.randint(1,999)
                # m *= 3
                n = random.randint(1,999)
                # n *= 8
                result = gcdByMiddleSchool(m, n)
                values.append(result[2])
                results.append(result[1])
            plt.scatter(values, results, alpha=0.5)
            plt.title('Middle School Complexity')
            plt.show()
        else:
            return 1
    else:
        return 1

main()
