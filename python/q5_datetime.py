# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'

ds = datetime.datetime.strptime(date_start,"%m-%d-%Y")
de = datetime.datetime.strptime(date_stop,"%m-%d-%Y")
diff = de-ds
print("The difference is ",diff.days," days")

####b)  
date_start = '12312013'  
date_stop = '05282015'  

ds = datetime.datetime.strptime(date_start,"%m%d%Y")
de = datetime.datetime.strptime(date_stop,"%m%d%Y")
diff = de-ds
print("The difference is ",diff.days," days")

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

ds = datetime.datetime.strptime(date_start,"%d-%b-%Y")
de = datetime.datetime.strptime(date_stop,"%d-%b-%Y")
diff = de-ds
print("The difference is ",diff.days," days")
