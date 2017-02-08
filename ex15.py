# -*- coding:utf-8 -*-

# 从sys包中引入argv功能模块
from sys import argv

# 使用argv模块获取文件名
script, filename = argv

# 使用open()函数打开文件，创建一个file对象并赋值给txt变量
txt = open(filename)

# 打印字符串，以及 %r 
print "Here's your file %r:" % filename
print txt.read()	# 从打开的文件读取字符串并打印

# 打印字符串
print "Type the filename again:"
file_again = raw_input("> ")	# 获取文件名	

txt_again = open(file_again)	# 再次打开文件

print txt_again.read()	# 从打开的文件读取字符串并打印
