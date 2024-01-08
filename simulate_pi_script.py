#Estimating the value of Pi using random numbers generator
import random

number_of_simulated_points = 10**3

inside = 0

x_inside = []
y_inside = []
x_outside = []
y_outside = []

for i in range(number_of_simulated_points):
    #Generate random point                                 
    x = random.uniform(-1.0,1.0)                    
    y = random.uniform(-1.0,1.0)

    #Check if generated point is inside/outside circle 
    if x**2+y**2 <= 1:
        inside += 1
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)

#Calculate estimated Pi    
pi = 4*inside/number_of_simulated_points

print(pi)
print("DONE")
