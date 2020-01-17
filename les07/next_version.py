version = input('Enter version number: ')


def next_version(version):
    """Return a string containing the next version number."""
    list_version = list(map(int, version.split('.')))
    slicE = len(str(list_version[0]))

    version = version.replace('.', '')
    next_version = str(int(version) + 1)

    if len(version) < len(next_version): 
        result = next_version[:slicE] + '.'.join(next_version[slicE:])
    elif list_version[0] > 9:
        result = next_version[:slicE - 1] + '.'.join(next_version[slicE - 1:])
    else:
        result = '.'.join(next_version)
        
    return 'Next version: ' + result


print(next_version(version))

print('Hello'[0:1])
