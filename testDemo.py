numbers=[1,2,3,1,5,0,0,8,1]

def filterone(number):
   if(number==0):
      return True
   else:
      return False

odd_numbers=filter(filterone,numbers)

for number in odd_numbers:
   print(number)
   lst=list(number)
   print(lst)