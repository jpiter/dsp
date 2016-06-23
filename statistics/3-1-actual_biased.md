[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

> > For "number of siblings" survey, the actual and biased pmfs are compared in the plot below.

<img src="https://github.com/jpiter/dsp/blob/master/statistics/pmf_familysize.png" width="400">

> > The mean computed from the actual pmf is 1.02, and the biased mean computed from simulated responses is 2.4. As expected, since kids from families with more siblings are presented by a larger group in a sample, the actual mean gets overestimated. The code is included below.

```
import thinkplot
import thinkstats2
import chap01soln

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
    new_pmf.Normalize()
    return new_pmf

resp = chap01soln.ReadFemResp()

resp_hist= thinkstats2.Hist(resp.numkdhh)
pmf_actual = thinkstats2.Pmf(resp_hist, label='actual')
print('mean', pmf_actual.Mean())

biased_pmf = BiasPmf(pmf_actual, label='observed')
print('\nbiased mean', biased_pmf.Mean())

thinkplot.clf()
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf_actual, biased_pmf])
thinkplot.Config(xlabel='class size', ylabel='PMF')

```
