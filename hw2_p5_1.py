n = int(input("Input an integer number:"))
def fib(n): #定義費氏數列的前n個數字
	fib_list = [0,1]
	for i in range(2,n): #建立費氏數列清單
		fib_list.append(fib_list[i-1] + fib_list[i-2])
		#依照費氏數列規則將元素逐一加入到清單中
	return fib_list
	#回傳算的值到清單中

result = fib(n+1)
#定義數列結果
print('The', n, '-th Fibonacci Sequenceresult is:', result[n])
#輸出結果的第 n+1 個數