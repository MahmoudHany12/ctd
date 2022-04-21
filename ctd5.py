import random
c=0
bag1=10
bag2=10
bag3=10
def yourturn():
    global bag1
    global bag2
    global bag3
    choice=int(input("enter number of bag from 1 to 3 \n "))
    if(choice>3 or choice<1):
        print("please enter number from 1 to 3 try again")
        yourturn()
        return
    if choice==1:
        if (bag1==0):
            print("you cant remove balls from empty bag\n")
            yourturn()
            return
        else:
            x=int(input("enter number u want to remove:"))
            if x<0:
                print("enter number of ball from 1 to 5 try again")
                yourturn()
                return
            if x > 5 :
                 print ("you cant remove more than 5")
                 yourturn()
                 return
            elif x > bag1:
                 print ("bag under flow")
                 yourturn()
                 return
            else: 
                bag1= bag1-x 
                print(bag1,bag2,bag3)
                return
    if choice==2:
         if (bag2==0):
            print("you cant remove balls from empty bag\n")
            yourturn()
            return
         else: 
            x=int(input("enter no u want to remove:"))
            if x<0:
                print("enter number of ball from 1 to 5 try again")
                yourturn()
                return
            if x > 5 :
                print ("you cant remove more than 5\n")
                yourturn()
                return
            elif x > bag2:
                print ("bag under flow")
                yourturn()
                return
            else: 
                bag2= bag2-x
                print(bag1,bag2,bag3)
                return
    if choice==3:
         if (bag3==0):
            print("you cant remove balls from empty bag")
            yourturn()
            return
         else:
            x=int(input("enter no u want to remove:"))
            if x<0:
                print("enter number of ball from 1 to 5 try again")
                yourturn()
                return
            if x > 5 :
                print ("you cant remove more than 5")
                yourturn()
                return
            elif x > bag3:
                print ("bag under flow")
                yourturn()
                return
            else: 
                bag3= bag3-x
                print(bag1,bag2,bag3)
                return
def comp():
    global bag1
    global bag2
    global bag3
    print("computer turn \n")
    if bag1<=5 and bag1>0 :
        bag1=bag1-bag1
        print(bag1,bag2,bag3)
        return
    elif bag2<=5 and bag2>0 :
        bag2=bag2-bag2 
        print(bag1,bag2,bag3)
        return
    elif bag3<=5 and bag3>0 :
        bag3=bag3-bag3 
        print(bag1,bag2,bag3)
        return
    else:
        chice = random.randint(1, 3)
        y=random.randint(1, 5)
        if chice==1:
            if(bag1>0):
                bag1=bag1-y
                print(bag1,bag2,bag3)
                return
            elif(bag1==0):
                    r=random.randint(2, 3)
                    if(r==2):
                        if bag2 ==0:
                            bag3=bag3-y
                            print(bag1,bag2,bag3)
                            return
                        else :
                            bag2=bag2-y
                            print(bag1,bag2,bag3)
                            return
                    elif(r==3):
                        if bag3 ==0:
                            bag2=bag2-y
                            print(bag1,bag2,bag3)
                            return
                        else:
                            bag3=bag3-y
                            print(bag1,bag2,bag3)
                            return
        elif chice==2:
            if(bag2>0):
                bag2=bag2-y
                print(bag1,bag2,bag3)
                return
            elif(bag2==0):
                    r=random.randint(2, 3)
                    if(r==2):
                        if bag1 ==0:
                            bag3=bag3-y
                            print(bag1,bag2,bag3)
                            return
                        else:
                            bag1=bag1-y
                            print(bag1,bag2,bag3)
                            return
                    elif(r==3):
                        if bag3 ==0:
                            bag1=bag1-y
                            print(bag1,bag2,bag3)
                            return
                        else:
                            bag3=bag3-y
                            print(bag1,bag2,bag3)
                            return
        elif chice==3:
            if(bag3>0):
                bag3=bag3-y
                print(bag1,bag2,bag3)
                return
            elif(bag3==0):
                    r=random.randint(2, 3)
                    if(r==2):
                         if bag2 ==0:
                            bag1=bag1-y
                            print(bag1,bag2,bag3)
                            return
                         else:
                            bag2=bag2-y
                            print(bag1,bag2,bag3)
                            return
                    elif(r==3):
                         if bag1 ==0:
                            bag2=bag2-y
                            print(bag1,bag2,bag3)
                            return
                         else:
                            bag1=bag1-y
                            print(bag1,bag2,bag3)
                            return
while(c!=-1):
    if(c==0):
        yourturn()
        if(bag1==0 and bag2==0 and bag3==0):
            print("you won")
            break
        else: c=c+1
    elif(c==1):
        comp()
        if(bag1==0 and bag2==0 and bag3==0):
            print("you lost")
            break
        else: c=c-1
