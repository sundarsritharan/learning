import matplotlib.pyplot as plt
from random_walk import RandomWalk

#make random walk 
rw = RandomWalk()
rw.fill_walk() 

#keep making random walks as long as the program is running
while True:
    #Plot the points in the walk 
    plt.style.use('classic')
    fig,ax = plt.subplots()
    ax.scatter(rw.x_value,rw.y_value,s=15)
    plt.show()
    
    keep_running = input("Do you want to make another walk? (y/n): " )
    if keep_running == 'n':
        break