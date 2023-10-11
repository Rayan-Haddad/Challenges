class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            l = str(x)
            xx = l[0:(len(l)//2)]
            xxx = l[((len(l)+1)//2):]
            fx = xxx[::-1]
            if xx == fx:
                return True
            else:
                return False       
