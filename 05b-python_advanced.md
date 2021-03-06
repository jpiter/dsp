## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

> > Different degrees are MPH, MD, MA, BSEd, MS, ScD, JD, PhD. There is also one rogue entry that did not have a value.


```{'MPH': 2, 'MD': 1, 'MA': 1, 'BSEd': 1, 'MS': 2, 'ScD': 6, 'JD': 1, 'PhD': 31, '0': 1}```


####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

> > There are essentially three titles Professor of Biostatistics, Assistant Professor of Biostatistics and Associate Professor of Biostatistics. One entry had a typo in the title  - "Assistant professor is Biostatistics". The summary is below, fixing the typo will change number of Assistant Professors of Biostatistics to 12.

``` {'Professor of Biostatistics': 13, 'Assistant Professor of Biostatistics': 11, 'Associate Professor of Biostatistics': 12, 'Assistant Professor is Biostatistics': 1}```


####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.


```
Email List:

bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
jinboche@upenn.edu
sellenbe@upenn.edu
jellenbe@mail.med.upenn.edu
ruifeng@upenn.edu
bcfrench@mail.med.upenn.edu
pgimotty@upenn.edu
wguo@mail.med.upenn.edu
hsu9@mail.med.upenn.edu
rhubb@mail.med.upenn.edu
whwang@mail.med.upenn.edu
mjoffe@mail.med.upenn.edu
jrlandis@mail.med.upenn.edu
liy3@email.chop.edu
mingyao@mail.med.upenn.edu
hongzhe@upenn.edu
rlocalio@upenn.edu
nanditam@mail.med.upenn.edu
knashawn@mail.med.upenn.edu
propert@mail.med.upenn.edu
mputt@mail.med.upenn.edu
sratclif@upenn.edu
michross@upenn.edu
jaroy@mail.med.upenn.edu
msammel@cceb.med.upenn.edu
shawp@upenn.edu
rshi@mail.med.upenn.edu
hshou@mail.med.upenn.edu
jshults@mail.med.upenn.edu
alisaste@mail.med.upenn.edu
atroxel@mail.med.upenn.edu
rxiao@mail.med.upenn.edu
sxie@mail.med.upenn.edu
dxie@upenn.edu
weiyang@mail.med.upenn.edu
```


####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.


```
Unique domains:

mail.med.upenn.edu
upenn.edu
cceb.med.upenn.edu
email.chop.edu
```

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

> > The file emails.csv is in dsp/python/ folder


### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:

> > I am printing 5 entries. I had to do a work around in order for the last name Ellenberg to work.

```
Bellamy :  ['ScD', 'Associate Professor', 'bellamys@mail.med.upenn.edu']
Bilker :  ['PhD', 'Professor', 'warren@upenn.edu']
Bryan :  ['PhD', 'Assistant Professor', 'bryanma@upenn.edu']
Chen :  ['PhD', 'Associate Professor', 'jinboche@upenn.edu']
Ellenberg :  [['PhD', 'Professor', 'sellenbe@upenn.edu'], ['PhD', 'Professor', 'jellenbe@mail.med.upenn.edu']]
```


####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```

Print the first 3 key and value pairs of the dictionary:

```
('Knashawn', 'Morales') :  ['ScD', 'Associate Professor', 'knashawn@mail.med.upenn.edu']
('Sharon', 'Xie') :  ['PhD', 'Associate Professor', 'sxie@mail.med.upenn.edu']
('Pamela', 'Shaw') :  ['PhD', 'Assistant Professor', 'shawp@upenn.edu']
```

> > Question to Reshama: Would applying regex fix my fourth entry? Why does my dictionary not printing by first name?(Q8)


```('J.', 'Landis') :  ['BSEd MS PhD', 'Professor', 'jrlandis@mail.med.upenn.edu']```



####Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

```
('Scarlett', 'Bellamy') :  ['ScD', 'Associate Professor', 'bellamys@mail.med.upenn.edu']
('Warren', 'Bilker') :  ['PhD', 'Professor', 'warren@upenn.edu']
('Matthew', 'Bryan') :  ['PhD', 'Assistant Professor', 'bryanma@upenn.edu']
```

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

