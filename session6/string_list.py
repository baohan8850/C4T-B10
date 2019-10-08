items = ['sport', 'LOL', 'BTS']

print(items)
a,b = input("them so thich:").split(',')
items.append(a)
items.append(b)

for i,item in enumerate(items):
    print(i+1,".",item.upper())


for s in items:
    if s.startswith('E'):
        print(s)