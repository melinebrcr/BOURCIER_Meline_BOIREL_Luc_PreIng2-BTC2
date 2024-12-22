#importing modules
import matplotlib.pyplot as plt
import math
import csv

#set up the titles for our graphic
axes = plt.subplot()
axes.set_title('Fecal live bacteria')
axes.set_xlabel('Washout day')
axes.set_ylabel('log10 (live bacteria/wet g)')

#file is in reading mode
with open('filepath', 'r') as fIN:
    lines = fIN.readlines()

# for every mouse ranging from the first to the last mouse_ID, we search up the whole list everytime and we add the values of the mouse that we want in a list
for mouse in range(number of the first mouse_ID,number of the last mouse_ID +1):
    yVal=[] # corresponding bacteria for the curent targeted mouse
    xVal=[] # corresponding day for the curent targeted mouse
    for line in lines[1:]:#run all the lines except the first one
        values=line.split(';')#separates data and stock it in a list
        if values[2] == 'fecal' and int(values[4].replace('ABX0', '').strip()) == mouse:
            #adding the values to the lists
            xVal.append(int(values[7]))
            yVal.append(math.log10(float(values[8])))
            color=values[5]  # color depending on the treatment type
    if color == "placebo":
        # after acquiring all of the data of the mouse, we add it to the graph
        axes.plot(xVal, yVal, color="blue",label='Placebo') 
    else:
        axes.plot(xVal, yVal, color="orange",label='ABX')


# we used this site to help us with the legend : https://stackoverflow.com/questions/13588920/stop-matplotlib-repeating-labels-in-legend
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
axes.legend(by_label.values(), by_label.keys())
axes.grid()#grid display
plt.show()#display the graph in another window 
plt.savefig('result.png', dpi=300)
