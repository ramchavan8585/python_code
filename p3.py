#WAPP take two list , first list contain items as number from 1 to 10, second list contain numbers from 15 to 20 and perform the following task
#1>shallow copy 2>deep_copy 3>append 4>extend 5>insert 5>slicing and indexing

import copy
l1=[1,2,3,4,5,6,7,8,9,10]
l2=[15,16,17,18,19,20]

print("\nlist 1 :-> ",l1)
print("\nlist 2 :-> ",l2)
l3=l1 #shallow copy
#copy.copy() also used to perform shallow copy

print("\nlist 3 :-> ",l3)
print('\nID of List l1:', id(l1))
print('\nID of List l3:', id(l3))

#deep copy
l4=copy.deepcopy(l2)
print("\nlist 4:-> ",l4)
new_list=[21,22,23,24,25]
l4.append([21,22,23,24,25])
print("\nappended list l4:-> ",l4)
l3.extend([30,31,32,33,34,35])
print("\n extended list l3:-> ",l3)
print("\nremoved element from l3",l3.remove(33))
print("\npop method on l4 :-> ",l4.pop())
l4.insert(1,78)

print("insert at first index of l4 :-> ",l4) 

#slicing in list
slice_obj=slice(4,7)
print("sliced list l3 :-> ",l3[slice_obj])




