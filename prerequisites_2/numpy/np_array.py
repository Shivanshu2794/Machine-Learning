import numpy as np

ls=[[1,2,3],[2,3,4]]
np.array(ls) #convert to np array

np.arange(0,10) #genrate array

# to generate array of zeros and ones
np.zeros(3)
np.ones((5,5))

np.linspace(0,5,5) #evenly spaced numbers

np.eye(5) #for identity matrix

#random module

# rand function
np.random.rand(5) #samples from uniform disribution
np.random.rand(5,5)

np.random.randn(5) # samples from normal distribution 

# randint 
np.random.randint(1,100)
np.random.randint(1,100,5) 

#array attributes

arr=np.arange(10)
arr
arr.reshape(5,2)
narr=np.random.randint(5,53,10)
print(narr)

#max and min and location 
max=narr.max()
min=narr.min()
a=narr.argmax()
print(min,max,a)

#shape
narr.shape

narr.dtype

