import numpy as np
import matplotlib.pyplot as plt
pop = np.loadtxt(open("india-districts-census-2011.csv", "rb"), delimiter=",",skiprows=1, dtype=object)
k=1
male_pop=[]
female_pop=[]
pop_ratio=[]
states=[]
for i in range(0, 640):
    if(int(pop[i,0])==k):
        male_pop.append(int(pop[i,5]))
        female_pop.append(int(pop[i,6]))
    elif(int(pop[i,0])>k):
        k=k+1
        a=np.sum(male_pop)
        b=np.sum(female_pop)
        male_pop=[]
        female_pop=[]
        i=i-1
        if(k!=5 and k!=27 and k!=32):
            states.append(str(pop[i,1]))
            pop_ratio.append(a/b)
pop_gen_ratio=np.array(pop_ratio).round(decimals=2)
labels=np.array(states)
a=np.argmax(pop_gen_ratio)
b=np.argmin(pop_gen_ratio)
print('This shows the comparison of different states of Indian based on their respective male to female ration index and also the state with maximaum males and he one with minimum males.')
print()
print()
print('State wise Male to Female Ratio')
print('Male/Female\t    State Name')
for i in range(0,labels.size):
    print(' ',pop_gen_ratio[i],'\t\t',labels[i])
print()
print()
print('State with maximum male/female ratio = ',labels[a])
print('State with minimum male/female ratio = ',labels[b])

font1 = {'family':'serif','color':'black','size':15}
font2 = {'family':'serif','color':'black','size':10}
plt.title("State wise Male to Female Ratio", fontdict = font1)
plt.ylabel("States", fontdict = font2)
plt.xlabel("Male/Female", fontdict = font2)
plt.plot(pop_gen_ratio, labels, linewidth = 2, color = 'b', marker = 'o', ms = 5, mec = 'black', mfc = 'black')
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
plt.show()
