# -*- coding:utf-8 -*-

# 深入使用 raw_input
age = raw_input("How old are you? ")	# 括号中间加入的为提示信息
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")

# 打印字符串，并格式化输出变量
print "So, you'r %r old, %r tall and %r heavy." % (age, height, weight)
