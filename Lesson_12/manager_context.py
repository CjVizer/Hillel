with open('src.jpg', 'rb') as src, open('dst1.jpg', 'wb') as dst:
    if src.closed is False:
        print('File opened')
    else:
        print('File closed')

    while True:
        data = src.read(32)
        if data:
            dst.write(data)
        else:
            break

if src.closed is False:
    print('File opened')
else:
    print('File closed')