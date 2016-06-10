# # # Q1: Degree Data # # #

f=open('faculty.csv')
csv_f = csv.reader(f)
csv_data = list(csv_f)
f.close()

# define keys to be headers of the data table
keys = csv_data[0]
# transpose data table to prep for creating a dictionary
info = list(map(list, zip(*csv_data[1:]))) #games' statistics, transpose of the original data record, as a list of lists
# create a dictionary
d = dict(zip(keys,info)) 
#read the column with the degree information
parsed_degree = d[' degree']

# define a function which "cleans" the list of strings: removes whitespaces, dots, 
# separates ocasional one cell multiples entries, returns a list
def clean_data(parsed_data):
    parsed_data =[x.strip() for x in parsed_data]
    parsed_data =[x.replace(".","") for x in parsed_data]
    
    new_list=[]

    for x in parsed_data:
        if x.isalnum():
            new_list.append(x)
        else:
            t = x.split()
            new_list.extend(t)
            
    return new_list

# clean degree data 
degree = clean_data(parsed_degree)

#create a set of unique values
unique_degree = set(degree)

#create a dictionary where keys are degrees and corresponding values are frequencies
degree_dict = {x: degree.count(x) for x in unique_degree}

# # # Q2 # # #
parsed_title = d[' title']
parsed_title = [str(x) for x in parsed_title]
unique_title = set(parsed_title)

title_dict = {x: parsed_title.count(x) for x in unique_title}

parsed_email =d[' email']
parsed_email = [str(x) for x in parsed_email]
print("\nEmail List:\n")
for x in parsed_email:
    print(x)

domains=[]
for x in parsed_email:
    ind = x.index("@")
    domains.append(x[ind+1:])
unique_domains = set(domains)
print("\nUnique domains:\n")
for x in unique_domains:
    print(x)
