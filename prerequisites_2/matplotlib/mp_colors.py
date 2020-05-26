import matplotlib.pyplot as plt

%matplotlib inline

import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

#colors 

fig, ax = plt.subplots()
ax.plot(x, x**2, 'b.-') # blue line with dots
ax.plot(x, x**3, 'r--') # red dashed line

fig, ax = plt.subplots(figsize=(12,6))

# linewidth 

ax.plot(x, x+1, color="blue", linewidth=0.50)
ax.plot(x, x+2, color="red", linewidth=1.0)
ax.plot(x, x+3, color="red", linewidth=2.00)
ax.plot(x, x+4, color="orange", linewidth=4.00)

# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax.plot(x, x+ 9, color="blue", linewidth=0.50, ls='-', marker='+')
ax.plot(x, x+10, color="red", linewidth=1.0, ls='--', marker='o')
ax.plot(x, x+11, color="green", linewidth=2.0, ls='-', marker='s')
ax.plot(x, x+12, color="orange", linewidth=3.0, ls='--', marker='1')

# plt.scatter(x,y) scatter plotting


#histogram

''' from random import sample
data = sample(range(1, 1000), 100)
plt.hist(data)
'''




