def main():
    print("Palindrome")
    print("123 is palindrome", palindrome(123))
    print("121 is palindrome", palindrome(121))

def palindrome(n):
    reverse = 0
    num = n

    while num > 0:
        reverse = reverse * 10 + num%10
        num = num // 10
    
    return reverse == n

if __name__ == "__main__":
    main()