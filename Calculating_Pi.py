import random 
from math import sqrt
#defines function to calculate distance from (0,0) to randomly selected point
def dist(x,y):
    distance = sqrt(x*x + y*y)
    return distance

cnt = 0
length_of_calc = 10000000 #determines how many passes to do
output_list = [0]*length_of_calc
#more passes = more accurate, but more expensive

for i in output_list:
    if dist(random.random(),random.random()) < 1:
        #if the distance is within the unit circle, then flag
        output_list[cnt] = 1

    cnt +=1

#Here we calculate pi by comparing the ratio of points 
#in the circle to total number of points. 
ratio = sum(output_list)/len(output_list)
pi = 4*ratio

#comparing our imputed pi to the first 10 digits of pi
real_pi = 3.1415926535
print("You were %1.7f digits off" %abs(real_pi-pi))
