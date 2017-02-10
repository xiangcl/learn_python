 # -*- coding:utf-8 -*-

# 定义函数，用于指定分隔符对字符串进行切片；split(' ')指定空格为分割符对字符串进行分割
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

# 定义sort_words()函数，使用sorted()进行排序
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

# 定义print_first_word()函数，使用pop()函数移除列表中的第一个元素，并返回改值
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word

# 定义print_last_word()函数，使用pop()函数移除列表中的倒数第一个元素，并返回该值
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word

# 定义sort_sentence()函数，经上面的函数处理后返回值 
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the fitst and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
