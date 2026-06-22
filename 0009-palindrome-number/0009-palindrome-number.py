class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        s=str(x)
        i = 0
        j = len(s)-1
        ans = True
        while i < j and j > i:
            if(s[i]==s[j]):
                i+=1
                j-=1
            elif(s[i]!=s[j]):
                ans = False
                break
        return ans