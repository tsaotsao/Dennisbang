import random
print("\n҉你҉已҉來҉到҉不҉可҉逃҉出҉之҉秘҉密҉地҉下҉協҉會҉,҉要҉猜҉出҉密҉碼҉才҉可҉逃҉出҉")
random_number = random.randint(1,100)
x = 1
y = 100
count = 0
while True:
	if count == 6:
		print('\t\t扣打被你用完了啦 滾')
		break
	elif count >=100:
		print('\n҉你҉已҉成҉功҉逃҉出҉')
		break
	else:
		for guess_number in range(x,y):
			print('\t\t你已猜錯',count,'次')
			a = int(input("~猜個密碼吧:"))	
			if a>y:
				print('\t\t幹勒猜錯拉太大了')
				break
			elif a<x:
				print('\t\t太小囉')
				break
			elif y>a>random_number:
				y=a
				print("\t\t數字介於",x,"到",y,"之間")
				break
			elif random_number>a>x:
				x=a
				print("\t\t數字介於",x,"到",y,"之間")
				break
			elif a==x or a==y:
				print("\t\t不要猜猜過的好爆")
				break
			elif random_number == a:
				print('\t\t~猜對囉~')
				count +=100
				break
		count +=1
	
	
	
