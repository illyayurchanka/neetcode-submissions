class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        l, r = 0, 0

        unique_string = s[0]
        max_len = 0
        while r < len(s) - 1:
            r += 1
            if s[r] not in unique_string:
                unique_string += s[r]
            else:
                while l <= r:
                    l += 1
                    unique_string = s[l:r]
                    if s[r] not in unique_string:
                        unique_string += s[r]
                        break
                    else:
                        continue
            
            max_len = max(len(unique_string), max_len)
        return max_len

