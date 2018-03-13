def jugdenumber(i):
	while True:
		n = int(input('輸入一個數字判斷是不是質數(輸入0可以退出):'))
		if n == 0:
			print('bye')
			break
		while True:
			if n!=0:
				if n%2==0 and n!=2:
					print('no')
					break
				elif n%3==0 and n!=3:
					print('no')
					break
				elif n%5==0 and n!=5:
					print('no')
					break
				elif n%7==0 and n!=7:
					print('no')
					break
				elif n%11==0 and n!=11:
					print('no')
					break
				elif n%13==0 and n!=13:
					print('no')
					break
				elif n%17==0 and n!=17:
					print('no')
					break
				elif n%19==0 and n!=19:
					print('no')
					break
				elif n%23==0 and n!=23:
					print('no')
					break
				elif n%29==0 and n!=29:
					print('no')
					break
				elif n%31==0 and n!=31:
					print('no')
					break
				elif n%37==0 and n!=37:
					print('no')
					break
				elif n%41==0 and n!=41:
					print('no')
					break
				elif n%43==0 and n!=43:
					print('no')
					break
				elif n%47==0 and n!=47:
					print('no')
					break
				elif n%53==0 and n!=53:
					print('no')
					break
				elif n%59==0 and n!=59:
					print('no')
					break
				elif n%61==0 and n!=61:
					print('no')
					break
				elif n%67==0 and n!=67:
					print('no')
					break
				elif n%71==0 and n!=71:
					print('no')
					break
				elif n%73==0 and n!=73:
					print('no')
					break
				elif n%79==0 and n!=79:
					print('no')
					break
				elif n%83==0 and n!=83:
					print('no')
					break
				elif n%89==0 and n!=89:
					print('no')
					break
				elif n%97==0 and n!=97:
					print('no')
					break
				else:
					print('yes')
					break
haha = jugdenumber(1)