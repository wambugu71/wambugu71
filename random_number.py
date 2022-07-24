while True:
	import random
	rad =random.randint(1, 9)
	guess=int(input("key in your guess:"))
	try:
		if rad>guess:
			print("too low!")
			
		elif rad<guess:
			print("Too high!")
			
		elif rad==guess:
			print("congrats! correct!")
		else:
			print("invalid operation!")
	except:
			print("sorry that is not an interger!")
			redo=input("Do you wish to continue?(y/n)?:")
			if redo=='n':
				break
				
print("randon generated number is %d"%rad)

#made by @ken########