#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##1.What are the two values of the Boolean data type? How do you write them?


# In[ ]:


The two values of boolean data type are o and 1.
we can represent it as True and False.


# In[ ]:


##2. What are the three different types of Boolean operators?


# In[ ]:


Three different types of boolean operators are AND, OR and NOT.


# In[ ]:


##3.Make a list of each Boolean operator truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).


# In[ ]:


AND 
OR
NOT


 X             Y         X AND Y       X OR y      NOT X      NOT Y

True(1)    True(1)      True(1)      True(1)    False(0)    False(0)
True(1)    False(0)     False(0)     True(1)        
False(0)   True(1)      False(0)     True(1)    True(1)     True(0)
False(0)   False(0)     False(0)     False(0)   


# In[ ]:


##4. What are the values of the following expressions?
(5 > 4) and (3 == 5)------------------>False
not (5 > 4)--------------------------->False
(5 > 4) or (3 == 5)------------------->True
not ((5 > 4) or (3 == 5))------------->False
(True and True) and (True == False)--->False
(not False) or (not True)------------->True


# In[ ]:


##5. What are the six comparison operators?


# In[ ]:


1.grater than (>)
2.less than (<)
3.grater than or equql to (>=)
4.less than or equql to (<=)
eqal to (==)
not equal to (!=)


# In[ ]:


##6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.


# In[ ]:


equal to operator is used to compare both values are same or not same.
ex:x==y.
assignment operators are used to assign or store values in to variables
for example:
    x=1 and y=2,here we are assigning values 1,2 in to variables x,y
    


# In[ ]:


##7. Identify the three blocks in this code:
spam = 0
if spam == 10:------->if block
print('eggs')
if spam > 5:
print('bacon')
else:     ---------->else block
print('ham')
print('spam')
print('spam')


# In[1]:


spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')
print('spam')


# In[2]:


spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')


# In[ ]:


##8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.


# In[ ]:


if spam==1:
    print("Hello")
elif spam==2:
    print("Howdy")
else:
    print("Greetings!")


# In[ ]:


##9.If your programme is stuck in an endless loop, what keys you’ll press?


# In[ ]:


CTRL+C


# In[ ]:


##10. How can you tell the difference between break and continue?


# In[ ]:


break:
    break statement termintes the excution of the loop
continue:
    continue statement stop the excution of the current iteration and jump to next iteration 


# In[ ]:


##11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?


# In[ ]:


range(10),range(0,10),range(0,10,1) all these three functions takes the values from 0to 9


# In[ ]:


##12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.


# In[3]:


n=10
for i in range(1,n+1):
    print(i)


# In[4]:


i=1
while i < 11 :
    print(i)
    i=i+1


# In[ ]:


##13. If you had a function named bacon() inside a module named spam, how would you call it after
get_ipython().set_next_input('importing spam');get_ipython().run_line_magic('pinfo', 'spam')


# In[ ]:


spam.bacon()

