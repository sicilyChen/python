file=open('d.txt','w') #文件的写入
file.write('hello')
file1=open('d.txt','a')#在文件中追加'world'
file1.write('world')
file1.flush()#把缓冲区的内容写入文件，但不关闭文件
file1.write('python')
file1.close