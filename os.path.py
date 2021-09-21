import os.path
print(os.path.abspath('hello.py'))#用于获取文件或目录的绝对路径
print(os.path.exists('hello.py'),os.path.exists('1.py'))#用于判断文件或目录是否存在，如果存在返回True,否则返回False
print(os.path.join('D:\\python程序练习','hello.py'))#将目录与目录或者文件名拼接起来
print(os.path.split('D:\\python程序练习\\hello.py'))#文件名和扩展名
print(os.path.basename('D:\\python程序练习\\hello.py'))#分离文件名和扩展名
print(os.path.dirname('D:\\python程序练习\\hello.py'))#从一个路径中提取文件路径，不包括文件名
print(os.path.isdir('D:\\python程序练习\\hello.py'))#用于判断是否为路径