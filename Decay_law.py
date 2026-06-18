"""The aim is to visualize decay law using simulation"""
import numpy as np
import matplotlib.pyplot as plt
import math 
# 1: Not decayed , 0: Decayed
n = 50 #Matrix dimensions nxn
half_life = 5

lamda = math.log(2)/half_life
print(lamda)
grid = np.ones((n,n))
dt = 0.1 #sec
rand_grid = np.ones((n,n))
size = n*n
initial = size*math.exp(-1*lamda*dt)
alive = np.count_nonzero(grid)

plt.ion()
fig, ax = plt.subplots()
t = 2
time = [dt]
alive_list = [alive]
real = [initial]
while alive >= 1:

    alive = np.count_nonzero(grid)

    ax.clear()

    im = ax.imshow(grid, cmap="RdYlGn")

    ax.set_title(f"t = {dt:.1f}")
    
    plt.pause(t)   
    t = 0.5


    
    for i in range(n):
        for j in range(n):
            if grid[i,j] != 0:
                probab_alive = np.random.binomial(grid[i,j], np.exp(-1*lamda*dt))
                probability_of_decay = 1 - probab_alive
                
                rand_grid[i,j] = probab_alive
                
            if grid[i,j] == 0:
                rand_grid[i,j] = 0

    dt += 0.1
    grid = rand_grid
    alive_list.append(np.count_nonzero(rand_grid))
    real.append( size*math.exp(-1*lamda*dt))
    time.append(dt)

plt.close()      # close animation window

plt.ioff()       # leave interactive mode

plt.figure()     # NEW figure

plt.scatter(time, alive_list)
plt.scatter(time,(np.array(alive_list)*np.exp(-1*lamda*np.array(time))),label = "Formula")

plt.xlabel("Time")
plt.ylabel("Alive nuclei")
plt.legend()
plt.grid()
plt.show()
print(alive_list)
print("____________________________")
print((alive_list[0]*np.exp(-1*lamda*np.array(time))))




