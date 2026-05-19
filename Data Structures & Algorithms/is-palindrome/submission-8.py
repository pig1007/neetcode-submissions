class Solution:
    def isPalindrome(self, s: str) -> bool:
        slow = s.lower()
        i, j = 0, len(slow)-1
        while i < j:
            while i<j and not slow[i].isalnum():
                i+=1
            while i< j and not slow[j].isalnum():
                j-=1
            if slow[i] != slow[j]:
                return False
            i+=1
            j-=1
        return True