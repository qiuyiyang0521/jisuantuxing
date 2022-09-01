def a(x, y, Type):
	if Type == "a,h":
		return x
	if Type == "a,S":
		return x
	if Type == "h,S":
		return int(y / x)
def h(x, y, Type):
	if Type == "a,h":
		return y
	if Type == "a,S":
		return int(y / x)
	if Type == "h,S":
		return x

def S(x, y, Type):
	if Type == "a,h":
		return x * y
	if Type == "a,S":
		return y
	if Type == "h,S":
		return y
