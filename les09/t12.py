import sys
n = 1
m = 56


def strongest_even(n, m):
     """Return the even number that is the strongest in the interval."""
     dict_num = {}
     for num in range(n, m + 1):
          key = num
          counter = 0
          while num % 2 == 0:
              num /= 2
              counter += 1
              dict_num[key] = counter
     result_list = [key for key, value in dict_num.items() if value == max(dict_num.values())]
     
     return min(result_list)


print(strongest_even(1, sys.maxsize))
