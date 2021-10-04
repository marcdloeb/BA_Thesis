#!/usr/bin/env python
# coding: utf-8

# In[17]:


from bs4 import BeautifulSoup


# In[19]:


import os
os.getcwd()


# In[20]:


os.chdir('/project2/adstanle/marcdloeb/dates_output/south_shared/')


# In[21]:


#filename = "5801_ELLIS_@5801_S_ELLIS_AVE@.html"  #5801_ELLIS_@5801_S_ELLIS_AVE@.html


# In[22]:


import glob
import pandas

output_list = []

#mycontentz = []

for filename in glob.glob("*.html"):
    with open(filename) as f:
        mycontent = f.readlines()
        #print(mycontent)
        searchstr = '<p>Page:'
        found_divs_morepages = []
        for myz in mycontent:
            #print('==myz_top==')
            #print(myz)
            #print('==myz_end==')
            biggestnumber = 0
            if searchstr in myz:
                #found_divs_morepages.append(myz)
                #print("found searchstr")
                mynumbers = []
                #print('--=myz_top=--')
                #print(myz)
                #print('--=myz_off=--')
                soup_fdm = BeautifulSoup(myz)
                #print(soup_fdm)
                mypages = soup_fdm.findAll('a')
                for myp in mypages:
                    print(myp)
                    #print('===')
                    #print(myp.text)
                    if myp.text.isnumeric() and int(myp.text) not in mynumbers:
                        mynumbers.append(int(myp.text))
                        #print('--')
                    biggestnumber = max(mynumbers)
                    #print(biggestnumber)
                    #print('--')
                    #print(biggestnumber)
                if [filename, biggestnumber] not in output_list:
                    output_list.append([filename, biggestnumber]) #, columns='name','number')


# In[23]:


for opl in output_list:
    print(opl)


# In[86]:


#output_df = pandas.DataFrame(output_list, columns=['name','number'])


# In[87]:


#print(output_df)


# In[24]:


import csv 

csv_file = "/project2/adstanle/marcdloeb/extra_csv/south_shared_extra.csv"

file = open(csv_file, 'w+', newline ='')

with file:     
    write = csv.writer(file) 
    write.writerows(output_list) 


# In[ ]:




