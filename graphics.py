import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from baseAlgo import *
import random
import argparse
import time
import math

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
parser.add_argument("-s", "--speed", default=1, help="set the speed of the animation (1 is default)")
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
        listGen = insertSort(listToSort)

    elif args["algorithm"].startswith('q'):
        #DO QUICKSORTING CODE HERE
        quickSort(listToSort, 0, len(listToSort)-1)


    for c in listGen:
        #time.sleep(0.3)
        plt.cla()
        #time.sleep(float(args["time"]))
        plt.bar([item for item in range(0,len(c))], c,      #draws the graph
                color = "red")      #the graph is a bar chart where each
                                #bar is a value in an array
                                #and the height of the graph is the value
        break
        
plt.title("Sorting plot") #naming the plot

if __name__ == "__main__":

    #invoke and run the animation
    animation = FuncAnimation(fig,animation_function, interval=10*float(args["speed"]))

    plt.show()
