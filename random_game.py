i = 3
import random
r = random.randint(1, 10)
while True:
	num = input('請輸入數字')
	num = int(num)
	if num == r:
		print('恭喜猜對了')
		break
	elif num > r:
		i = i - 1
		print('再小一點 還剩下', i, '次機會')
		if i == 0:
			break
	elif num < r:
		i = i - 1
		print('再大一點 還剩下', i, '次機會')
		if i == 0:
			break