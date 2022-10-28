#!/usr/bin/env python
# coding: utf-8

# In[1]:


def multiply(myList):
    result = 1
    for x in myList:
        result = result * x
    return result
 
list1 = [2, 3, 6]

print(multiply(list1))

    


# In[2]:


def last(n): 
    return n[-1]  
  
def sort_list_last(tuples):  
  return sorted(tuples, key=last)  
  
print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))  


# In[3]:


d1 = {'a': 100, 'b': 200, 'c': 300}  
d2 = {'a': 300, 'b': 200, 'd':400}  
for key in d1:
    if key in d2:
        d2[key] = d1[key] + d2[key]
    else:
        d2[key]=d1[key]
print(d2)       


# In[ ]:


n = int(input("Please enter the value of n : "))
squares = {i : i*i for i in range(1, n+1)}
print(squares)


# In[ ]:




