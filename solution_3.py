num=int(input("Enter the number"))
t=bin(num)
print(t)
t=t[2:]
z=t.split('0')
print(z)  
print(max(map(len,z)))

