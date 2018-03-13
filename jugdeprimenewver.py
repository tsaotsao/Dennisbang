def theprimenumber(i):
		while True:
			n = int(input('請輸入一個數字判斷是不是質數（輸入0可以離開):'))
			if n==0:
				print('bye')
				break
			elif n==1:
				print('這不是質數亦不是和數')
			elif n==2:
				print('yes')
			else:
				for i in range(2,n):
					if n%i ==0:
						print('no')
						break
					elif n-1==i:
						print('yes')
						break
haha = theprimenumber(1)