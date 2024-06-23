year = int(input('Please input Year:'))
month = int(input('Please input Month:'))

#設定月份的天數
if month == 2:
	if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
		days = 29
	else:
		days = 28
elif month == 4 or 6 or 9 or 11:
	days = 30
else:
	days = 31

#算出該月份的第一天是星期幾 將1、2月視為13和14月
if month == 1 or month == 2:
	month += 12

#設定要用到的算式
year -= 1
k = year % 100
j = year // 100
w = (1 + 13*(month+1)//5 + k + k//4 + j//4 + 5*j) % 7

#印出日曆
print('Sun Mon Tue Wed Thu Fri Sat')
print("    "*((w % 7 + 7) % 7), end="")

for i in range(1, days+1):
	print("{0:3d}".format(i), end="")
	if(i + (w%7+7)%7)%7 == 0:
		print()