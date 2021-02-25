import random

r = random.randint(1, 10)
count = 0

while True:
    num = input('請猜數字: ')
    num = int(num)
    count += 1
    if num == r:
        print('猜對囉')
        print('一共猜了', count, '次')
        break
    elif num > r:
        print('比答案大喔')
    elif num < r:
        print('比答案小喔')
    print('一共猜了', count, '次')