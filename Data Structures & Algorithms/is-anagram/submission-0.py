class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_count = {}
        t_char_count = {}

        # initialise dictionary
        for char in s: 
            s_char_count[char] = 0
        for char in t:
            t_char_count[char] = 0

        # record chars
        for char in s:
            s_char_count[char] = s_char_count[char] + 1
        for char in t:
            t_char_count[char] = t_char_count[char] + 1

        if s_char_count == t_char_count:
            return True
        else:
            return False