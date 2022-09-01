# -*- coding: utf-8 -*-
# @Author: qiuyiyang
# @Date: 2022-07-10 10:52:41
# @Email: 22133090041@qq.com
# @Last_modified_by: qiuyiyang
# @Last_modified_time: 2022-07-17 12:22:37

def fenge(a=70):
	print("-"*a)
import sys
import os 
import time
sys.path.append("2D")
sys.path.append("3D")
from 圆 import rounds
from 三角形 import triangles
from 梯形 import trapezoidal
from 正方形 import square
from 长方形 import rectangular
from 平行四边形 import parallelogram
from 正方体 import zhengfangti
first = 0
while True:
	fenge()
	first = int(input("1 2D图形\n2 3D图形\n3 退出\n"))
	if first == 3:
		break
	if first == 1:
		fenge()
		second = int(input("1 三角形\n2 正方形\n3 长方形\n4 平行四边形\n5 梯形\n6 圆\n"))

		if second == 6:
			fenge()
			x = str(input("已知的部分："))
			num = float(input("已知的部分的数据："))
			print("|{:^4s}|{:^12.3f}|".format("半径", rounds.r(num,x)))
			print("|{:^4s}|{:^12.3f}|".format("直径", rounds.d(num,x)))
			print("|{:^4s}|{:^12.3f}|".format("周长", rounds.C(num,x)))
			print("|{:^4s}|{:^12.3f}|".format("面积", rounds.S(num,x)))
			time.sleep(1)

		if second == 1:
			fenge()
			print("请输入数据(如果变量是求的部分按“Enter”)")
			a = str(input("底："))
			h = str(input("高："))
			S = str(input("面积："))

			if a == "":
				h = float(h)
				S = float(S)
				print("|{:^5s}|{:^10.3f}|".format("底", triangles.a(h, S)))
				print("|{:^5s}|{:^10.3f}|".format("高", h))
				print("|{:^4s}|{:^10.3f}|".format("面积", S))
				time.sleep(1)

			if h == "":
				a = float(a)
				S = float(S)
				print("|{:^5s}|{:^10.3f}|".format("底", a))
				print("|{:^5s}|{:^10.3f}|".format("高", triangles.h(a, S)))
				print("|{:^4s}|{:^10.3f}|".format("面积", S))
				time.sleep(1)

			if S == "":
				a = float(a)
				h = float(h)
				print("|{:^5s}|{:^10.3f}|".format("底", a))
				print("|{:^5s}|{:^10.3f}|".format("高", h))
				print("|{:^4s}|{:^10.3f}|".format("面积", triangles.S(a, h)))
				time.sleep(1)

		if second == 2:
			fenge()
			x = str(input("已知的部分："))
			num = float(input("已知的部分的数据："))
			print("|{:^4s}|{:^12.3f}|".format("边长", square.a(num,x)))
			print("|{:^4s}|{:^12.3f}|".format("周长", square.C(num,x)))
			print("|{:^4s}|{:^12.3f}|".format("面积", square.S(num,x)))
			time.sleep(1)

		if second == 3:
			fenge()
			print("请输入数据(如果数据未知按“Enter”，目前只支持整数)")
			a = str(input("长："))
			b = str(input("宽："))
			C = str(input("周长："))
			S = str(input("面积："))

			if a != "" and b != "":
				a = int(a)
				b = int(b)
				print("|{:^5s}|{:^10d}|".format("长", rectangular.a(a, b, "a,b")))
				print("|{:^5s}|{:^10d}|".format("宽", rectangular.b(a, b, "a,b")))
				print("|{:^4s}|{:^10d}|".format("周长", rectangular.C(a, b, "a,b")))
				print("|{:^4s}|{:^10d}|".format("面积", rectangular.S(a, b, "a,b")))
				time.sleep(1)

			if a != "" and C != "":
				a = int(a)
				C = int(C)
				print("|{:^5s}|{:^10d}|".format("长", rectangular.a(a, C, "a,C")))
				print("|{:^5s}|{:^10d}|".format("宽", rectangular.b(a, C, "a,C")))
				print("|{:^4s}|{:^10d}|".format("周长", rectangular.C(a, C, "a,C")))
				print("|{:^4s}|{:^10d}|".format("面积", rectangular.S(a, C, "a,C")))
				time.sleep(1)

			if a != "" and S != "":
				a = int(a)
				S = int(S)
				print("|{:^5s}|{:^10d}|".format("长", rectangular.a(a, S, "a,S")))
				print("|{:^5s}|{:^10d}|".format("宽", rectangular.b(a, S, "a,S")))
				print("|{:^4s}|{:^10d}|".format("周长", rectangular.C(a, S, "a,S")))
				print("|{:^4s}|{:^10d}|".format("面积", rectangular.S(a, S, "a,S")))
				time.sleep(1)

			if b != "" and C != "":
				b = int(b)
				C = int(C)
				print("|{:^5s}|{:^10d}|".format("长", rectangular.a(b, C, "b,C")))
				print("|{:^5s}|{:^10d}|".format("宽", rectangular.b(b, C, "b,C")))
				print("|{:^4s}|{:^10d}|".format("周长", rectangular.C(b, C, "b,C")))
				print("|{:^4s}|{:^10d}|".format("面积", rectangular.S(b, C, "b,C")))
				time.sleep(1)

			if b != "" and S != "":
				b = int(b)
				S = int(S)
				print("|{:^5s}|{:^10d}|".format("长", rectangular.a(b, S, "b,S")))
				print("|{:^5s}|{:^10d}|".format("宽", rectangular.b(b, S, "b,S")))
				print("|{:^4s}|{:^10d}|".format("周长", rectangular.C(b, S, "b,S")))
				print("|{:^4s}|{:^10d}|".format("面积", rectangular.S(b, S, "b,S")))
				time.sleep(1)

			if C != "" and S != "":
				C = int(C)
				S = int(S)
				print("|{:^5s}|{:^10d}|".format("长", rectangular.a(C, S, "C,S")))
				print("|{:^5s}|{:^10d}|".format("宽", rectangular.b(C, S, "C,S")))
				print("|{:^4s}|{:^10d}|".format("周长", rectangular.C(C, S, "C,S")))
				print("|{:^4s}|{:^10d}|".format("面积", rectangular.S(C, S, "C,S")))
				time.sleep(1)

		if second == 4:
			fenge()
			print("请输入数据(如果数据未知按“Enter”，目前只支持整数)")
			a = str(input("底："))
			h = str(input("高："))
			S = str(input("面积："))

			if a != "" and h != "":
				a = int(a)
				h = int(h)
				print("|{:^5s}|{:^10d}|".format("底", parallelogram.a(a, h, "a,h")))
				print("|{:^5s}|{:^10d}|".format("高", parallelogram.h(a, h, "a,h")))
				print("|{:^4s}|{:^10d}|".format("面积", parallelogram.S(a, h, "a,h")))
				time.sleep(1)
			
			if a != "" and S != "":
				a = int(a)
				S = int(S)
				print("|{:^5s}|{:^10d}|".format("底", parallelogram.a(a, S, "a,S")))
				print("|{:^5s}|{:^10d}|".format("高", parallelogram.h(a, S, "a,S")))
				print("|{:^4s}|{:^10d}|".format("面积", parallelogram.S(a, S, "a,S")))
				time.sleep(1)

			if h != "" and S != "":
				h = int(h)
				S = int(S)
				print("|{:^5s}|{:^10d}|".format("底", parallelogram.a(h, S, "h,S")))
				print("|{:^5s}|{:^10d}|".format("高", parallelogram.h(h, S, "h,S")))
				print("|{:^4s}|{:^10d}|".format("面积", parallelogram.S(h, S, "h,S")))
				time.sleep(1)

		if second == 5:
			fenge()
			print("请输入数据(如果数据未知按“Enter”)")
			a_and_b = str(input("上下底的和："))
			h = str(input("高："))
			S = str(input("面积："))

			if a_and_b == "":
				h = float(h)
				S = float(S)
				print("|{:^5s}|{:^10.3f}|".format("上下底的和", trapezoidal.a_and_b(h, S)))
				print("|{:^8s}|{:^10.3f}|".format("高", h))
				print("|{:^7s}|{:^10.3f}|".format("面积", S))
				time.sleep(1)

			if h == "":
				a_and_b = eval(a_and_b)
				a_and_b = float(a_and_b)
				S = float(S)
				print("|{:^5s}|{:^10.3f}|".format("上下底的和", a_and_b))
				print("|{:^8s}|{:^10.3f}|".format("高", trapezoidal.h(a_and_b, S)))
				print("|{:^7s}|{:^10.3f}|".format("面积", S))
				time.sleep(1)

			if S == "":
				a_and_b = eval(a_and_b)
				a_and_b = float(a_and_b)
				h = float(h)
				print("|{:^5s}|{:^10.3f}|".format("上下底的和", a_and_b))
				print("|{:^8s}|{:^10.3f}|".format("高", h))
				print("|{:^7s}|{:^10.3f}|".format("面积", trapezoidal.S(a_and_b, h)))
				time.sleep(1)

	if first == 2:
		fenge()
		second = int(input("1 正方体\n"))

		if second == 1:
			fenge()
			

	if first == "":
		break
				