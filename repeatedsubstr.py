'''
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

#class Solution:
#    def lengthOfLongestSubstring(self, s: str) -> int:
import sys
s = sys.argv[1]    
def lengthOfLongestSubstring(s):
    count = 0
    def check(i, j):
        substr = set()
        for k in range(i, j+1):
            sub = s[k]
            if sub in substr:
                return False
            substr.add(sub)
            print(substr)
        return True


    for i in range(len(s)):
        for j in range(i, len(s)):
            if check(i, j):
                count = max(count, j - i+1)
                #print("substring: "+ substr)
            
    print(str(count))
    # print(str(substr))
    return count

if __name__ == "__main__":
    lengthOfLongestSubstring(s)



