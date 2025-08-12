import math

def main():
    print("Position of Right Most Set Bit")

    print(f"Position of right most bit of 40 is {right_most_set_bit(40)}")


def right_most_set_bit(num):
    result = num ^ (num & num -1)

    return int(math.log(result, 2) + 1)

if __name__ == "__main__":
    main()