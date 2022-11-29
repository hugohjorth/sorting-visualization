import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from baseAlgo import *
import random

#the total number of elements in the array
elementsToSort = 1000

fig = plt.figure(figsize=(10,10))
axes = fig.add_subplot(1,1,1)

#the range of values the y-axis can have
axes.set_ylim(0,elementsToSort)

#creates and fills a list with ints (1 - lenght)
#then randomly shuffles the list
def createList(lenght):
    list = []
    for i in range(1,lenght+1):
        list.append(i)
    
    random.shuffle(list)
    return list

listToSort = createList(elementsToSort)
x = []
for i in range(1,len(listToSort)+1):
    x.append(i)

#main animation function
def animation_function(i):
    global listToSort
    if i < len(listToSort):
        insertSort(listToSort,i)
    
    #listToSort = quickSort(listToSort, 0, len(listToSort)-1)
    plt.cla() #clears the graph
    plt.bar(x, listToSort,      #draws the graph
            color = "red")      #the graph is a bar chart where each
                                #bar is a value in an array
                                #and the height of the graph is the value

plt.title("Sorting plot") #naming the plot

#invoke and run the animation
animation = FuncAnimation(fig,animation_function, frames=elementsToSort)

plt.show()