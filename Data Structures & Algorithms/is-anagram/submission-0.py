class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        COUNTS,COUNTT={},{}

        for i in range(len(s)):
            COUNTS[s[i]] = COUNTS.get(s[i],0)+1
            COUNTT[t[i]] = COUNTT.get(t[i],0)+1
        
        for j in COUNTS:
            if COUNTS[j]!=COUNTT.get(j,0):
                return False
        return True