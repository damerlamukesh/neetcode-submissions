class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Optimal
        if len(s) != len(t):
            return False
        
        #iterate S and Count the instances
        hashmap={}
        for ch in s:
            if ch in hashmap:
                hashmap[ch] += 1
            else:
                hashmap[ch]=1
        
        # iterate t and think all the cases
        for ch in t:
            if ch not in hashmap:
                return False
            #on every match -1
            hashmap[ch]-=1
            #count od ch is less than 0 return false
            if hashmap[ch] < 0:
                return False
            
        return True


        