import os
file = "C:\\Users\\mps\\Desktop\\Razzak\\file.txt"
if os.path.exists(file) :
    file = open(file, 'r')
    print(file.read())

else:
    print('file not exist')
