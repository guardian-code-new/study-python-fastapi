
ex = ['1.', '2.', '3.', '4.']
print(ex[0],'and', ex[1])

Name = 'Julie'
load_1 = 6
load_2 = 4.68
load_3 = load_1 * load_2
load_4 = load_1 + load_2
l1 = load_1 != load_2
l2 = load_1 > load_2
l3 = load_1 == load_2
new_lst = ['cat', 'dog', 'parrot', 'hamster']
tpl = ('tax', 'finance', 'money')
dct1 = {'Name': Name, 'Age': int(load_3), 'pet': new_lst[-1], 'quantity': float(load_4)}
check = None
result = dct1['pet'] in new_lst
print(l1, l2, l3, new_lst)
print(dct1.items(), '\n', result)

print('\n', 'Робота з рядками:')

print(ex[0])
num_str = 125
trans_str = str(num_str)
print(trans_str)

print(ex[1])
message = 'Hi, my name is Python!'
change_mes1 = message.replace('y', '0')
change_mes1 = change_mes1.replace('i', '1')
print(change_mes1)

print(ex[2])
split_test = 'This is a split test'
spl = split_test.split()
print(spl)
string_join = " ".join(spl)
print(string_join)

print(ex[3])
print(len(string_join))

print('\n', 'Робота зі списками:')

print(ex[0])
list_append = [1, 2, 3]
print(list_append)
list_append.append(4)
print(list_append)
list_append.append(5)
print(list_append)

print(ex[1])
list_extend = [4, 5, 6]
print(list_extend)
list_extend.extend([7, 8, 9])
print(list_extend)

print(ex[2])
ind1 = list_extend.index(6)
print(ind1)

print(ex[3])
print(len(list_append))

print('\n', 'Робота зі словниками:')

print(ex[0])
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test.get('car'), dict_test.get('where'))

print(ex[1])
print(dict_test.keys())
print(dict_test.values())

print(ex[2])
print(dict_test.items())
