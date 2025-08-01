def main():
    print("Divisors of a Number")

    print("Divisors of 20")
    divisors_naive(20)

    print("Divisors of 40")
    divisors(40)

    print("Divisors of 40 in order")
    divisors_in_order(40)

# O(n) complexity
def divisors_naive(num):
    for i in range(1, num+1):
        if num % i == 0:
            print(i)
"""
The optimal soln is to use following observations
1. The divisors comes in pair, eg 40 -> (1, 40), (2,20) etc
2. The first elem in the divisor (a, b) pair is <= second, so we can say a <= sqrt(n)
That means loop only until sqrt(n) to get the first divisors
3. Using first divisor find the second divisor as follows -> a * b = n
"""
def divisors(num):
    i = 1

    while i * i <= num:
        if num % i == 0:
            print(i)
            if num // i != i:
                print(num//i)
        
        i +=1

def divisors_in_order(num):
    i = 1

    while i * i <= num:
        if num % i == 0:
            print(i)
        i+=1
    
    while i >= 1:
        if num % i == 0 and num // i != i:
            print(num // i)
        i-=1


if __name__ == "__main__":
    main()