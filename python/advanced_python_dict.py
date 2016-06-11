import os
import csv


#os.chdir('/Users/jpiterbarg/ds/metis/prework/dsp/python/')

f=open('faculty.csv')
csv_f = csv.reader(f)
csv_data = list(csv_f)
f.close()

keys = csv_data[0]
#games' statistics, transpose of the original data record, as a list of lists
info = list(map(list, zip(*csv_data[1:]))) 
#dictionary by type of data('name',' degree', ' title', 'email')
d = dict(zip(keys,info)) 

#Q
parsed_degree = d[' degree']

# removes white spaces and "."
def clean_degree(parsed_data):
    parsed_data =[x.strip() for x in parsed_data]
    parsed_data =[x.replace(".","") for x in parsed_data]
    
    return parsed_data

degree = clean_degree(parsed_degree)

parsed_title = d[' title']
parsed_title = [str(x) for x in parsed_title]
t=[x.replace('of Biostatistics','') for x in parsed_title]
short_title = [x.strip() for x in t]

parsed_email=d[' email']

parsed_name =d['name']
full_name = [ x.split(sep=' ') for x in parsed_name]
last_name=[x[-1] for x in full_name]
unique_last_name = set(last_name)

faculty=list(zip(last_name, degree, short_title, parsed_email))

seen=[]
dict_entry=[]

# I had to do this work around since keys should
# have unique entries.
# If there already an entry for the key, I am creating
# a new entry for the key that is a list of lists
for x in faculty:
    if x[0] in seen:
        ind = seen.index(x[0])
        dict_entry[ind]=[dict_entry[ind],list(x[1:])]
    else:
        seen.append(x[0])
        dict_entry.append(list(x[1:]))

#tuple_for_dict=tuple(zip(last_name, dict_entry))
#
faculty_dict =dict(zip(seen,dict_entry))

for key in sorted(faculty_dict.items()):
    print(key[0],": " ,key[1])
    
#Q7
#create a list of tuple of first and last names
faculty=[]

first_last_name = [(x[0],x[-1]) for x in full_name]
faculty=list(zip(first_last_name,degree, short_title, parsed_email))

professor_dict ={x[0]:list(x[1:]) for x in faculty}

for x,v in professor_dict.items():
    print(x, ": ",v)

#Q8
for x,v in sorted(professor_dict.items(), key = lambda x: x[0][1]):
    print(x, ": ",v)
    
    

    



