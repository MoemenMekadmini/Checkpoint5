#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Point3D:
    def __init__(self, x, y,z):
        self.x = x
        self.y = y
        self.z = z
    def method(self):
        return "({},{},{})".format(self.x, self.y, self.z)
my_point = Point3D(1,2,3)
print(my_point.method())


# In[2]:


class rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return (self.length+self.width)*2
my_rectangle=rectangle(4,3)
print(my_rectangle.area()) 
print(my_rectangle.perimeter())
    


# In[18]:


class circle:
    def __init__(self,a,b,r,x,y):
        self.a=a
        self.b=b
        self.r=r
        self.x=x
        self.y=y
    def area(self):
        return self.r**2*3.14  
    def perimeter(self):
        return 2*self.r*3.14
    def isInside(self):
        if (x-a)**2 - (y-b)**2==r**2:
            print("Inside the circle")
        else:
            print("Not inside the circle")
c = circle(0,5,2,1,3)
print(c.area())
print(c.perimeter())
print(c.isInside())

    


# In[10]:


class bank:
    def __init__(self):
         self.balance=0
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print(" You Withdrew:", amount)
        else:
            print(" Insufficient balance  ")
s = bank()
print(bank.deposit())
print(bank.withdraw())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




