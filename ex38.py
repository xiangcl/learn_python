# -*- coding:utf-8 -*-

# 定义一个变量，并赋值字符串
ten_things = "Apples Oranges Crows Telephone Light Sugar"

# 打印字符串提示
print "Wait there are not 10 things in that list. Let's fix that."

# 将ten_things变量里的字符串进行分割，然后赋值给变量stuff
stuff = ten_things.split(' ')	# 指定空白为分割符对字符串进行分割
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]	# 定义一个列表，并赋值给变量more_stuff

# while循环，循环的条件判断stuff的元素长度不为10，为10则跳出循环 
while len(stuff) != 10:
	next_one = more_stuff.pop()	# 移除more_stuff[]列表中的最后一个元素，并将移除的元素赋值给next_one
	print "Adding: ", next_one	# 打印next_one的值
	stuff.append(next_one)	# 将next_one的结果添加的stuff列表的末尾
	print "There are %d items now." % len(stuff)	# 打印添加元素后stuff列表元素的个数

print "There we go: ", stuff	# 打印添加元素后的stuff列表

print "Let's do some things with stuff."

print stuff[1]	# 打印stuff[]列表中的第2个元素
print stuff[-1] # whoa! fancy	# 打印stuff[]重的倒数第一个元素
print stuff.pop()	# 移除stuff[]列表中的最后一个元素，并打印之
print ' '.join(stuff) # what? cool!	# 将stuff[]序列中的元素以空格隔开组成新的序列打印
print '#'.join(stuff[3:5]) # super stellar!	# 将stuff的序列中的元素以#为分割组成新的序列并打印
