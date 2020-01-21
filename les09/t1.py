import operator

def power(x):
    count = 0
    while x % 2 == 0:
        x = x / 2
        count += 1
    return count

string = input("Input round: ").split(' ')
power_value = {}
for i in range(int(string[0]), int(string[1]), 1):
    tmp = power(i)
    power_value[i] = tmp
    
print(power_value)
#print(power_value.items())
maks = max(power_value.items(), key = operator.itemgetter(1))[0]
#maks = max(power_value)
print(maks)
