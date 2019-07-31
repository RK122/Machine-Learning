# matplotlib -- library for graph -- same as matlab's plot
import matplotlib.pyplot as plt

# plt.plot(x,y) -- x = list of x-axis pts & y = list of y-axis pts
plt.plot([1,2,3,4],[1,4,9,16])
plt.xlabel('indices')
plt.ylabel('squares')
plt.title('g1')
plt.show()

# if only one argument is given = y & x's list = [0,1,2, ....]
plt.plot([1,4,9,16])
plt.xlabel('indices')
plt.ylabel('squares')
plt.title('g1')
plt.show()

plt.plot([1,2,3,4],[1,4,9,16])
plt.xlabel('indices')
plt.ylabel('squares')
plt.title('g1')
plt.grid() # for grid lines
plt.show()

# linewidth = width of line to set
plt.plot([1,2,3,4],[1,4,9,16],'ro',linewidth=5) # r for red & o for o-shaped dots -- no lines only dots
plt.xlabel('indices')
plt.ylabel('squares')
plt.title('g1')
plt.grid()
plt.show()

# b-- = blue line of --
# rs = red line of squares
# g^ = grenn line of triangles
# label = little information about line
# legend = to show labels
from numpy import arange
t=arange(0.0,5.0,0.2)
plt.plot(t,t**2,'b--',label='^2')
plt.plot(t,t**2.2,'rs',label='^2.2')
plt.plot(t,t**2.5,'g^',label='^2.5')
plt.legend()
plt.show()

# color = 'g' -- for color
x1=[1,2,3,4]
y1=[1,2,3,4]
x2=[1.5,2.2,3.6,4.4]
y2=[1.5,2.2,3.6,4.4]
lines=plt.plot(x1,y1,x2,y2)
plt.setp(lines[0],color='r',linewidth=2.3)
plt.setp(lines[1],color='g',linewidth=3.6)
plt.grid()


# figure & subplots

plt.figure(1) # it will create a figure numbered 1
plt.subplot(211) # it that figure, subplot divides that plot in 2 rows , 1 col & other 1 is for switching
# means now we are in upper part
plt.plot([1,2,3,4]) # this plot will be draw in upper part

plt.subplot(212) # means now we are in lower plot
plt.plot([1,4,9,16])

plt.figure(2) # another figure = another plot -- not attached with figure 1
plt.subplot(221) # means it will divide the figure 2 in 4 parts -- & now we are in 1st part
plt.plot([1,2**0.5,3**0.5,4**0.5])

plt.subplot(222) # we are in 2nd part
plt.plot([1,2**2,3**2,4**2])

plt.subplot(223) # we are in 3rd part
plt.plot([1,2**2.2,3**2.2,4**2.2])

plt.subplot(224) # we are in 4th part
plt.plot([1,2**2.5,3**2.5,4**2.5])

# using figure we can jump on any figure on any time
plt.figure(1)
plt.subplot(212)
plt.title('dknks')
plt.grid()
plt.show()

