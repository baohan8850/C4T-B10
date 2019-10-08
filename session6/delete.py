items = ['sport', 'LOL', 'BTS']

print(items)
new = input('so thich moi: ')
items.append(new)
print(items)

items.pop(2)
print(items)

a = input('nhap phan tu muon xoa: ')
items.remove(a)
print(items)