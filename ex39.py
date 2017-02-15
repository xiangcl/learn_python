# -*- coding: utf-8 -*-

# create a mapping of state to abbreviation
# 定义一个 states 的字典
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states and some citres in them
# 定义一个 cities 的字典
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
# 往cities字典中添加元素
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print our some cities
print '-' * 10
print "NY State has: ", cities['NY']	# 打印cities字典中 NY 元素对应的键值
print "OR State has: ", cities['OR']	# 打印cities字典中 OR 元素对应的键值

# print some states
print '-' * 10
print "Michigan's abbrebiation is: ", states['Michigan']	# 打印states字典中对应的 Michigan 对应的键值
print "Florida's abbreviation is: ", states['Florida']	# 打印states字典中对应的 Florida 对应的键值

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]	# 打印cities字典中对应的states字典中对应的Michigan键值
print "Florida has: ", cities[states['Florida']]	# 打印cities字典中对应的states字典中对应的Florida对应的键值

# print every state abberviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbrebviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that mighi not be there
sate = states.get('Texas')

if not state:
	print "Sorry, no Texas."

# get a city with a dafault value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is : %s" % city
