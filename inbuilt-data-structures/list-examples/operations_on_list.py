# li = [10,20.34,"abc",True,1+2j]
# print(li,type(li)) #[10, 20.34, 'abc', True, (1+2j)] <class 'list'>

# li = [10,20,30]
# print(len(li)) #3
# print(sum(li)) #60

# l1 = [1,2,3]
# l2 = l1
# print(l1 is l2) #True
# print(id(l1),id(l2))  #1933705893056 1933705893056

# p = print
# p("Sai")  #Sai

# l1 = [1,2,3]
# l2 = l1.copy()
# print(l1==l2) #True
# print(l1 is l2) #False
# l1[0] = 111
# print(l1,l2)  #[111, 2, 3] [1, 2, 3]

# l1 = [1,[2,3],4]
# l2 = l1.copy()

# case 1
# l1[0] = 11
# print(l1,l2)  #[11, [2, 3], 4] [1, [2, 3], 4]

# case 2
# l1[1][0] = 22
# print(l1,l2)  #[1, [22, 3], 4] [1, [22, 3], 4]

# import copy
# l1 = [1,[2,3],4]
# l2 = copy.deepcopy(l1)
# l1[1][0] = 22
# print(l1,l2)  #[1, [22, 3], 4] [1, [2, 3], 4]








