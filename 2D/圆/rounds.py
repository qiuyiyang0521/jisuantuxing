def r(a, b):
	#b是直径
	if b == "d" or b == "直径":
		return a / 2
	#b是周长
	if b == "C" or b == "周长" or b == "c":
		return a / 3.14 / 2
	#b是面积
	if b == "S" or b == "面积" or b == "s":
		return (a / 3.14) ** 0.5

	if b == "r" or b == "半径":
		return a

def d(a, b):
	#b是半径
	if b == "r" or b == "半径":
		return a * 2
	#b是周长
	if b == "C" or b == "周长" or b == "c":
		return a / 3.14
	#b是面积
	if b == "S" or b == "面积" or b == "s":
		return (a / 3.14) ** 0.5 / 2

	if b == "d" or b == "直径":
		return a

def C(a, b):
	#b是半径
	if b == "r" or b == "半径":
		return a * 2 * 3.14
	#b是直径
	if b == "d" or b == "直径":
		return a * 3.14
	#b是面积
	if b == "S" or b == "面积" or b == "s":
		return (a / 3.14) ** 0.5 * 2 * 3.14

	if b == "C" or b == "周长" or b == "c":
		return a

def S(a, b):
	#b是半径
	if b == "r" or b == "半径":
		return a ** 2 * 3.14
	#b是直径
	if b == "d" or b == "直径":
		return (a / 2) ** 0.5 * 3.14
	#b是周长
	if b == "C" or b == "周长" or b == "c":
		return ((a / 3.14) / 2) **2

	if b == "S" or b == "面积" or b == "s":
		return a 
