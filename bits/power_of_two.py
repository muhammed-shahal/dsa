class Solution(object):
    def is_power_of_two(self, n):
        """
        :type n: int
        :rtype: bool
        """

        count = 0

        while n != 0 and count <= 1:
            n = n & n-1
            count +=1
        
        if count == 1:
            return True
        
        return False
    
    def is_power_of_two_optimal(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 0:
            return False
        
        return n & n-1 == 0