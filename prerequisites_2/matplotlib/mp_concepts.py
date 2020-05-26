import matplotlib.pyplot as plt

%matplotlib inline

import numpy as np

x=np.linspace(0,10,10)
y=x**2

plt.plot(x,y,'r-')  # r- is colour
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Title')
#plt.show() # no need to write in jupyter


# subplot -> multiplots on same canvas
plt.subplot(1,2,1)
plt.plot(x, y, 'r-') 
plt.subplot(1,2,2)
plt.plot(y, x, 'g-');
