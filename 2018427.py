# 作业：请采用leastsq拟合一条曲线
# y=a*x*x + b*x +c
#
# X:  0,1,2,3,-1,-2,-3
# Y: -1.22,1.85,3.22,10.29,2.21,3.72,8.7
#
# 请尝试写出程序，与课堂上相比，多了一阶。
# 请进一步学习
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.leastsq.html，请理解调用中的func, x0, args三个关键参数。


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
plt.figure(figsize=(9,9))

x=np.linspace(-4,4,1000)
X=np.array([0.,1.,2.,3.,-1.,-2.,-3.])
Y=np.array([-1.22,1.85,3.22,10.29,2.21,3.72,8.7])

def f(p):
    a,b,c=p
    return(Y-(a*X*X + b*X +c))

r=leastsq(f,[1,0,0])
a,b,c=r[0]
print('a=',a,'b=',b,'c=',c)

plt.scatter(X,Y,s=100,alpha=1.0,marker='o',label=u'数据点') #散点图 原数据

y=a*x*x + b*x +c
ax=plt.gca()

ax.set_xlabel(..., fontsize=20)
ax.set_ylabel(..., fontsize=20)
#设置坐标轴标签字体大小

plt.plot(x, y, color='r',linewidth=5, linestyle=":",markersize=20, label=u'拟合曲线')

plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='xx-large')

plt.xlabel(u'X')
plt.ylabel(u'Y')

plt.xlim(-5, x.max() * 1.1)
plt.ylim(-2, y.max() * 1.1)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#刻度字体大小
plt.legend(loc='upper left')

plt.show()