n = int(input("Введите число: "))
num2 = n % 3
num3 = n // 3
is4 = False

if num2 == 1:
    num3 -= 1
    num2 = '2,2'
    is4 = True
    num4 = '4'

threes = '3,' * num3

print(threes + num2)
if is4:
    print('\n', threes + num4)    
