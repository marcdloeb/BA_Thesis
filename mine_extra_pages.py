#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#https://campub.lib.uchicago.edu/search/?keyword=%225802+ellis%22&startDoc=21
    
    
    #https://campub.lib.uchicago.edu/search/?keyword=%22
        
    #pagenum = 20 * (n-1)
    
    


# In[ ]:





# In[ ]:





# In[1]:



import pandas, os, sys

'''

#read in file
csv_filename = "/project2/adstanle/marcdloeb/extra_csv/___.csv"

fname = os.path.basename(csv_filename)[:-4]
print(fname)

mdf = pandas.read_csv(csv_filename)

'''

# In[2]:


base_directory = "/project2/adstanle/marcdloeb/output/"


# In[21]:


out_directory = base_directory + "test_extra/"


# In[ ]:
'''

if not os.path.exists (out_directory):
    os.system ("mkdir " + out_directory)
    print ("directory " + out_directory + " created")
else:
    print ("directory exists")
    sys.exit ("stahp")

'''

# In[4]:


built_url = 'https://campub.lib.uchicago.edu/search/?keyword='

pct = "%22" #'"'


file_name = "5802_ellis@5802_S_ellis_ave"
    
street_address = file_name.split ("@")[0]

print(street_address)

total_pages = 88

for snum in range(1, total_pages):
    page_num = 20 * (snum) + 1
    extra_url = built_url + pct + street_address.replace("_","+") + pct + "&startDoc=" + str(page_num)
    print(extra_url)
    
    out_filename = "page_" + str(snum) + "_@" + street_address + ".html"
    #print (out_filename)
    
    #os.system("curl " + extra_url + " > " + out_directory + out_filename)
    sys_thing = "curl " + extra_url + " > " + out_directory + out_filename
    #os.system(syscall)
    print("--top--")
    print(sys_thing)
    print("--bot--")
    
    
    






