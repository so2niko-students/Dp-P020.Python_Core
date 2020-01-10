total = 0 # This is global variable.
problems = 'no'

def my_sum(arg1, arg2):
    global problems, total
    problems = 'yes'
    print(problems,':local-problems')
    total = arg1 + arg2 # Here total is local variable.
    print ("Inside the function local total : ", total)

    return total

my_sum(1,2)
print(total,':global-total')
print(problems,':global-problems')
print((lambda x: x * 2)(22))
