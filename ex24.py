# -*- coding:utf-8 -*-

# 打印字符串以及格式化输出符
print "Let's practice everything."
print "You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs."

# 定义一段字符串以及格式化输出
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# 打印poem的内容
print "---------------"
print poem
print "---------------"

# 计算表达式的结果并将值赋给一个变量
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# 定义一个函数,计算一系列的值
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

# 调用secret_formula()，并传递值进去，将返回的值一次赋值给beans,jars,cartes
start_point = 10000
beans, jars, cartes = secret_formula(start_point)

# 打印一系列的值
print "With a staring point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, cartes)

# 计算
start_point = start_point / 10

# 调用secret_formula()计算
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
