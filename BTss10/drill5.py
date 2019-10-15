list = [
    {
        'name':'Huy',
        'role':'waiter',
        'hour':12,
        'salary per hour':0.8
    },
    {
        'name':'Trung',
        'role':'cook',
        'hour':24,
        'salary per hour':1.5
    },
    {
        'name':'M.Duc',
        'role':'manager',
        'hour':20,
        'salary per hour':2
    }
]

print(list)

#p1 = {
#    'name':'Don',
#    'role':'waiter',
#    'hour':12,
#    'salary per hour':0.9
#}

#p2 = {
#    'name':'H.Duc',
#    'role':'waiter',
#    'hour':14,
#    'salary per hour':0.7
#}

#list.append(p1)
#list.append(p2)

#print(list[2])

#print(list[0])

#p3 = {
#    'name':'huyen',
#    'role':'waitress',
#    'hour':14,
#    'salary per hour':1
#}


#list.append(p3)


list.pop(2)

for p in list:
    print(p)