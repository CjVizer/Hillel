buff = 32

src = open('src.jpg', 'br')
dst = open('dst.jpg', 'wb')

while True:
    data = src.read(buff)
    if data:
        dst.write(data)
    else:
        break

dst.close()
src.close()