import random
start = input('請輸入隨機數字範圍開始值：')
end = input('請輸入隨機數字範圍結束值：')
start = int(start)
end = int(end)
x = random.randint(start, end)
count = 0
while True:
	count += 1 #count = count + 1
	num = input('請猜數字: ')
	num = int(num)
	if num == x:
		print('你猜對了! 總共猜了', count, '次')
		break 

	elif num > x:
		print('比答案大')
	elif num < x:
		print('比答案小')
	print('你猜了第', count, '次')

