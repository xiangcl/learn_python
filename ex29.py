# -*- coding:utf-8 -*-

# 定义三个变量，并分别赋值 
people = 20
cats = 30
dogs = 15

# 使用if语句进行条件判断,如满足条件则执行打印的语句
if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry!"

# 将dogs变量加5
dogs += 5

# 判断条件，如果条件满足，则打印满足条件的语句
if people >= dogs:
	print "People are greater than or equal dogs."

if people <= dogs:
	print "People are less than or equal to dogs."

if people == dogs:
	print "People are dogs."
