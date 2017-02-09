# -*- coding:utf-8 -*-

# 调用库
from sys import argv

# 解压argv的方法，并将argv的参数依次赋值给左边的变量
script, input_file = argv

# 定义一个函数;read():读取文件内容
def print_all(f):
	print f.read()

# 定义一个函数;seek():移动文件读取指针到指定位置
def rewind(f):
	f.seek(0)

# 定义一个函数;readline():读取每一行的内容
def print_a_line(line_count, f):
	print line_count, f.readline(),

# 打开文件
current_file = open(input_file)

print "First let's print the whole file:\n"

# 调用print_all函数
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# 调用rewind()函数
rewind(current_file)

print "Let's print three lines:"

# 给current_line赋初值，后面每调用一次print_a_line()函数，就使current_line加1
current_line = 1
print_a_line(current_line, current_file)

current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
