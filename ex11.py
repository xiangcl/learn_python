# -*- coding:utf-8 -*-

print "How old are you?",	# 打印字符串
age = raw_input()	# 定义变量，并将输入的值赋给变量
print "How tall are you?",	# 打印字符串
height = raw_input()	# 定义变量，并将输入的值赋给变量
print "How much do you weight?",	# 打印字符串
weight = raw_input()	# 定义变量，并将输入的值赋给变量

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)	# 打印字符串，并使用 %r 输出格式化变量的字符
