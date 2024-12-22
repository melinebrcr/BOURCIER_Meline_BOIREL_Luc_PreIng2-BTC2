#importing modules
import matplotlib.pyplot as plt
import math
import csv

#set up the titles for our graphic
fig, axes = plt.subplots()
axes.set_title('Ileal live bacteria')
axes.set_xlabel('Treatment')
axes.set_ylabel('log10 (live bacteria/wet g)')

positions=[1,3] # sapce out graphics
#file is in reading mode
with open('filepath', 'r') as fIN:
    lines = fIN.readlines()

linesFilteredIlealPlacebo=[] # values for the ileal sample with placebo treatment
linesFilteredIlealABX=[]#values for the ileal sample with ABX
for line in lines[1:]:#run all the lines except the first one
    values=line.split(";")#separates data and stock it in a list
    if int(values[7])==0: # corresponding to the 7th day of the experience
        if values[2] in "ileal" and values[5]=="placebo": # check if the sample is ileal and if the treatment used is the placebo
            linesFilteredIlealPlacebo.append(math.log10(float(values[8])))
        elif values[2] in "ileal" and values[5]=="ABX": # check if the sample is ileal and if the treatment used is the cocktail
            linesFilteredIlealABX.append(math.log10(float(values[8]))) #add bacteria
#we obtain two lists, one with the values for the placebo treatment and the other for ABX


#source : https://matplotlib.org/stable/gallery/statistics/customized_violin.html#sphx-glr-gallery-statistics-customized-violin-py
violin= axes.violinplot([linesFilteredIlealABX,linesFilteredIlealPlacebo],showextrema=True,positions=positions, widths=2) # creation des 2 violons, determination des extremats,des positions des grapiques et de la taille

#set up the color of the graphics 
i=0
colors=['orange','blue']
for body in violin['bodies']:
    body.set_color(colors[i])
    i+=1
    

#display the points
x=[1]*len(linesFilteredIlealABX)#x is used to place the points
axes.scatter(x, linesFilteredIlealABX)
x=[3]*len(linesFilteredIlealPlacebo)
axes.scatter(x, linesFilteredIlealPlacebo)

axes.legend(labels=['ABX','Placebo'])#set up the legend
axes.grid()#display the grid
plt.show()#display the graphic in another window 
plt.savefig('result.png', dpi=300)
