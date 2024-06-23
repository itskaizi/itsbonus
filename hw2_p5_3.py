k =i nt(input("The number of the requested element in Fibonacci(n) number:"))
#仿射密碼
s1 = input('The first string for Palindromic detection(s1)=')
s2=input('The second string for Palindromic detection(s2)=')
x=input('The plaintext to be encrypted:')
print('----- extract key for encrypt method -----')

def fib(k):
#定義費氏數列的前n個數字
	fib_list=[0,1]
	#建立費氏數列清單
	for i in range(2, k):
		fib_list.append(fib_list[i-1] + fib_list[i-2])
		#依照費氏數列規則將元素逐一加入到清單中
	return fib_list
	#回傳算的值到清單中

result = fib(k+1)
#定義數列結果
print('The',k,'-th Fibonacci Sequenceresult is:',result[k])
#輸出結果的第 n+1 個數



n1=' '+s1+' '
n2=' '+s2+' '
for i in range(0,len(n1)):

	if n1[1+i:len(n1)-1-i]==n1[len(n1)-2-i:i:-1]:
		a=n1[1+i:len(n1)-1-i]
		print('Longest palindrome substing is:',a)
		print('Length is: ',a)
		break

else:
#從每個字母開始檢查 往左右兩邊擴展
	if n2[2+j:len(n2)-1-j]==n2[len(n2)-2-j:j+1:-1]:
		b=n2[2+j:len(n2)-1-j]
		print('Longest palindrome substing is:',b)
		print('Length is: ',len(b))
		break
	elif n2[1+j:len(n2)-2-j]==n2[len(n2)-3-j:j:-1]:
		b=n2[1+j:len(n2)-2-j]
		print('Longest palindrome substing is:',b)
		print('Length is: ',len(b))
		break
	j += 1

#加密
print('----- encryption completed -----')

letters = list(x)
number = []
encrypt = []

for m in range(o,len(x)):
	number.append(ord(letters[m]))
#逐步將加密後字母列入清單
for o in range(0, len(x)):
	#y1 = len(a)*(((number[o] + result[k])+len(b)-65)%26)+65
	encrypt.append(chr((((len(a)*(number[o] + result[k])+len(b))-65)%26)+65))

#print(encrypt) #['I', 'T', 'J']
#將字母組合成一單字 並印出結果
result = ''.join(encrypt)
print('The encrypted text is:',result)