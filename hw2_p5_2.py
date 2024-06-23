k = input('Enter a string:')
n = ''+ k + ''

#先檢查單字是否有回文
#去掉開頭第一個字母 從第二個字母檢查到最後是否滿足回文
#去掉最後一個字母 從第一個字母檢查到最後是否滿足回文
#都沒有回文 則去除頭尾字母產生新單字 並進行上述流程直到發現回文

#程式碼中的i是若進到下一循環則將單字去頭去尾

for i in range(0, len(n)):
	#先檢查完整單字是否有回文
	#如果有便直接打印
if n[1+i:len(n)-1-i]==n[len(n)-2-i:i:-1]:
	print('Longest palindrome substing is: ',n[1+i:len(n)-1-i])
	print('Length is: ',len(n[1+i:len(n)-1-i]))
	#打印成功便可出循環
	break

else:
	#去掉開頭第一個字母 從第二個字母檢查到最後是否滿足回文
	if n[2 + i : len(n)-1-i] == n[len(n)-2-i : 1 + 1 : -1]:
		#若有則打印並出循環
		print('Longest palindrome substing is:', n[2+i:len(n)-1-i])
		print('Length is:',len(n[2+i:len(n)-1-i]))
		#若有則出循環
		break

		#若不滿足前述的if 則去掉最後一個字母 從第一個字母檢查到最後是否滿足回文
	elif n[1+i:len(n)-2-i]==n[len(n)-3-i:i:-1]:
		#若有 則打印並出循環
		print('Longest palindrome substing is:', n[1+i:len(n)-2-i])
		print('Length is:',len(n[1+i:len(n)-2-i]))
		break

i += 1