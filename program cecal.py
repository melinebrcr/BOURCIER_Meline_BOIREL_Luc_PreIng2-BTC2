#importing modules
import matplotlib.pyplot as plt
import math
import csv

#set up the titles for our graphic
fig, axes = plt.subplots()
axes.set_title('Cecal live bacteria')
axes.set_xlabel('Treatment')
axes.set_ylabel('log10 (live bacteria/wet g)')

positions=[1,3] # sapce out graphics
#file is in reading mode
with open('filepath', 'r') as fIN:
    lines = fIN.readlines()

linesFilteredCecalPlacebo=[] # values for the cecal sample with placebo treatment
linesFilteredCecalABX=[]#values for the ileal sample with ABX
for line in lines[1:]:#run all the lines except the first one
    values=line.split(";")#separates data and stock it in a list
    if int(values[7])==0: # corresponding to the 7th day of the experience 
        if values[2] in "cecal" and values[5]=="placebo": # check if the sample is cecal and if the treatment used is the placebo
            linesFilteredCecalPlacebo.append(math.log10(float(values[8])))
        elif values[2] in "cecal" and values[5]=="ABX": # check if the sample is cecal and if the treatment used is the cocktail
            linesFilteredCecalABX.append(math.log10(float(values[8]))) #add bacteria
#we obtain two lists, one with the values for the placebo treatment and the other for ABX


#source :https://matplotlib.org/stable/gallery/statistics/customized_violin.html#sphx-glr-gallery-statistics-customized-violin-py
violin= axes.violinplot([linesFilteredCecalABX,linesFilteredCecalPlacebo],showextrema=True,positions=positions, widths=2) # creation des 2 violons, determination des extremats,des positions des grapiques et de la taille

#set up the color of the graphics
i=0
colors=['orange','blue']
for body in violin['bodies']:
    body.set_color(colors[i])
    i+=1
    
#display the points
x=[1]*len(linesFilteredCecalABX)#x is used to place the points 
axes.scatter(x, linesFilteredCecalABX)
x=[3]*len(linesFilteredCecalPlacebo)
axes.scatter(x, linesFilteredCecalPlacebo)

axes.legend(labels=['ABX','Placebo'])#set up the legend
axes.grid()#display the grid
plt.show()#display the graph in another window 
plt.savefig('result.png', dpi=300)
