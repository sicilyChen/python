import sys
import os
import re

class Solution:
    def partitionNumber(self, text):
        # Write Code Here 
        max_l = 0
        res = ""
        for i in range(0, len(text)):
            for j in range(i, len(text)):
                substring = s[i:j + 1]
                
                if substring == substring[::-1]:
                    # print substring, j + 1 - i, max_l
                    if max_l < j + 1 - i:
                        max_l = j + 1 - i
                        res = substring
                        
        return res

try:
    _text = input()
except:
    _text = None

  
s = Solution()
res = s.partitionNumber(_text)

print(str(res) + "\n")