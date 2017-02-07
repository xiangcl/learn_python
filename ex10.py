# -*- coding:utf-8 -*-
# 第一种方法
print "I am 6'2\" tall."	# 将字符中的双引号转义
print 'I am 6\'2" tall.'	# 将字符中的单引号转义


# 第二种方法
tabby_cat = "\t I'm tabbed in."		# 将tab转义
persian_cat = "I'm split\non a line."	# 转义换行
backslash_cat = "I'm \\ a \\ cat."	# 将 \ 转义

# 使用三引号输出，用了tab以及换行的转义
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# 打印变量
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
