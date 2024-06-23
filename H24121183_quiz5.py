size = int(input('Input the size of the grid: '))

#建立grid格式
element = ['_']
line = (element[0] + " ")*size + '\n'
matrix = line*size
print(matrix)


#輸入欲變更的矩陣位置與元素
pos = input('Enter the cell coordinates to edit: ')
val = input('Enter the new value for the cell: ')

while pos != 'done': #使用者輸入不為done時則繼續
	pos.split(',') #先將輸入的位子分為兩個字串以待等等使用
