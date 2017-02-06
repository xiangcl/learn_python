# -*- coding:utf-8 -*-
# 定义变量 cars 并赋值100
cars = 100
# 定义变量 space_in_a_car ,并赋值4.0
space_in_a_car = 4.0
# 定义变量 drivers, 并赋值30
drivers = 30
# 定义变量passengers， 并赋值90
passengers = 90
# 定义变量cars_not_driven, 并将cars-drivers计算后的值赋给cars_not_driven
cars_not_driven = cars - drivers
# 将drivers的值赋给cars_driven
cars_driven = drivers
# 计算 cars_driven*space_in_a_car ,并将计算后的结果赋值给carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# 计算 passengers / cars_driven, 并将计算后的结果赋值给average_passengers
average_passengers_per_car = passengers / cars_driven

# 打印文本以及 cars 的值
print "There are", cars, "cars acailable."
# 打印文本以及 drivers 的值
print "There are only", drivers, "drivers avaliable."
# 打印文本以及 cars_not_driven 的值
print "There will be", cars_not_driven, "empty cars today."
# 打印文本以及 carpool_capacity 的值
print "We can transport", carpool_capacity, "people today."
# 打印文本以及 passengers 的值
print "We have", passengers,"to carpool today."
# 打印文本以及 average_passengers_per_car 的值
print "We need to put about", average_passengers_per_car, "in each car."
