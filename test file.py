try:
    file=open("E:\\python programs\\program`s files\\bf.txt",'w')
    print(file.read())
    print(1/0)
finally:
    file.close()
