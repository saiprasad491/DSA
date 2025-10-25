d = {1:"One",2:"Two",3:"Three",4:"Four"}
print(d)  #{1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}
d = {1:"One",2:"Two",3:"Three",4:"Four",4:"dhoni"}
print(d)  #{1: 'One', 2: 'Two', 3: 'Three', 4: 'dhoni'}

print(d.keys()) #dict_keys([1, 2, 3, 4])
print(d.values()) #dict_values(['One', 'Two', 'Three', 'dhoni'])
print(d.items()) #dict_items([(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'dhoni')])

d = {i:i*i for i in range(1,11)}
print(d)  #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

d = {i:i*i for i in range(1,11) if i%2==0}
print(d)  #{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}





