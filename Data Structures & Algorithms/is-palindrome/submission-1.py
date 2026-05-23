class Solution:
    def isPalindrome(self, s: str) -> bool:

        # brute force

        string_copy = ''
        for c in s:
            if c.isalnum():
                string_copy += c.lower()
        return string_copy[::-1] == string_copy
        