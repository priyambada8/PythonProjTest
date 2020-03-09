list=[3,'t',6.9,12, "test",'u',8,5,11]
print(list[:])
list[0]=67
list.append([5, 6, 7])
list.extend([5, 6, 7])
list.insert(3,10)
list[2:2] = [5, 7]
print(list.pop(1))
print(list)
print(len(list))
#print(list[4])
#print(list[:-4])
#print (list[2:4])
#print(list[-8:-6])

#nested list

#lst = ["ram",[2,4,7,5,6]]
#print(lst[1][2])

#thislist1 = ["apple", "banana", "cherry","apple"]

#thislist2 = ['orange','mango']

#thislist1.append(thislist2)
#print (thislist1)

#thislist1.extend(thislist2)
#print (thislist1)
#-============ to remove the values=========
#thislist1.remove("banana")
#thislist1.pop(0)
#del thislist1[2]
#print (thislist1)

#===count the occurance of item inside list==
#x=thislist1.count("apple")

#x=thislist1.index("cherry")
#print (x)
nlst = ["ravi","@34xr", [2,0,1,5],[4,9,0]]
# Nested indexing
print(nlst[3][1])
print(nlst[1][4])
#negative index
print(nlst[-3][1])
print(nlst[:])
print(nlst.count(0))



