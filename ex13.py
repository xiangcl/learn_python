# -*- coding:utf-8 -*-

from sys import argv	# 导入 sys 模块

script, first, second, third = argv		# 将argv 进行unpack,并将参数赋予左边的变量名

# 打印字符串以及变量
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
