try:
    f=open('file.txt')

    try:
        f.write('i am learning pyhton codeing')

    except:

        print('an exception occurred')

    finally:

        f.close()
        print('close')

except:

    print('someting not went wrong when open the file')
