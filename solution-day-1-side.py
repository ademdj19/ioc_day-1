import re
inputs = open("Beginnings-side.txt","r").read()
passwords = inputs.split("\n")
sum_of_first_digits = 0
for password in passwords:
	result = re.fullmatch(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!#$%&\'()*<=>?@"]).{6,20}$', password)
	if result:
		first_digit = [*list(filter(lambda x:x.isdigit(),password)),0][0]
		print(first_digit,password,sep="---")
		sum_of_first_digits += int(first_digit)
print(sum_of_first_digits)	

