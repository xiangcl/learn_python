# -*- coding:utf-8 -*-

from sys import argv	# 将sys模块import

script, user_name = argv	# 将argv中的东西解包，将所有的参数依次赋予左边的变量名
prompt = '>  '	# 定义提示符变量

print "Hi %s, I'm the %s script." % (user_name, script)		# 打印字符串
print "I'd like to ask you a few questions."	# 打印字符串
print "Do you like me %s?" % user_name	# 打印字符串
likes = raw_input(prompt)	# 根据上面的提问，给出提示符等待输入，将输入的结果赋值给变量likes

print "Where do you live %s?" % user_name	#打印字符串
lives = raw_input(prompt)	# 根据上面的问题，给出提示符等待用户输入，将输入的结果赋值给变量lives

print "What kind of computer do you have?"	# 打印字符串
computer = raw_input(prompt)	# 根据上面的问题，给出提示符等待用户输入，并将输入的结果赋值给变量computer

# 打印字符串以及格式化字符 %r 输出以上变量的内容
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
