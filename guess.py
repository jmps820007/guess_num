import random
start = input('請決定隨機數字範圍開始值: ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
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