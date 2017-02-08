# -*- coding:utf-8 -*-

# 将sys模块import进来
from sys import argv

# 将argv解包，并将所有的参数依次赋给左边的变量
a, b, c = argv

print "这个脚本名是: ", a
print "你喜欢犀利哥么? ", b
# print "你喜欢我么? ", c

# 通过 raw_input 给变量c赋新值
c = raw_input ("你真的喜欢凤姐么? ")

print "是的，我真的%s" %(c)

