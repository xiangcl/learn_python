# -*- coding:utf-8 -*-

# 定义列表
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
# 使用for循环打印the_count序列
for number in the_count:
	print "This is count %d" % number

# same as above
# 使用for循环打印fruits序列
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notive we have to use %r since we don't know what's in it
# 使用for循环打印change序列
for i in change:
	print "I got %r" % i

# we can also build lists, first start with an empty one
# 定义一个空序列
elements = []

# then use the range function to do 0 to 5 counts
# 定义for循环,range()循环生成一个数值的序列
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)	# 将i循环出来的内容添加到elements序列中

# now we can print them out too
# 定义for循环，打印elements序列
for i in elements:
	print "Element was: %d" % i
