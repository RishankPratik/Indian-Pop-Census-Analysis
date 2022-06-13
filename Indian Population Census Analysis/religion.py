import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
pop = np.loadtxt(open("india-districts-census-2011.csv", "rb"), delimiter=",",skiprows=1, dtype=object)
k=1
population=[]
states=[]
hindu=[]
muslim=[]
sikhs=[]
christians=[]
buddhists=[]
jains=[]
other=[]
not_stated=[]
hindu_ratio=[]
muslim_ratio=[]
christians_ratio=[]
sikhs_ratio=[]
buddhists_ratio=[]
jains_ratio=[]
other_ratio=[]
not_stated_ratio=[]
for i in range(0, 640):
    if(int(pop[i,0])==k):
        population.append(int(pop[i,4]))
        hindu.append(int(pop[i,26]))
        muslim.append(int(pop[i,27]))
        christians.append(int(pop[i,28]))
        sikhs.append(int(pop[i,29]))
        buddhists.append(int(pop[i,30]))
        jains.append(int(pop[i,31]))
        other.append(int(pop[i,32]))
        not_stated.append(int(pop[i,33]))
    elif(int(pop[i,0])>k):
        k=k+1
        a=np.sum(population)
        f=np.sum(hindu)
        h=np.sum(muslim)
        c=np.sum(christians)
        d=np.sum(sikhs)
        e=np.sum(buddhists)
        g=np.sum(jains)
        j=np.sum(other)
        m=np.sum(not_stated)
        male_pop=[]
        female_pop=[]
        hindu=[]
        muslim=[]
        sikhs=[]
        christians=[]
        buddhists=[]
        jains=[]
        other=[]
        not_stated=[]
        i=i-1
        if(k!=5 and k!=27 and k!=32):
            states.append(str(pop[i,1]))
            hindu_ratio.append(f/a*100)
            muslim_ratio.append(h/a*100)
            christians_ratio.append(c/a*100)
            sikhs_ratio.append(d/a*100)
            buddhists_ratio.append(e/a*100)
            jains_ratio.append(g/a*100)
            other_ratio.append(j/a*100)
            not_stated_ratio.append(m/a*100)
            
hindu1=np.array(hindu_ratio).round(decimals=2)
muslim1=np.array(muslim_ratio).round(decimals=2)
christians1=np.array(christians_ratio).round(decimals=2)
sikhs1=np.array(sikhs_ratio).round(decimals=2)
buddhists1=np.array(buddhists_ratio).round(decimals=2)
jains1=np.array(jains_ratio).round(decimals=2)
other1=np.array(other_ratio).round(decimals=2)
not_stated1=np.array(not_stated_ratio).round(decimals=2)
labels=np.array(states)
a=np.argmax(hindu1)
b=np.argmin(hindu1)
c=np.argmax(muslim1)
d=np.argmin(muslim1)
e=np.argmax(christians1)
f=np.argmin(christians1)
g=np.argmax(sikhs1)
h=np.argmin(sikhs1)
i=np.argmax(buddhists1)
j=np.argmin(buddhists1)
k=np.argmax(jains1)
l=np.argmin(jains1)
m=np.argmax(other1)
n=np.argmin(other1)
o=np.argmax(not_stated1)
p=np.argmin(not_stated1)
print('This shows the comparison of different states of Indian based on their religion distribution.')
print()
print()
print('Hindu\tMuslim\tChristian\tSikh\tBuddhist Jain\tOther\tNot Stated\t   State Name')
for i in range(0,labels.size):
    print(hindu1[i],'\t',muslim1[i],'\t',christians1[i],'\t\t',sikhs1[i],'\t',buddhists1[i],'\t',jains1[i],'\t',other1[i],'\t',not_stated1[i],'\t\t',labels[i])
print()
print()
print('State with maximum Hindus = ',labels[a])
print('State with minimum Hindus = ',labels[b])
print('State with maximum Muslims = ',labels[c])
print('State with minimum Muslims = ',labels[d])
print('State with maximum Christian = ',labels[e])
print('State with minimum Christian = ',labels[f])
print('State with maximum Sikhs = ',labels[g])
print('State with minimum Sikhs = ',labels[h])
print('State with maximum Buddhists = ',labels[i])
print('State with minimum Buddhists = ',labels[j])
print('State with maximum Jains = ',labels[k])
print('State with minimum Jains = ',labels[l])
print('State with maximum Others = ',labels[m])
print('State with minimum Others = ',labels[n])
print('State with maximum Not Stated = ',labels[o])
print('State with minimum Not Stated = ',labels[p])
font1 = {'family':'serif','color':'black','size':15}
font2 = {'family':'serif','color':'black','size':10}
plt.title("State wise Religion Distribution", fontdict = font1)
plt.xlabel("States", fontdict = font2)
plt.ylabel("Religion (%)", fontdict = font2)
plt.plot(labels, hindu1, label = "Hindu")
plt.plot(labels, muslim1, label = "Muslim")
plt.plot(labels, christians1, label = "Christian")
plt.plot(labels, sikhs1, label = "Sikh")
plt.plot(labels, buddhists1, label = "Buddhist")
plt.plot(labels, jains1, label = "Jain")
plt.plot(labels, other1, label = "Other")
plt.plot(labels, not_stated1, label = "Not Stated")
plt.legend()
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
plt.xticks(rotation=90)
plt.show()
