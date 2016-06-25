[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

> > 34.27% male population can be accepted to Blue Men Group. The code is below.

```
import scipy.stats

# 5'10'' feet is close to 177.8cm.
lb = scipy.stats.norm.cdf(177.8, loc=178, scale=7.7)

# 6'1'' feet is close to 185.42cm.
ub = scipy.stats.norm.cdf(185.42, loc=178, scale=7.7)

percentage = round((ub - lb)* 100, 2)

print("Percentage of population that can be accepted to Blue Men group is ", percentage,"%")

```
