import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
pop = np.loadtxt(open("india-districts-census-2011.csv", "rb"), delimiter=",",skiprows=1, dtype=object)
k=1
population=[]
states=[]
state_comp=[]
comp=[]
state_internet=[]
internet=[]
comp_ratio=[]
int_ratio=[]
for i in range(0, 640):
    if(int(pop[i,0])==k):
        comp.append(int(pop[i,37]))
        internet.append(int(pop[i,36]))
    elif(int(pop[i,0])>k):
        k=k+1
        f=np.sum(comp)
        g=np.sum(internet)
        comp=[]
        internet=[]
        i=i-1
        if(k!=5 and k!=27 and k!=32):
            states.append(str(pop[i,1]))
            state_comp.append(f)
            state_internet.append(g)

total=np.sum(state_comp)
total1=np.sum(state_internet)
for i in range(0, len(state_comp)):
    comp_ratio.append(state_comp[i]/state_internet[i]*100)
            
comp1=np.array(comp_ratio).round(decimals=2)
labels=np.array(states)
a=np.argmax(comp1)
b=np.argmin(comp1)
print('This shows the comparison of different states of Indian based on Computer to Internet ratio per household.')
print()
print()
print('Computer\t    State Name')
for i in range(0,labels.size):
    print(comp1[i],'\t\t',labels[i])
print()
print()
print('State with maximum Computer to Internet ratio = ',labels[a])
print('State with minimum Computer to Internet ratio = ',labels[b])

font1 = {'family':'serif','color':'black','size':15}
font2 = {'family':'serif','color':'black','size':10}
# Figure Size
fig, ax = plt.subplots(figsize =(16, 9))
 
# Horizontal Bar Plot
ax.barh(labels, comp1)
 
# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
 
# Add padding between axes and labels
ax.xaxis.set_tick_params(pad = 5)
ax.yaxis.set_tick_params(pad = 10)
 
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
 
# Show top values 
ax.invert_yaxis()
 
# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5, 
             str(round((i.get_width()), 2)),
             fontsize = 10, color ='black')
ax.set_title("State wise Computer to Internet ratio facility per household", fontdict = font1)
plt.ylabel("States", fontdict = font2)
plt.xlabel("Computer to Internet Ratio", fontdict = font2)
plt.show()
