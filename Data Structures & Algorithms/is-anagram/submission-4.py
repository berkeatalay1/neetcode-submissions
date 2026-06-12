class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myHash = {}

        for i in s:
            myHash[i] = myHash.get(i, 0) + 1

        for i in t:
            if i not in myHash:
                return False
            else:
                myHash[i] -= 1
                if myHash[i] < 0:
                    return False
        
        for k,v in myHash.items():
            if v != 0:
                return False
        
        return True