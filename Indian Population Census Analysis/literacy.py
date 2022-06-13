import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
pop = np.loadtxt(open("india-districts-census-2011.csv", "rb"), delimiter=",",skiprows=1, dtype=object)
k=1
male_pop=[]
female_pop=[]
male_lit_ratio=[]
states=[]
female_lit_ratio=[]
male_lit=[]
female_lit=[]
for i in range(0, 640):
    if(int(pop[i,0])==k):
        male_pop.append(int(pop[i,5]))
        female_pop.append(int(pop[i,6]))
        male_lit.append(int(pop[i,8]))
        female_lit.append(int(pop[i,9]))
    elif(int(pop[i,0])>k):
        k=k+1
        a=np.sum(male_pop)
        b=np.sum(female_pop)
        f=np.sum(male_lit)
        h=np.sum(female_lit)
        male_pop=[]
        female_pop=[]
        male_lit=[]
        female_lit=[]
        i=i-1
        if(k!=5 and k!=27 and k!=32):
            states.append(str(pop[i,1]))
            r=f/a
            r=r*100
            c=h/b
            c=c*100
            male_lit_ratio.append(r)
            female_lit_ratio.append(c)
men=np.array(male_lit_ratio).round(decimals=2)
women=np.array(female_lit_ratio).round(decimals=2)
labels=np.array(states)
a=np.argmax(men)
b=np.argmin(men)
c=np.argmax(women)
d=np.argmin(women)
print('This shows the comparison of different states of Indian based on their respective male and female literacy index.')
print()
print()
print('State wise literacy rates according to gender')
print('Male\t Female\t\t    State Name')
for i in range(0,labels.size):
    print(men[i],'\t',women[i],'\t\t',labels[i])
print()
print()
print('State with maximum male literacy = ',labels[a])
print('State with minimum male literacy = ',labels[b])
print('State with maximum female literacy = ',labels[c])
print('State with minimum female literacy = ',labels[d])
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men, width, label='Men', align='center')
rects2 = ax.bar(x + width/2, women, width, label='Women', align='center')
# Add some text for labels, title and custom x-axis tick labels, etc.
font1 = {'family':'serif','color':'black','size':15}
font2 = {'family':'serif','color':'black','size':10}
ax.set_ylabel('Literacy Rates (%)', fontdict = font2)
ax.set_title('States wise Literacy rates gender wise', fontdict = font1)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontdict = font2)
ax.legend()
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
plt.xticks(rotation=90)
plt.show()
