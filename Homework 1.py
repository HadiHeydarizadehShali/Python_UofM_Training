# This code has been written by Hadi Heydarizadeh Shali ...
# ... as the 1st python homework
"""
    Vertical Position of a trajectory
"""
import numpy              # import mathemetical library
v0 = 5                    # Initial velocity in m/s
g=9.81                    # Acceleration of gravity in m/s^2

t1= 0                     # first time in s
t2= 2                     # second time in s
   
k=0
y=[0,0]
t=[t1,t2]
for i in t:
    y[k] = v0 * i - 0.5 * g * pow(i,2) 
    k = k+1
    
print ('maximum height between t = 0 and t = 2s is',y)                  # Printing the results in a list
print('===End of the first part====')
print()

## Second Part of the Question: ##

Timespann = numpy.linspace(0,2,2000)  # build an array with 2000 time-steps between 0 and 2
lengg=numpy.size(Timespann)           # extract the size of array
y2=numpy.zeros(lengg)                 # preallocation

jj=0
for i in Timespann:
    y2[jj] = v0 * i - 0.5 * g * pow(i,2) 
    
    if y2[jj] > y2[jj-1]:              # If (conditional)
        Max_height=y2[jj]
        
        Time_of_max_height=i
    jj +=1

print('maximum height of the trajectory:',Max_height,'m')
print('time to reach the maximum height occurs in:',Time_of_max_height,'s')
