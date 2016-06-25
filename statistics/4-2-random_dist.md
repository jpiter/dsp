[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

> >

```
random.seed(a = 120)
val=[]
for i in range(1000):
    val.append(random.random())

thinkplot.clf()
thinkplot.PrePlot(cols = 2)

d_rand = thinkstats2.Hist(val)

pmf_rand = thinkstats2.Pmf(d_rand)
thinkplot.Pmfs([pmf_rand])
thinkplot.Config(xlabel='random values', ylabel='PMF')

cdf_rand = thinkstats2.Cdf(d_rand)
thinkplot.SubPlot(2)
thinkplot.Cdf(cdf_rand)
thinkplot.Config(xlabel='random values', ylabel='CDF')
```
