nums = input('Enter a sequence of integers separated by whitespace: ')

#將使用者輸入的string更改為list
nums.split( )

#initialization
L = []
length = 0

for i in range(len(nums)): #設定i為在list長度內的數
	if int(nums[i]) < int(nums[i+1]): #如果list中前一個數比後面的數小
		L.append(num[i]) #則將該元素增加至L內
		length += 1 #設定變數length也+1

print('Length', length)
print('LICS:', L)