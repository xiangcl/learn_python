# -*- coding:utf-8 -*-

# 定义名为 cheese_and_crackers 的函数，并接受两个参数
def cheese_and_crackers(cheese_count, boxes_of_crachers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crachers!" % boxes_of_crachers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# 调用函数是直接传递两个参数
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# 定义两个变量，并赋值
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# 调用函数，将变量传递给参数
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 调用函数，并将两个运算表达式传递给参数
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# 调用函数,并将两个变量值运算表达式作为参数传递给函数
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
	
