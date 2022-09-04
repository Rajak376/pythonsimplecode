#searching error in file

with open('file.txt') as f:
    if 'error' in f.read():
        print('error found')
