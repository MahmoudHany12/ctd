import numpy as  np
array= np.random.randint(1, 100, 5)
print(array)
x=5
s = str(input(" enter or remove "))
if s == "remove":
    if x >= 5:
        a = int(input("Enter  Integer to remove : "))
        array= np.delete(array ,np.where(array == a))
        print(array.tolist())
    else :
        print("bag is at minimum capcity")
elif s == "enter":
    x=x+1
    b = int(input("Enter  Integer to add : "))
    array= np.append(array ,b)
    print(array.tolist())

             
