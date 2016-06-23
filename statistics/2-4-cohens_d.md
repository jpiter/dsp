[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

> > First, I plotted two superimposed histograms. Since each different value works as a class, for totalwgt_lb there are too many bins, and the histograms are not easy to compare. It does look that two data sets are not much different. The pictures is attached below.


![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

> > The Cohen's d size effect,  is -0.0887 which is considered to be very small. So there is no difference in weight between first and other babies.

```
import nsfg
import thinkplot
import thinkstats2


df = nsfg.ReadFemPreg()

live = df[df.outcome == 1]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

first_hist = nsfg.thinkstats2.Hist(firsts.totalwgt_lb, label = "first babies")
other_hist = nsfg.thinkstats2.Hist(others.totalwgt_lb, label = "siblings")

w = 0.05
thinkplot.clf()
thinkplot.preplot(2, cols = 2)
thinkplot.Hist(first_hist, align='right', width=w)
thinkplot.Hist(other_hist, align='left', width=w)
thinkplot.Config(xlabel='lb', ylabel='frequency')

cd_effect = nsfg.thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
print("Cohen's d = ", cd_effect)
```
