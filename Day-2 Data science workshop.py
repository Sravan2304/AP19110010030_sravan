#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Write a  program to check whether the user is elgible to vote or not
x = int(input("Enter your age:"))
if (x>=18):
    print("You are elgible to vote")
else:
    print("You are not elgible to vote")


# In[6]:


#To check whether the given number is positive or not
x = int(input("Enter your number:"))
if (x>0):
    print("The number is positive:",x)
elif (x<0):
    print("The number is negative:",x)    
else:
    print("The number is zero")


# In[13]:


#To check whether given number is odd or even, and if it's even check will it be divided by 4 or not
x = int(input("Enter your number:"))
if (x%2==0 and x%4==0):
    print("The number is even and divisible by 4:",x)
elif (x%2==0 and x%4!=0):
    print("The number is even:",x)    
else:
    print("The number is odd")


# In[18]:


#program to print the student grades based on their percentages
x = int(input("Enter your percentage:"))
if (x>=60):
    print("The student passed in distinction",x,"%")
elif (x>=35 and x<60):
    print("The student just passed:",x,"%")    
else:
    print("The student failed")


# In[3]:


#To check the given year is leap year or not
x = int(input("Enter the year number:"))
if (x%4==0 and x%100!=0):
    print("The year is leap year",x) 
elif (x%100==0):
    print("The year is not a leap year",x)
elif (x%400==0):
     print("The year is leap year",x)     
else:
    print("The year is not a leap year")

