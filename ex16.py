# -*- coding:utf-8 -*-

# 引入 sys 模块的argv列表
from sys import argv

# 将argv解包后的参数依次赋给左边的变量
script, filename = argv

# 打印字符串以及 变量filename
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# 打印提示符 ? ,并接收用户输入
raw_input("?")

print "Opening the file..."
target = open(filename, 'w')	# 以写的方式打开文件，并赋值给左边的变量

print "Truncating the file. Goodbye!"
target.truncate()	# 清空文件

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")	# 给出提示符，并接收用户输入，将输入结果赋值给左边的变量
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# 将用户输入的值写入到文件内
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()	# 关闭文件
