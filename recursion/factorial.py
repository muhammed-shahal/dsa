class Solution:
    def factorial(self, num):
        if num == 0 or num == 1:
            return 1
        
        return num * self.factorial(num-1)

result = Solution()

print(result.factorial(5))