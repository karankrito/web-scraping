#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from requests import get


# In[2]:


name=[]
rating=[]
votes=[]
gross=[]
years=[]
y=[]
for i in range(2000,2023):
    years.append(i)
for year in years:
    for i in range(20):
        response=get("https://www.imdb.com/search/title/?release_date="+str(year)+"&sort=num_votes,desc&start="+str(i*50+1))
        kn=BeautifulSoup(response.text,"html.parser")
        krito=kn.find_all('div',class_="lister-item-content")
        for i in krito:
            name.append(i.h3.a.text)
            rating.append(i.strong.text)
            y.append(year)
            votes.append(i.find('span', attrs = {'name':'nv'})['data-value']) 
            g=i.find('p', attrs = {'class':'sort-num_votes-visible'})
            t=0
            if len(g)==11:
                for i in g:
                    if t==9:
                        gross.append(i.text)
                    t+=1
            else:
                gross.append("not known")


# In[3]:


for i in name:
    if "'" in i:
        print(i)


# In[4]:


for i in range(len(name)):
    if "'" in name[i]:
        name[i]=name[i].replace("'","")
        
name


# In[6]:


import pandas as pd
df=pd.DataFrame({"name":name,
                 "year":y,
               "rating":rating,
               "votes":votes,
               "gross":gross})
df


# In[9]:


import pymysql


# In[17]:


try:
    con=pymysql.connect(user="root",password="root",host="localhost",database="krito")
    cursor=con.cursor()
except:
    print("error")
cursor.execute("use krito;")
record = cursor.fetchone()
    #print("You're connected to database: ", record)
cursor.execute('DROP TABLE IF EXISTS imdb;')
print('Creating table....')
sql1= """CREATE TABLE imdb(
    movie varchar(255),
    year int,
    rating float,
    votes int,
    gross varchar(255)
    );"""
cursor.execute(sql1)
for i in range(len(df)):
            #here %S means string values 
            sql = "INSERT INTO imdb VALUES ('%s',%s,%s,%s,'%s');"%(df["name"][i],df["year"][i],df["rating"][i],df["votes"][i],df["gross"][i])
            #print(sql)
            cursor.execute(sql)
            #print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            con.commit()


# In[26]:


try:
    k=pd.read_csv("C:\\Users\\user\\Downloads\\project1.csv")
except:
    print("error")


# In[25]:


df.to_csv("project1.csv")


# In[23]:




