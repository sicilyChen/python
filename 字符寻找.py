def firstUniqChar(self, s):
    dic = {}
    for i in s:#i是字符
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] = dic[i] + 1
    for i in range(len(s)):#i是索引
        if dic[s[i]] == 1:
            return i
    return -1