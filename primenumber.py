def primenumber(n):
	#the_prime_number = []
	#the_prime_number[0]=2
	for i in range(2,n): 
		prime1=i
		if i%2 == 0 and i!=2:
			prime1 = ''
		elif i%3 == 0 and i!=3:
			prime1 = ''
		elif i%5 == 0 and i!=5:
			prime1 = ''
		elif i%7 ==0 and i!=7:
			prime1 = ''
		elif i%11 ==0 and i!=11:
			prime1 = ''
		elif i%13 ==0 and i!=13:
			prime1 = ''
		elif i%17 ==0 and i!=17:
			prime1 = ''
		elif i%19 ==0 and i!=19:
			prime1 = ''

		print(prime1)

n=int(input("請輸入一個數字："))
haha = primenumber(n)
the_prime_number = []
#print(the_prime_number)

#while 1 and 2:
#跟 
#while 1:
#   while 2:
#哪個複雜度比較高？