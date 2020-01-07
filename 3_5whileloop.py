error = 50
while error > 5:
    error = error/4
    print(error)

offset = input('Enter number: ')
offset = float(offset)
while offset !=0:
    print('correting ...')
    if offset < 0:
        offset = offset + 1
        print(offset)
    else:
        offset = offset - 1
        print(offset)
