list1 = ['ST','BD','BTL','CG','DD','HBT']
list2 = [150300,247100,333300,266800,420900,318000]

print('chi so quan dong dan nhat:', max(list2))
print('chi so quan it dan nhat:', min(list2))

n = list2.index(max(list2))
print(list1[n])
s = list2.index(min(list2))
print(list1[s])