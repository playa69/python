import math
with open("out.txt", "w") as f:
	for i in range(0,10000):
		res = ("true" if 
				math.floor(math.sqrt(i)) ** 2 == i 
				else "false")
		f.write(f"if(a=={i})" + "{return " + res + ";}\n")