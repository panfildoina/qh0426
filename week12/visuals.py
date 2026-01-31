#1

import matplotlib.pyplot as plt          # Import matplotlib pyplot for plotting

def triangle():
    # Plot a blue triangle with a dashed line and pentagon markers
    x = [0, 1, 2, 0]                      # X-coordinates of the triangle
    y = [0, 5, 0, 0]                      # Y-coordinates of the triangle
    plt.plot(x, y, 'b--p')                # Blue (b), dashed (--), pentagon marker (p)

def left_rectangle():
    # Plot a green rectangle on the left with a solid line and triangle markers
    x = [0, 0, 1, 1, 0]                   # X-coordinates of the left rectangle
    y = [4, 5, 5, 4, 4]                   # Y-coordinates of the left rectangle
    plt.plot(x, y, 'g-^')                 # Green (g), solid (-), triangle marker (^)

def right_rectangle():
    # Plot a red rectangle on the right with a dotted line and square markers
    x = [1, 1, 2, 2, 1]                   # X-coordinates of the right rectangle
    y = [4, 5, 5, 4, 4]                   # Y-coordinates of the right rectangle
    plt.plot(x, y, 'r:s')                 # Red (r), dotted (:), square marker (s)

def run():
    triangle()                            # Draw the triangle
    left_rectangle()                     # Draw the left rectangle
    right_rectangle()                    # Draw the right rectangle
    plt.show()                            # Display the plot window

run()                                     # Run the program


#2

import matplotlib.pyplot as plt                 # Import matplotlib for plotting


def draw_pentagon():
    """Draws a blue pentagon with a dashed line and pentagon markers"""
    x = [2, 4, 6, 5, 3, 2]                      # X-coordinates of the pentagon
    y = [4, 7, 4, 1, 1, 4]                      # Y-coordinates of the pentagon
    plt.plot(x, y, 'b--p')                     # Blue, dashed line, pentagon markers


def draw_triangle():
    """Draws a green triangle with a solid line and triangle markers"""
    x = [3.5, 4.5, 5.5, 3.5]                    # X-coordinates of the triangle
    y = [4, 6, 4, 4]                            # Y-coordinates of the triangle
    plt.plot(x, y, 'g-^')                      # Green, solid line, triangle markers


def draw_rectangle():
    """Draws a red rectangle with a dotted line and square markers"""
    x = [3.5, 5.5, 5.5, 3.5, 3.5]               # X-coordinates of the rectangle
    y = [2, 2, 3, 3, 2]                         # Y-coordinates of the rectangle
    plt.plot(x, y, 'r:s')                      # Red, dotted line, square markers


def run():
    """Runs the program and displays the plot"""
    draw_pentagon()                             # Draw the pentagon
    draw_triangle()                             # Draw the triangle
    draw_rectangle()                            # Draw the rectangle

    plt.title("Pentagon, Triangle and Rectangle")  # Add a title
    plt.xlabel("X-axis")                         # Label the X-axis
    plt.ylabel("Y-axis")                         # Label the Y-axis

    plt.show()                                  # Display the plot window


run()                                           # Call the run function to execute the program



import matplotlib.pyplot as plt

def run():
    fig = plt.figure()
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)

    n = int(input("Enter number of students: "))
    c_s = ([5,6,1], [7,1,3])
    ms = {“HP”:5, “Hercules”:3}
    ss = {“Rap”:8, “Pop”:4 }

    ax1.plot(c_s[0], c_s[1], "rx")
    ax1.set_xlabel("Coffee intake (cups per day)")
    ax1.set_ylabel("Sleep in hours/night")
    ax1.set_title("Coffee vs Sleep")

    ax2.pie(ms.values(), labels = ms.keys(), autopct = "%.f%%")

    ax3.pie(ss.values(), labels = ss.keys(), autopct = "%1.1f%%")
    ax3.set_title("Music preference")

    ax4.bar(["Micky Mouse", "Donald Duck"], [6, 10])

    plt.show()