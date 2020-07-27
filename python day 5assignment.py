#!/usr/bin/env python
# coding: utf-8

# In[5]:


list1=[(10,4),(2,1),(6,7),(2,6)]
def func1(x):
    return x[0]+x[1]
list1.sort(key=func1)
print(list1)


# In[25]:


list1=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
list2=[]
list1.sort()

for each in list1[:]:
    if each==0:
         list1.remove(each)
         list2.append(each)
print(list1+list2)


# In[37]:


list1=[10,20,40,60,70,80]
list2=[5,15,25,35,45,60]

size1=len(list1)
print(size1)


# In[41]:


list1=[10,20,40,60,70,80]
list2=[5,15,25,35,45,60]
list3=[]
size1=len(list1)
size2=len(list2)
res=[]
i=0
j=0
while i<size1 and j<size2:
    if list1[i]<list2[j]:
        res.append(list1[i])
        i+=1
        
    else:
        res.append(list2[j])
        j+=1
res=res+list1[i:]+list2[j:]
print(res)


# In[ ]:




