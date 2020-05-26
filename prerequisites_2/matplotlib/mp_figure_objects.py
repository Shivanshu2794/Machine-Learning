import matplotlib.pyplot as plt

%matplotlib inline

import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

# Figure 
fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)

# Plot on the defined set of axes
axes.plot(x, y, 'b')
axes.set_xlabel('X') 
axes.set_ylabel('Y')
axes.set_title('Title')

# Creates blank canvas
f = plt.figure()

a1 = f.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
a2 = f.add_axes([0.2, 0.5, 0.4, 0.3]) # inside axes

fig,axes=plt.subplots(nrows=1,ncols=2) #subplots() using axes object 

for ax in axes:
    ax.plot(x, y, 'b')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('title')

#plt.tight_layout() # to deal with overlapping content

fig = plt.figure(figsize=(8,4), dpi=100) # figure size and dpi  


axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) 


#fig.savefig("filename.png")   #saving figure


axes.plot(x, y,'r-',label="x**2")
axes.plot(y, x, 'b',label="y**2")
axes.set_title('title');
axes.legend(loc=2)  #placing legend on figure # place can also be set using loc keyword



