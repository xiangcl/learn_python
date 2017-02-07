# -*- coding:utf-8 -*-
# 定义变量，并使用格式化输出
formatter = "%r %r %r %r"

# 打印数字格式化输出
print formatter % (1, 2, 3, 4)
# 打印文字格式化输出
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
# 调用自身输出
print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.", # 当碰到双引号内部有单引号时，%r 会格式化输出单引号为双引号
	"So I said goodnight."
)
