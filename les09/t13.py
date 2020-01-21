a = 2049
b = 4095
c = str (bin(b))
#print (c)
count = -3
it = 0
for d in c: count += 1 
#print (count)
a = a if a % 2 == 0 else a + 1
b = b if b % 2 == 0 else b - 1
def fun(a,b,count):
    global it
    
    dva = 2**count
    if dva in range (a, b + 1):
        return dva
    for d in range (a, b + 1, 2) :
        it += 1
        print (d, it)
        if d > dva: 
          if not d % dva:
            return d
    count -= 1
    return fun (a,b,count)
print (fun (a,b,count))
