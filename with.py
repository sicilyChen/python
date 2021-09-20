with open('a.txt','r') as file: 
    print(file.read())

'''文件的复制'''
with open('图6c.png','rb') as src_file:
    with open('copy2图6c.png','wb') as target_file: 
        target_file.write(src_file.read())