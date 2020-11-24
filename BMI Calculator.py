
name = input('whats your name?\n')
print('hello there,%s!' % name)
po = input('would you like to know your BMI? yes or no\n')
yes = 2
no = 4
yesno = yes / no
if yesno < 1:
	print('great lets get started')
else:
	print('goodbye')

weight_kg = float(input('enter your weight : '))

height_m = float(input('enter your height : '))

bmi = weight_kg / (height_m ** 2)
print('bmi: ')
print(bmi)
if bmi < 25:
	print(name)
	print('is not over weight')
else:
	print(name)
	print('is overweight')

	
