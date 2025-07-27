class Solution:
    def factorial(self, num):
        if num == 0 or num == 1:
            return 1
        fact = 1
        for i in range(2, num+1):
            fact *= i
        
        return fact

    def trailing_zeros_in_factorial_naive_solution(self, num):
        if num <= 4:
            return 0
        
        fact = self.factorial(num)

        zeros = 0
        while fact % 10 == 0:
            zeros +=1
            fact = fact//10

        return zeros

    def trailing_zeros_in_factorial(self, num):
        count = 0
        i= 5

        while i <= num:
            count += num // i
            i = i*5
        
        return count


result = Solution()

print(result.factorial(5))

print(result.trailing_zeros_in_factorial(10))