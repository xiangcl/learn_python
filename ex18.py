# -*- coding:utf-8 -*-

# this one is like your script with argv
def print_two(*args):	# 定义变量名为 print_two 的函数,并使用 * 将所有参数组织成一个列表放在args里
	arg1, arg2 = args	# 将args里的参数解包并依次赋值给左边的变量
	print "arg1: %r, arg2: %r" % (arg1, arg2)	# 打印变量

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):	# 定义变量并直接接收两个参数赋值给变量
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):	# 接受单个参数，并赋值给变量
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():	# 不接受参数
	print "I got nothin'."

print_two("Zed","Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
