#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ASSIGNMENT-1
port1={21:"FTP",22:"SSH",23:"telnet",80:"http"}
print(port1)
port1={value:key for key,value in port1.items()}
port2=dict([(key,value) for key ,value in port1.items()])
print(port2)
print(port1)


# In[2]:


#ASSIGNMENT-2
list1=[(1,2),(3,4),(5,6),(4,5)]
for each in list1:
    list2=sum(list(each))
    print(list2)


# In[3]:


#ASSIGNMENT3
list3=[(1,2,3),[1,2],['a','hit','less']]
list4=[item for each in list3 for item in each]
print(list4)


# In[ ]:




