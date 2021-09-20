file=open('a.txt','r')
#print(file.read()) 从文件中读取size个字符或字节的内容返回，若省略[size],则读取到文件末尾，即一次读取文件所有内容
#print(file.readline())把文本文件中每一行都作为独立的字符串对象，并将这些对象放入列表返回
print(file.readlines())#把文本文件中每一行都作为独立的字符串对象，并将这些对象放入列表返回
print('---------------------')
file1=open('d.txt','r')
'''file1.write('hello')#将字符串str内容写入文件
lst=['java','go','python']
file1.writelines(lst)#将字符串列表s_list写入文本文件，不添加换行符'''
 
print('-------------')
file1.seek(2)#seek(offset[,whence])(把文件指针移动到新的位置，offset表示相对于whence的位置；offset:为正往结束方向移动，为负往开始方向移动
#whence不同的值代表不同含义:0:从文件头开始计算（默认值）1：从当前位置开始计算；2：从文件尾开始计算
print(file1.read())
print(file1.tell())#返回文件指针的当前位置
file1.close()