
x=str(input("what is the input type c if celsius f if fahrenheit  "))
if x == 'c' :
    celsius = float(input("Enter temperature in celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))
elif x == 'f' :
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))
else:
    print("error enter valid input like c or f")
    
    
    



