# -*- coding:utf-8 -*-

# 定义三个变量，并赋初始值
people = 30
cars = 40
trucks = 15
home = 30

# 进行if else条件判断
if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
elif home > trucks:
	print "home大于trucks"
else:
	print "We can't decide."

if trucks > cars:
	print "	That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."

if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, Let's stay home then."
