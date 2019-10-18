for a in range(1,101):
	if a%7!=0 and (a-7)%10!=0:
		if a>69 and a<80:
			continue
		print(a)
	a+=1
