class Solution(object):
    def isPalindrome(self, x):
        if x < 0: return False

        div = 1
        while x >= div * 10:
            div *= 10
        
        while x:
            right = x % 10
            left = x // div
            if left != right: return False

            x = x % div // 10
            #1234 % div = 234 // 10 = 23
            div = div // 100
            #div=1000, then now its 10
        return True