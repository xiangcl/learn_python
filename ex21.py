# -*- coding:utf-8 -*-

# 定义一个add()的函数,函数返回a+b的值
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

# 定义一个subtract()的函数，函数返回a - b的值
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

# 定义一个multiply()的函数，函数返回a * b的值
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

# 定一个divide()的函数,函数返回a/b的值
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

# 打印字符串
print "Let's do some math with just function!"

# 调用各个函数并传递参数进去
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100,2)

# 打印函数计算后的结果
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# 循环调用了函数的返回值
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it  by hand?"
