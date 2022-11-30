import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from baseAlgo import *
import random
import argparse

#Code for argument parsing
argDesc = "Visualize a algorithm"

parser = argparse.ArgumentParser(formatter_class =
argparse.RawDescriptionHelpFormatter, description=argDesc)

#all the different valid algorithm arguments to use
#aka arguments without flag
functionMap = ['insertsort', 'quicksort']

parser.add_argument("algorithm", choices=functionMap,help="Algorithm to use")
#flag n is the size of the array
parser.add_argument("-n", "--number", default=20, help="Number of elements to sort")
args = vars(parser.parse_args())

#the total number of elements in the array
elementsToSort = int(args["number"])

#some values for the creation of the graph
fig = plt.figure(figsize=(10,10))
axes = fig.add_subplot(1,1,1)

#the range of values the y-axis can have
axes.set_ylim(0,elementsToSort)

#creates and fills a list with ints (1 -> lenght)
#then randomly shuffles the list
def createList(lenght):
    list = []
    for i in range(1,lenght+1):
        list.append(i)
    
    random.shuffle(list)
    return list

#The list to sort
listToSort = createList(elementsToSort)
#main animation function
def animation_function(i):
    global listToSort

    if args["algorithm"].startswith('i'):  
        if i < len(listToSort):
            insertSort(listToSort,i)
    elif args["algorithm"].startswith('q'):
        #DO QUICKSORTING CODE HERE
        pass
    
    plt.cla() #clears the graph
    plt.bar([item for item in range(1,len(listToSort)+1)], listToSort,      #draws the graph
            color = "red")      #the graph is a bar chart where each
                                #bar is a value in an array
                                #and the height of the graph is the value

plt.title("Sorting plot") #naming the plot

#invoke and run the animation
animation = FuncAnimation(fig,animation_function, frames=elementsToSort)

plt.show()