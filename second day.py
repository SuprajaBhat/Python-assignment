#!/usr/bin/env python
# coding: utf-8

# In[3]:


x=y=10
z=20
print("x is %d y is %d z is %d"%(x,y,z))
id(x)
id(y)


# In[4]:


id(y)


# In[5]:


del x


# In[6]:


id(x)


# In[7]:


id(y)


# In[8]:


y=x
id(x)


# In[9]:


x=5**2
print(x)


# In[12]:


x=10//4
print(x)


# In[13]:


10/2


# In[14]:


10//2


# In[15]:


10%3


# In[16]:


a=10
b=20
a==b


# In[17]:


a<=b


# In[18]:


a>=b


# In[19]:


a!=b


# In[20]:


a+=a


# In[21]:


a=a+10


# In[24]:


str="Python"
"a" not in str


# In[25]:


"y"not in str


# In[26]:


str="Python"
"a"  in str


# In[27]:


"y" in str


# In[28]:


a=b=10
a==b


# In[29]:


a is b


# In[30]:


id(a)==id(b)


# In[31]:


x=y
x=1.5
id(x)==id(y)


# In[32]:


x=1
y=1
x==y
id(x)==id(y)


# In[33]:


id(x)==id(y)


# In[34]:


x is y


# In[35]:


a=10


# In[36]:


b=10


# In[37]:


a is b


# In[38]:


a=1.6
b=1.6
a is b


# In[39]:


id(a)==id(y)


# In[40]:


id(a)


# In[41]:


id(b)


# In[42]:


a=257
b=257
a is b


# In[43]:


10//20*2


# In[44]:


10/20*2


# In[45]:


20//2*5+9//3


# In[46]:


2^1


# In[ ]:




