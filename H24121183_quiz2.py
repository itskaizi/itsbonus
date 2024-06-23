#使用者輸入消費金額和會員等級
amount = int(input('Enter the shopping amount :'))
membership = input('Enter the membership level (Regular or Gold) :')

#設立會員等級變數
r = ('Regular')
g = ('Gold')

#檢視會員等級是否為正確
if membership == r and g: #假設會員等級輸入正確
	if amount < 1000:         #如果金額小於1000 直接輸出會員等級＋金額
		print(membership + amount)
	elif 1000 <= amount < 2000:   #如果金額大於1000 對應會員級別享有折扣
		if membership == r:
			print('Regular', + amount*0.9)
		elif membership == g:
			print('Gold', + amount*0.85)
		elif 2000 <= amount < 3000:
			if membership == r:
				print('Regular', + amount*0.85)
			elif membership == g:
				print('Gold', + amount*0.8)
	elif 3000 <= amount:
		if membership == r:
			print('Regular', + amount*0.8)
		elif membership == g:
			print('Gold', + amount*0.75)
else:  #若會員等級輸入錯誤
	print('Invalid membership level. Please enter \' Regular \' or \' Gold \'')






