'''一、使用print方式输出（输出的目的地是文件）'''
fp=open('d:/test.txt','w')
print('奋斗成就更好的自己',file=fp)
fp.close()

'''二、使用文件读写操作'''
with open('d:/test1.txt','w') as file: 
    file.write('奋斗成就更好的自己')