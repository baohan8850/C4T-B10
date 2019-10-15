sach = {
    'name':'dragon ball',
    'year':'2014',
    'char':'Son Goku, Picollo, Gohan,...'
}

sach['conutry'] = 'Japan'

print(sach)

for x in sach:
    print(x,'-',sach[x])



sach['name'] = 'a'
sach['year'] = 1999
sach['char'] = ['b', 'f', 'r']
sach['country'] = 'c'

print(sach)

#sach['char'].append('d')
print(sach['char'][1])

for x in sach['char']:
    print(x)

for z in sach:
    print(z,sach[z])