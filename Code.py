import math

def conse_int(num):
	try:
		n = int(num)
		satis = 0
		# 一个数M若可以写成以a开头的连续n个自然数之和，则M=a+(a+1)+(a+2)+…+(a+n-1)=n*a+n*(n-1)/2
		for start_num in range(1,math.ceil(n/2),1):
			for conse_num in range(2,math.ceil(n/2)+1,1):
				if (NUM == start_num * conse_num + conse_num * (conse_num-1)/2):
					satis = 1
					break
			if satis == 1:
				break
	    			
	except ValueError:
		print("Please input an integer")
	return satis,start_num,conse_num

NUM = 188	
result,start,conse = conse_int(NUM)
if result == 1:
	print("Integer number %s can be divided into %s integers, start from %s"%(NUM,conse,start))
elif result == 0:
	print("No")
