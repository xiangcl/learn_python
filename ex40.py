# -*- coding:utf-8 -*-

# 创建 cities 的字典
cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

# 在 cities 中添加元素
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):	# 创建一个find_city()的函数
	if state in themap:			# 对元素进行判断
		return themap[state]
	else:
		return "Not found."

# ok pay attention!
cities['_find'] = find_city		# 

while True:						# 使用while循环
	print "State? (ENTER to quit)",		# 打印字符提示
	state = raw_input("> ")
	if not state: break				# 如果state没有接受则跳出循环

	# this line is the most important ever! study!
	city_found = cities['_find'](cities, state)		# 调用find_city函数
	print city_found	# 打印结果
