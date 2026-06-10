class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Brute force
        if len(s) != len(t):
            return False
        sorts=sorted(s)
        sortt=sorted(t)
        if sorts == sortt:
            return True
        return False
        