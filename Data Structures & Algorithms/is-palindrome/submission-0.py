class Solution:
    def isPalindrome(self, s: str) -> bool:
        remove_spaces_str = ''

        for c in s:
            if c.isalnum():
                remove_spaces_str += c.lower()
        return remove_spaces_str == remove_spaces_str[::-1]
        