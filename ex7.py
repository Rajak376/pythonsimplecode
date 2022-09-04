try:
    f=open('file.txt','w')

    try:
        f.write('i am learing simple codings')

    except:

        print('an exption is occurred')

    finally:

        f.close()

        print(close)

except:

    print('try and expcet are closed')
