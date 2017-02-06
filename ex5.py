# -*- coding: utf-8 -*-
# 将名字赋值给变量name
name = '向常乐'
# 将年龄 35 赋值给变量 age
age = 18 # not a lie
# 将 74 赋值给变量 height
height = 67 * 2.54 # inches 将英寸转化为厘米
# 将 180 赋值给变量 weight
weight = 132 * 0.4536 # lbs 将磅转化为千克
# 将 'Blue' 赋值给变量eyes
eyes = 'black'
# 将 'White' 赋值给变量 teeth
teeth = 'White'
# 将 'Broen' 赋值给变量hair
hair = 'Black'

# 打印文本，并格式化字符输出变量name
print "Let's talk about %s." % name
# 打印文本，并格式化整数输出变量height
print "He's %d inches tall." % height
# 打印文本，并格式化字符串输出变量weight
print "He's %s pounds heavy." % weight
# 打印文本
print "Actually that's not too heavy."
# 打印文本，并格式化字符串输出变量eyes，hair
print "He's got %s eyes and %s hair." %  (eyes, hair)
# 打印文本，并格式化字符串输出变量teeth
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(age, height, weight, age + height + weight)
