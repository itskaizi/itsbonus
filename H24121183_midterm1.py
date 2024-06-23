i, j = 9, 9 #設定變數i、j的初始值

#i j兩變數的遞減 
while j >= 1: 
	while i >= 1:
		print(i, 'x', j, '=', i*j, end = '\t')
		print(i, 'x', j-1, '=', i*(j-1), end ='\t')
		print(i, 'x', j-2, '=', i*(j-2), end = '\n')
		i = i - 1
	print()
	i = 9
	j -= 3