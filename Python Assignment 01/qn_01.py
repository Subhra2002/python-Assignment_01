
numbers=[]

for a in range(2000,3201): 
    if (a%7==0) and (a%5!=0):
        numbers.append(a)

print(numbers)
