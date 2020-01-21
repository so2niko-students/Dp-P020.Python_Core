#fName = input('Enter a filename, please')
fName = 'log.txt'
#text = input('Enter an information')
#with open(fName, 'a') as f:
#   f.write(text)

with open(fName, 'r') as f:
    #print(f.readline())
    print(f.readlines())
    for line in f:
        print(line)

    
