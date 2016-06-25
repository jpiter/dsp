[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

> > "Random number" generator is a recurrence formula that produces a sequence of numbers, that exhibit properties of random numbers. Therefore these values are actualy pseudo-random. The pmf and cdf of 1000 values is presented below.

<img src="https://github.com/jpiter/dsp/blob/master/statistics/random_numbers2.png">


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
