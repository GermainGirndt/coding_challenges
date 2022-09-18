
# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        print(f"Running with string '{s}'")
        
        chars_seen = {}
        max_length = start = 0
        for index, char in enumerate(s):
            print("Chars seen: ")
            print(chars_seen)
            print("Max Length: ")
            print(max_length)
            print("Start: ")
            print(start)

            print(f"Index: {index} | Current char {char}")

            if char in chars_seen and start <= chars_seen[char]:
                start = chars_seen[char] + 1
            else:
                max_length = max(max_length, index - start + 1)

            chars_seen[char] = index

            print("--------")


        return max_length


#Solution().lengthOfLongestSubstring("ABCDADBDAB")

