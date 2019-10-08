list = ['blue','orange','green']
print(list)
new = input('mau moi: ')
list.append(new)

print(list)

vt = input('nhap pt muon xoa:')
if vt == int:
    list.pop(vt)
elif vt == str:
    list.remove(vt)
print(list)