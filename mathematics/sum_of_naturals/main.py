def main():
    print("Sum of naturals", sum_of_naturals(5))

def sum_of_naturals(n):
    return (n * (n + 1)) // 2

if __name__ == "__main__":
    main()