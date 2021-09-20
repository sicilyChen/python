file=open('a.txt','r')
#print(file.read()) 从文件中读取size个字符或字节的内容返回，若省略[size],则读取到文件末尾，即一次读取文件所有内容
#print(file.readline())把文本文件中每一行都作为独立的字符串对象，并将这些对象放入列表返回
print(file.readlines())#把文本文件中每一行都作为独立的字符串对象，并将这些对象放入列表返回


