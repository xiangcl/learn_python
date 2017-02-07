# -*- coding:utf-8 -*-
# 定义变量 x ，并将字符串以及格式化整数赋值给变量x。
x = "There are %d types of people." % 10
# 定义变量 binary ，并将字符串 binary 赋值给变量 binary
binary = "binary"
# 定义变量do_not,并将字符串 don't 赋值给变量 do_not
do_not = "don't"
# 定义变量y，并将字符串以及格式化字符串赋值给变量y
y = "Those who know %s and those who %s." % (binary, do_not)

# 打印变量x
print x
# 打印变量y
print y

# 打印字符串以及格式化输出 
print "I said: %r." % x
# 打印字符串以及格式化字符串输出
print "I also said: '%s'." % y

# 定义变量hilarous，并将False赋值给变量
hilarous = False
# 定义变量joke_evaluation, 并赋值
joke_evaluation = "Isn't that joke so funny?! %r"

# 打印字符串
print joke_evaluation % hilarous

# 定义变量，并赋值字符串
w = "This is the left side of..."
# 定义变量，并赋值字符串
e = "a string with a right side."

# 打印变量 w 以及 e 的变量内容
print w + e
