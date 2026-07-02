class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False

        dict1 = {}
        dict2 = {}

        # Count frequency of characters in s
        for ch in s:
            if ch in dict1:
                dict1[ch] += 1
            else:
                dict1[ch] = 1

        # Count frequency of characters in t
        for ch in t:
            if ch in dict2:
                dict2[ch] += 1
            else:
                dict2[ch] = 1

        # Compare the two dictionaries
        return dict1 == dict2