import sys
import os
import re

class Solution:
    def partitionNumber(self, text):
        # Write Code Here 
        for i in range(1,len(text)):
            if text[:i]==text[len(text)-i:]:
                return 2+self.partitionNumber(text[i:len(text)-i])
            return 1 if text else 0

try:
    _text = input()
except:
    _text = None

  
s = Solution()
res = s.partitionNumber(_text)

print(str(res) + "\n")