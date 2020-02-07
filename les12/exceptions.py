g = [11]
try:
    print(1 / 0)
    print('Thanks for watching in try')
    print(g[11])
except KeyError:
    print('keyError except')
except IndexError:
    print('IndexError except')
except:
    print('empty except')
finally:
    print('Thanks for watching. Final')




    
  
    
