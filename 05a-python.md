# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

> > Python lists and tuples are both indexed sets of values. Lists are mutable, which means you can access each element and change its value. Tuples are immutable, you can not change a value of a tuple element(which does not mean you can't delete or append elements to existing tuple)


> >Tuples are best to use as keys in dictionaries. Keys are hashable, which means dictionaries associate a hash values with each key that points to each key-value pair. Changing keys will change hash values, thus compromising integrity of the dictionary. Since elements of a tupple could not be changed, it is best to use the latter.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

> > Lists and sets are both a collection of values. List's elements are indexed, you can access the value of each element by using the corresponding index. Sets are not indexed.

> > Use sets to store unordered collection of values without duplicates, for example a set of all words used in an essay. Use lists to store an ordered collection of values. Searching in sets is faster than in lists, since set values are hashable.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

> > Lambda function capability allows to define an inline function. It is usually used as a callable function. See the example below:


```sorted(['Some', 'words', 'sort', 'differently'], key=lambda word: word.lower())
['differently', 'Some', 'sort', 'words']```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

> > List comprehensions provide a concise way to create lists. For example, to make new lists where each element is the result of some operations applied to each member of another iterable set or to create a subsequence of those elements that satisfy a certain condition. Consider an example below.

```>>> mylist=[1, -2, 0, -1, 5, -1.5]
>>> mylist
[1, -2, 0, -1, 5, -1.5]
>>> squares = [x**2 for x in mylist]
>>> squares
[1, 4, 0, 1, 25, 2.25]
>>> positives = [x for x in mylist if x > 0]
>>> positives
[1, 5]```



---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





