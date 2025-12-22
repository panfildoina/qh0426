import matplotlib.pyplot as plt
def small():
    x = [3,3,4,4,3]
    y = [3,4,4,3,3]

    plt.plot(x,y, 'r:o', label='small')  

def medium():
    x = [2,2,5,5,2]
    y = [2,5,5,2,2]

    plt.plot(x,y, 'g--s', label='medium')

def large():
    x = [1,1,6,6,1]
    y = [1,6,6,1,1]

    plt.plot(x,y, 'b-p', label='large')

def run_task_2():
    plt.figure()  #starst a new figure
    small()
    medium()
    large()
    
    plt.axis('equal') #keeps the x and y scale the same so shapes are not distorted
    plt.grid(True) #show grid (optional)
    plt.legend()  #show labels (optional)
    plt.show()
    

#makes sure the plot runs when you press Run
if __name__ == "__main__":
    run_task_2()