#first solution just compares the strings
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


#solution could potentially use a hashmap
class Solution:
    def isansagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] == 0:
                del count[char]
                
        return len(count) == 0

#used knowledge gained from two sum and created a hashmap. Providing a wrong answer, will try again later