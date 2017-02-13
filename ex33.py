# -*- coding:utf-8 -*-

# 定义一个变量i，并赋0给它。再定义一个空的序列
i = 0
numbers = []

# 定义一个while循环
while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)	# 在numbers[]列表后面添加新的对象

	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num
