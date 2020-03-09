'''tupl = ("banana","orange","apple","mango",23)
print (tupl)
print(tupl[1])
print(tupl[1:4])
print(tupl[-1])
print(tupl[-4])
print (tupl[-3:-1])
# count and find the index of ele in tuple and delete element

x=tupl.count("apple")
print (x)
y = tupl.index("mango")
print (y)

del y
print (y)'''
tpl = ('d','u','r','g','a','s','o','f','t','a')
print(tpl)
print(tpl[:4])
print(tpl.count('a'))
print(tpl.index('a'))
print(type(tpl))
ntpl = ("durga", (7, 8, 6), (1, 2, 3))
print(ntpl[0][3])
print(ntpl[1][1])
print(ntpl[2][2])
#negative indexing
print(ntpl[-2][-1])
print(ntpl[:])


