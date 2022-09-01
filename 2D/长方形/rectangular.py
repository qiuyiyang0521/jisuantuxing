def a(x, y, Type):
	if Type == "a,b":
		return x
	if Type == "a,C":
		return x
	if Type == "a,S":
		return x
	if Type == "b,C":
		return int(y / 2 - x)
	if Type == "b,S":
		return int(y / x)
	if Type == "C,S":
		a = 1
		while True:
		    b = x / 2 - a
		    if a * b == y:
		        if a<b:
		        	a,b = b,a
		        return int(a)
		        break
		    a += 1
def b(x, y, Type):
	if Type == "a,b":
		return y
	if Type == "a,C":
		return int(y / 2 - x) #不改类型会报错，奇怪！
	if Type == "a,S":
		return int(y / x) #This's too.
	if Type == "b,C":
		return x
	if Type == "b,S":
		return x
	if Type == "C,S":
		a = 1
		while True:
		    b = x / 2 - a
		    if a * b == y:
		        if a<b:
		        	a,b = b,a
		        return int(b)
		        break
		    a += 1

def C(x, y, Type):
	if Type == "a,b":
		return (x + y) * 2
	if Type == "a,C":
		return y
	if Type == "a,S":
		return int((y / x + x) * 2)
	if Type == "b,C":
		return y
	if Type == "b,S":
		return int((y / x + x) * 2)
	if Type == "C,S":
		return x

def S(x, y, Type):
	if Type == "a,b":
		return x * y
	if Type == "a,C":
		return int((y / 2 - x) * x) #和33行的情况一样
	if Type == "a,S":
		return y
	if Type == "b,C":
		return int((y / 2 - x) * x)
	if Type == "b,S":
		return y
	if Type == "C,S":
		return y

