# -*- coding:utf-8 -*-

# 引入sys的argv，以及os.path的exists
from sys import argv
from os.path import exists	# 将文件名作为参数,如果文件存在的话返回True否则返回False

# 将 argv 解压缩，并依次赋值给左边的变量
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
input = open(from_file)		# 打开要赋值的文件,并赋值给变量
indata = input.read()	# 读取打开的文件,并赋值给左边的变量 

print "The input file is %d bytes long" % len(indata)	# 打印变量的长度

print "Does the output file exist? %r" % exists(to_file)	# 判断药品输出的文件是否存在
print "Ready, hit RETURN to continue, CTRL-C to abort." # 询问是否继续
raw_input()	# 读取用户的输入

output = open(to_file, 'w')	# 打开等待输入内容的文件，并开启写模式
output.write(indata)	# 将indate的内容写入

print "Alright, all done."

# 关闭打开的文件
output.close()
input.close()
