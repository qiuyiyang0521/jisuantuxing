# -*- coding: utf-8 -*-
# @Author: qiuyiyang
# @Date: 2022-07-10 16:17:18
# @Email: 22133090041@qq.com
# @Last_modified_by: qiuyiyang
# @Last_modified_time: 2022-07-12 20:11:08

def a(x, y):
	if y == "a" or y == "边长":
		return x
	if y == "C" or y == "周长":
		return x / 4
	if y == "S" or y == "面积":
		return x ** 0.5
def C(x, y):
	if y == "a" or y == "边长":
		return x * 4
	if y == "C" or y == "周长":
		return x
	if y == "S" or y == "面积":
		return (x ** 0.5) * 4
def S(x, y):
	if y == "a" or y == "边长":
		return x ** 2
	if y == "C" or y == "周长":
		return (x / 4) * (x / 4)
	if y == "S" or y == "面积":
		return x
