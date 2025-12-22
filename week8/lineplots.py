import matplotlib.pyplot as plt
def coordinate():
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))
    return(x,y)

def path():
    print("Retriving path...")
    x_values = []
    y_values = []

    for i in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])

    return [x_values, y_values]

def run_task3():
    values = path()
    plt.plot(values[0], values[1], 'r--o') #draws line with red dashed line
    plt.xlabel("X values")
    plt.ylabel("Y values") 
    plt.title("Path Plot")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    run_task3()
