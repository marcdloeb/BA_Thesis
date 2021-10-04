#!/usr/bin/env python
# coding: utf-8

import pandas, os, sys

#read in file
csv_filename = "/project2/adstanle/marcdloeb/csv_v3/east_repeated_w_suffix_769-795.csv"

fname = os.path.basename(csv_filename)[:-4]
print(fname)

mdf = pandas.read_csv(csv_filename)

'''
#check 1
print ("Head")
print(mdf.head(10))

#check 2
print ("Combined Name")
print(mdf["combined_name"][1])

#check 3
print ("Data Types")
print(mdf.dtypes)

print ("=====")
print ("")
'''

#####

base_directory = "/project2/adstanle/marcdloeb/output/"

out_directory = base_directory + fname +"/"

#ie "/project2/adstanle/marcdloeb/output/project2/adstanle/marcdloeb/csv_v3/east_repeated_w_suffix_769-795.csv/"

if not os.path.exists (out_directory):
    os.system ("mkdir " + out_directory)
    print ("directory " + out_directory + " created")
else:
    print ("directory exists")
    sys.exit ("stahp")

#sys.exit ("extra stahp")

#####

#built_url = "http://campub.lib.uchicago.edu/search/?keyword="

built_url = 'https://campub.lib.uchicago.edu/search/?keyword='

pct = "%22"
#this is the html stand in for '"'


for index, row in mdf.iterrows():

    street_name = row["combined_name"]
    streetnum_min = row["min_add_num"]
    streetnum_max = row["max_add_num"]

    for snum in range(streetnum_min, streetnum_max + 1):

        address_str = str(snum) + " " + street_name

        #print(address_str)

        out_filename = address_str.replace(" ","_") + "_@" + str(snum) + "_" + row["official_name"].replace(" ","_") + "@" + ".html"  # e.g. "9050_S_ABBOTT_av_@9050_S_ABBOTT_AVE@.html"

        print(out_filename)

        # jump in and reset built_url (for testing)
        #address_str = "5301 ELLIS"

        addr_url = built_url + pct + address_str.replace(" ","+") + pct

        print(addr_url)

        os.system("curl " + addr_url + " > " + out_directory + out_filename)

        #os.system("curl " + built_url + pct + address_str.replace(" ","+") + pct + " > " + out_directory + out_filename)

        #sys.exit("stop_after_1")
