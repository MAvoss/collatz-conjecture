CheckNumber = float(input("enter your number"))
print(str(CheckNumber) +' setnumber')
while CheckNumber != 1:
	numcheck = CheckNumber
	if CheckNumber % 2 == 0:
			CheckNumber = CheckNumber / 2
			print(str(CheckNumber) +' output reduced')

	else:
			CheckNumber = CheckNumber * 3 + 1
			print(str(CheckNumber) +' output increased')
		
#CheckNumber = 1
#for x in range(int(input("please let me know the number youd like to #start end with"))):

	#CheckNumber = CheckNumber + x



