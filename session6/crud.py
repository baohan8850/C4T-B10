list = ['bun','pho','mien']
n = input('ban muon chon C,R,U,D?').lower()

if n == "c":
    a = input('mon ban thich la?')
    list.append(a)
    print(list)

elif n == "r":
    for i, item in enumerate(list):
        print(i+1,".",item)

elif n == "u":
    i = int(input('vi tri:'))
    x = input('so thich: ')
    list[i] = x
    print(list)

elif n == "d":
    b = input('nhap phan tu muon xoa: ')
    list.remove(a)
    print(list)
