list = ['sport','LOL','BTS']
print(*list, sep=' | ')
new = input('so thich moi: ')
list.append(new)
print(*list, sep=' | ')

print('index 0:')
print(list[0].upper())

print('index 1:')
print(list[1].upper())

print('index 2:')
print(list[2].upper())

print('index 3:')
print(list[3].upper())