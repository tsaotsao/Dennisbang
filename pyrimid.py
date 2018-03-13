def pyrimid(n):
	m = int(input('你要幾公分：'))
	n=m-1
	for i in range(1,n+2):
		for j in range(1,2*n):
			x=n-i+1
			y=2*i-1
			print('*'*x+'x'*y+'*'*x)
			break
haha = pyrimid(2)